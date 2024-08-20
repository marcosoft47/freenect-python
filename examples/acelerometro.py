import kinect.examples.eznect as eznect
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
freenect.runloop(body=main,video=eznect.runDisplayVideo)