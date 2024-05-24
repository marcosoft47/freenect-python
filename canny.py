# Example showcasing how you can use OpenCV stuff in the runloop

import cv2 
import eznect
import freenect

def canny_edge_detection(frame): 
	# Convert the frame to grayscale for edge detection 
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	
	# Apply Gaussian blur to reduce noise and smoothen edges 
	blurred = cv2.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.5) 
	
	# Perform Canny edge detection 
	edges = cv2.Canny(blurred, 70, 135) 
	# edges = cv2.Sobel(src=blurred, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
	
	return blurred, edges

def displayVideo(dev, data, timestamp):
    blurred, edges = canny_edge_detection(data) 
    cv2.imshow("RGB", cv2.cvtColor(data, cv2.COLOR_BGR2RGB))
    # cv2.imshow("Edges", edges) 

def displayDepth(dev, data, timestamp):
     cv2.imshow("Depth", eznect.prettyDepth(data))
	
def main(dev, ctx): 
    
    # Exit the loop when 'q' key is pressed 
    k = cv2.waitKey(1)
    if k == ord("w"):
        eznect.moverCorpo(dev, 1, True)
    if k == ord("x"):
        eznect.moverCorpo(dev, -1, True)
    if k == ord("s"):
        eznect.moverCorpo(dev, 0)
    if k == ord("q"): 
        raise freenect.Kill
	
	# Release the webcam and close the windows 

freenect.runloop(body=main, video=displayVideo, depth=displayDepth)

cv2.destroyAllWindows()