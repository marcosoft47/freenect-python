from easynect import *

ctx = freenect.init()
kinect = freenect.open_device(ctx, 1)
freenect.start_video(kinect)
freenect.start_depth(kinect)

while True:
    img = getVideo()
    cv.imshow("RGB", img)

    k = cv.waitKey(30)
    if k == ord("w"):
        moverCorpo(kinect)
    if k == ord("q"):
        break
cv.destroyAllWindows()