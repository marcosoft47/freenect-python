import eznect
import cv2 as cv
while True:
    depth = eznect.getDepth()
    depth = eznect.cvDepth(depth,2)

    cv.imshow('Colmeia', depth)
    if cv.waitKey(10) == ord('q'):
        break
cv.destroyAllWindows()

