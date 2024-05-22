from eznect import *

if __name__ == "__main__":
    while True:
        img = getVideo()
        depth = getDepth()
        cv.imshow("RGB", img)
        cv.imshow("Depth", prettyDepth(depth))
        k = cv.waitKey(30) & 0xff
        if k == ord('q'): 
            break
    cv.destroyAllWindows()