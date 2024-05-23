import eznect
import freenect
import cv2 as cv

def main(dev, ctx):
    acc = freenect.get_accel(dev)
    k = cv.waitKey(10)
    if k == ord('q'):
        raise freenect.Kill
    if k == ord('t'):
        print(acc)
freenect.runloop(body=main,video=eznect.runDisplayVideo)