''' Freenect, but easier! '''

import freenect
from freenect import np

__curLed = 0
__tiltCurState = 0
leds = [freenect.LED_OFF,
        freenect.LED_GREEN, 
        freenect.LED_RED, 
        freenect.LED_YELLOW, 
        freenect.LED_BLINK_GREEN, 
        freenect.LED_BLINK_RED_YELLOW]


def getIR() -> np.ndarray:
    '''
        Returns Kinect's infrared feed
    '''
    array,_ = freenect.sync_get_video(0, freenect.VIDEO_IR_8BIT)
    np.clip(array, 0, 2047, array)
    return array

def getVideo() -> np.ndarray:
    '''
        Return Kinect's video

        Returns:
            Video as a numpy array in RGB format
    '''
    array,_ = freenect.sync_get_video()
    array = array[:, :, ::-1]
    return array

def getDepth() -> np.ndarray:
    '''
        Returns Kinect's depth as a numpy array

        Returns:
            Depth as a numpy array in uint16 format
    '''
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint16)
    return array

def prettyDepth(depth: np.ndarray, smoothness=0) -> np.ndarray:
    '''
        Return depth as a smoother depth map

        Args:
            depth: Depth map
            smoothness: How smooth the depth map will become
    '''
    np.clip(depth, 0, 2047, depth)
    depth >>= smoothness
    depth = depth.astype(np.uint8)
    return depth


def cycleLed(dev: freenect.DevPtr):
    '''
        Cycles between LEDs
        Args:
            dev: Kinect device pointer
        Queue: OFF, GREEN, RED, YELLOW, BLINKING GREEN, BLINKING RED AND YELLOW
    '''
    global __curLed
    __curLed += 1
    if __curLed > len(leds):
        __curLed = 0
    freenect.set_led(dev, leds[__curLed])

def changeLed(dev: freenect.DevPtr, color: int):
    '''
        Changes LED to specified color

        Args:
            dev: Kinect device pointer
            color: LED's color
        
        color options:
            0: freenect.LED_OFF,
            1: freenect.LED_GREEN, 
            2: freenect.LED_RED, 
            3: freenect.LED_YELLOW, 
            4: freenect.LED_BLINK_GREEN, 
            5: freenect.LED_BLINK_RED_YELLOW
    '''
    if 0 <= color <= 5:
        freenect.set_led(dev, color)
    else:
        print("Invalid color!\nChoose one that Freenect offers (freenect.LED_*)")

def moveBody(dev: freenect.DevPtr, tilt: int, accumulate=False):
    """
        Moves Kinect's body
        Args:
            dev: Kinect device pointer
            tilt: Body's inclination
            accumulate: Accumulates to inclination or not
    """
    global __tiltCurState
    if not accumulate:
        __tiltCurState = tilt
        freenect.set_tilt_degs(dev, tilt)
    else:
        if -30 < __tiltCurState + tilt < 30:
            __tiltCurState += tilt
            freenect.set_tilt_degs(dev, __tiltCurState)

def controlKinect(dev: freenect.DevPtr, k: int):
    '''
        Compilation of buttons to control the Kinect
        Args:
            dev: Kinect device pointer
            k: character unicode
                use ord(char) to find the character unicode
        Botões:
        q: Kills the runloop
        w: Tilt the body 1 degree above
        x: Tilt the body 1 degree below
        s: Levels the body
        l: Cycles between LEDs
    '''
    if k == ord('w'):
        moveBody(dev, 1, True)
    if k == ord('x'):
        moveBody(dev, -1, True)
    if k == ord('s'):
        moveBody(dev, 0)
    if k == ord("l"):
        cycleLed(dev)
    if k == ord('q'):
        raise freenect.Kill

'''
Bunch of stuff that the lib have


freenect.LED_OFF
freenect.LED_GREEN
freenect.LED_RED
freenect.LED_YELLOW
freenect.LED_BLINK_GREEN 
freenect.LED_BLINK_RED_YELLOW

freenect.VIDEO_IR_10BIT_PACKED
freenect.DEPTH_10BIT
freenect.VIDEO_IR_8BIT
freenect.DEPTH_10BIT_PACKED
freenect.VIDEO_RGB
freenect.DEPTH_11BIT
freenect.VIDEO_YUV_RAW          
freenect.np
freenect.DEPTH_11BIT_PACKED
freenect.VIDEO_YUV_RGB
freenect.DEPTH_MM
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