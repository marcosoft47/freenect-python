import eznect
import freenect
import cv2 as cv

def body(dev, ctx):
    k = cv.waitKey(5)
    if k == ord("w"):
        eznect.moveBody(dev, 1, True)
    if k == ord("x"):
        eznect.moveBody(dev, -1, True)
    if k == ord("s"):
        eznect.moveBody(dev, 0)
    if k == ord("a"):
        eznect.cycleLed(dev)
    if k == ord("q"):
        raise freenect.Kill

def video(dev, video, timestamp):
    cv.imshow("Video", video)

freenect.runloop(video=video, body=body)
cv.destroyAllWindows()