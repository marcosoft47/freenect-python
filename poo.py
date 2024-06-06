import cv2 as cv
import numpy as np
import freenect
while True:
    depth,_ = freenect.sync_get_depth()
    depth = depth.astype(np.uint16)

    np.clip(depth, 0, 1023, depth)
    depth >>= 2
    depth = depth.astype(np.uint8)

    cv.imshow('Colmeia', depth)
    if cv.waitKey(10) == ord('q'):
        break
cv.destroyAllWindows()

