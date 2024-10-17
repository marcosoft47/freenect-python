import eznect
import freenect
import cv2 as cv

def main(dev, ctx):
    acc = freenect.get_accel(dev)
    k = cv.waitKey(10)
    if k == ord("w"):
        eznect.moveBody(dev, 1, True)
    if k == ord("x"):
        eznect.moveBody(dev, -1, True)
    if k == ord("s"):
        eznect.moveBody(dev, 0)
    if k == ord('q'):
        raise freenect.Kill
    if k == ord('t'):
        print(acc)

def displayVideo(dev, data, timestamp):
    cv.imshow("RGB", cv.cvtColor(data, cv.COLOR_BGR2RGB))
freenect.runloop(body=main,video=displayVideo)