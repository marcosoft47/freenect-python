''' Facilidades do freenect '''

import freenect
import numpy as np
import cv2 as cv
import time

lastTime = time.time()
__tiltLastTime = 0
__tiltCurState = 0

def getDepth():
    '''
        Retorna a profundidade como matriz do Numpy
    '''
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint16)
    return array

def getVideo():
    '''
        Retorna o vídeo como matriz do OpenCV
    '''
    array,_ = freenect.sync_get_video()
    array = cv.cvtColor(array,cv.COLOR_BGR2RGB) 
    return array

def runDisplayVideo(dev, data, timestamp):
    '''
        Roda o vídeo no runloop.
        Recomendado usar apenas em testes
    '''
    cv.imshow("RGB", cv.cvtColor(data, cv.COLOR_BGR2RGB))

def prettyDepth(depth, smoothness=0):
    '''
        Retorna a profundidade como uma matriz visivel para o opencv

        Args:
            depth: Mapa de profundidade
            smoothness: O quão liso quer a imagem
    '''
    np.clip(depth, 0, 1023, depth)
    depth >>= smoothness
    depth = depth.astype(np.uint8)
    return depth

def moverCorpo(dev: freenect.DevPtr, tilt: int, acc=False):
    """
        Move o corpo do Kinect
        Args:
            dev: Ponteiro de dispositivo do Kinect
            tilt: Inclinação da câmera
            acc: Acumula ou não na inclinação atual
    """
    global __tiltCurState
    if not acc:
        __tiltCurState = tilt
        freenect.set_tilt_degs(dev, tilt)
    else:
        if -30 < __tiltCurState + tilt < 30:
            __tiltCurState += tilt
            freenect.set_tilt_degs(dev, __tiltCurState)

'''
freenect.LED_BLINK_GREEN        
freenect.VIDEO_IR_10BIT_PACKED
freenect.DEPTH_10BIT            
freenect.LED_BLINK_RED_YELLOW   
freenect.VIDEO_IR_8BIT
freenect.DEPTH_10BIT_PACKED     
freenect.LED_GREEN              
freenect.VIDEO_RGB
freenect.DEPTH_11BIT            
freenect.LED_OFF                
freenect.VIDEO_YUV_RAW          
freenect.np                     
freenect.DEPTH_11BIT_PACKED     
freenect.LED_RED                
freenect.VIDEO_YUV_RGB
freenect.DEPTH_MM               
freenect.LED_YELLOW
freenect.DEPTH_REGISTERED       
freenect.RESOLUTION_HIGH
freenect.DEVICE_AUDIO           
freenect.RESOLUTION_LOW
freenect.DEVICE_CAMERA          
freenect.RESOLUTION_MEDIUM      
freenect.DEVICE_MOTOR           
freenect.VIDEO_BAYER
freenect.VIDEO_IR_10BIT         


freenect.CtxPtr()
freenect.get_tilt_state() 
freenect.set_video_callback()
freenect.get_video_format()
freenect.set_video_mode()
freenect.init()
freenect.shutdown()
freenect.start_depth()
freenect.num_devices()
freenect.start_video()
freenect.base_runloop()
freenect.open_device()
freenect.stop_depth()
freenect.close_device()
freenect.process_events()
freenect.stop_video()
freenect.error_open_device()
freenect.runloop()
freenect.sync_get_depth()
freenect.get_accel()
freenect.set_depth_callback()
freenect.sync_get_video()
freenect.StatePtr()
freenect.get_depth_format()
freenect.set_depth_mode()
freenect.sync_stop()
freenect.DevPtr()
freenect.get_mks_accel()
freenect.set_led()
freenect.update_tilt_state()
freenect.Kill()
freenect.get_tilt_degs()
freenect.set_tilt_degs()
'''