import eznect
import cv2 as cv
import numpy as np
def invertDepth(depth:np.ndarray):
    # a = 
    # depth[2047-a] = depth[2047-a]
    return depth
if __name__ == "__main__":
    while True:
        img = eznect.getVideo()
        depth = eznect.getDepth()
        # ir = eznect.getIR()
        cv.imshow("RGB", img)
        cv.imshow("Depth", eznect.prettyDepth(depth, 2))
        # cv.imshow("IR", ir)
        k = cv.waitKey(30)
        if k == ord('q'): 
            break
    cv.destroyAllWindows()