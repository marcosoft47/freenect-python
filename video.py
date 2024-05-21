import freenect
import numpy as np
import cv2 as cv
def get_depth():
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint16)
    return array

def get_video():
    array,_ = freenect.sync_get_video()
    array = cv.cvtColor(array,cv.COLOR_RGB2BGR)
    return array

if __name__ == "__main__":
    while True:
        img = get_video()
        cv.imshow("colmeia", img)