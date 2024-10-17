import cv2
import numpy as np
import freenect
import csv

def prettyDepth(depth: np.ndarray, smoothness=0) -> np.ndarray:
    '''
        Return depth as a smoother depth map, for better visualization

        Args:
            depth: Depth map
            smoothness: How smooth the depth map will become
    '''
    np.clip(depth, 0, 2047, depth)
    depth >>= smoothness
    depth = depth.astype(np.uint8)
    return depth

def depth2Rgb(depth: np.ndarray) -> np.ndarray:
    '''
        Return depth in RGB: value -> [value,value,value]
        Args:
            depth: Depth map
    '''
    depth = prettyDepth(depth)
    return np.repeat(depth[:, :, np.newaxis], 3, axis=2)

def body(dev, ctx):
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        raise freenect.Kill
    
    
    
def depth(dev, data, timestamp):
    depth = data

    # depth = prettyDepth(depth)
    depth = depth2Rgb(depth)
    cv2.imshow('Profundidade', depth)
    outd.write(depth)
    
def video(dev, data, timestamp):
    img = data
    img = img[:, :, ::-1]
    cv2.imshow('Colmeia', img)
    out.write(img)



cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'XVID') # type: ignore         
out = cv2.VideoWriter('rgb.avi', fourcc, 30.0, size)
outd = cv2.VideoWriter('depth.avi', fourcc, 30.0, size)

with open('dados.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['t','rx','ry','rz','ax','ay','az'])
    freenect.runloop(video=video, body=body, depth=depth)

cap.release()
out.release()
outd.release()
cv2.destroyAllWindows()

