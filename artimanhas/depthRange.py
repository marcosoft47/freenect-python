from eznect import getDepth,getVideo
import cv2 as cv
import numpy as np

if __name__ == "__main__":
    scope = 700
    threshold = 100
    while True:
        img = getVideo()
        a = np.zeros_like(getVideo())
        depth = getDepth()

        # mask = (scope - threshold < depth) & (depth < scope + threshold)
        mask = np.logical_and((scope - threshold < depth), (depth < scope + threshold))
        mask = np.logical_and(mask, depth != 2047)

        a[mask] = img[mask] # fonte: gepeto
        # a[np.logical_not(mask)] = (255,255,255)
        cv.imshow('img', a)
        k = cv.waitKey(1)
        if k == ord('w'):
            if scope+threshold<2047:
                scope+=threshold
            print(f'Escopo: {scope}')
        if k == ord('s'):
            if scope>threshold:
                scope-=threshold
            print(f'Escopo: {scope}')
        if k == ord('d'):
            threshold += 25
            print(f'Limiar: {threshold}')
        if k == ord('a'):
            threshold -= 25
            print(f'Limiar: {threshold}')
        if k == ord('q'):
            break
    
    cv.destroyAllWindows()
