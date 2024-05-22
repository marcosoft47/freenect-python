from eznect import *


def body(dev, ctx):
    k = cv.waitKey(5)
    if k == ord("w"):
        moverCorpo(dev, 1, True)
    if k == ord("x"):
        moverCorpo(dev, -1, True)
    if k == ord("s"):
        moverCorpo(dev, 0)
    if k == ord("a"):
        freenect.set_led(dev, freenect.LED_GREEN)
    if k == ord("q"):
        raise freenect.Kill


freenect.runloop(video=runDisplayVideo, body=body)
cv.destroyAllWindows()