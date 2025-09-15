# Example showcasing that you don't need the runloop to get it working!
# It uses freenect.sync_get_depth() and freenect.sync_get_video()
# TODO: make it simpler, add more functions

import cv2 as cv
import freenect
import numpy as np
from eznect import getDepth, getVideo

if __name__ == "__main__":
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    font = cv.FONT_HERSHEY_SIMPLEX
    showText = False
    depth = getDepth() # If we catch it earlier, it won't stutter when we start the real thing
    while True:
        img = getVideo()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    
        for (x,y,w,h) in faces: 
            forehead_x = x+w//2
            forehead_y = y+h//8
            depth = getDepth()
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,128),2)
            cv.rectangle(img,(forehead_x,0),(forehead_x,1080),(0,0,0),2)
            cv.rectangle(img,(0,forehead_y),(1920,forehead_y),(0,0,0),2)
            cv.circle(img,(forehead_x,forehead_y),w//20,(0,0,255),-1)
            cv.putText(img,f'({forehead_x}, {forehead_y}, {depth[forehead_y][forehead_x]})',(forehead_x+10,forehead_y+20), font, .5,(255,255,255),1,cv.LINE_AA)
            if showText:
                cv.putText(img,f'({forehead_x}, {forehead_y}, {depth[forehead_y][forehead_x]})',(0,300), font, 2,(0,0,0),6,cv.LINE_AA)
                cv.putText(img,f'({forehead_x}, {forehead_y}, {depth[forehead_y][forehead_x]})',(0,300), font, 2,(255,255,255),3,cv.LINE_AA)
        cv.imshow('Advanced AI Killing Machine (It\' Joever)',img) 
    
        k = cv.waitKey(30) & 0xff
        if k == ord('q'): 
            break
        elif k == ord('t'): 
            showText = not showText
    cv.destroyAllWindows()  
