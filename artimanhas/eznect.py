''' Facilidades do freenect '''

import freenect
import numpy as np
import cv2 as cv

__curLed = 0
__tiltCurState = 0
leds = [freenect.LED_OFF,
        freenect.LED_GREEN, 
        freenect.LED_RED, 
        freenect.LED_YELLOW, 
        freenect.LED_BLINK_GREEN, 
        freenect.LED_BLINK_RED_YELLOW]


def getDepth() -> np.ndarray:
    '''
        Retorna a profundidade como matriz do Numpy
    '''
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint16)
    return array

def getVideo() -> np.ndarray:
    '''
        Retorna o vídeo como matriz do OpenCV
    '''
    array,_ = freenect.sync_get_video()
    array = cv.cvtColor(array,cv.COLOR_BGR2RGB) 
    return array

def ciclarLed(dev: freenect.DevPtr):
    '''
        Cicla o LED para o próximo LED da fila
        Args:
            dev: Ponteiro de dispositivo do Kinect

        Fila: Desligado, Verde, Vermelho, Amarelo, Piscando Verde, Piscando Vermelho e Amarelo
    '''
    global __curLed
    __curLed += 1
    if __curLed > len(leds):
        __curLed = 0
    freenect.set_led(dev, leds[__curLed])

def mudarLed(dev: freenect.DevPtr, cor: int):
    '''
        Muda o Led para a cor especificada

        Args:
            dev: Ponteiro de dispositivo do Kinect
            cor: Constante da cor do LED
        
        Opções de cor:

            freenect.LED_OFF,
            freenect.LED_GREEN, 
            freenect.LED_RED, 
            freenect.LED_YELLOW, 
            freenect.LED_BLINK_GREEN, 
            freenect.LED_BLINK_RED_YELLOW
    '''
    if 0 <= cor <= 5:
        freenect.set_led(dev, cor)
    else:
        print("Cor inválida!\nEscolha uma das cores que o Freenect oferece (freenect.LED_*)")

def runDisplayVideo(dev, data, timestamp):
    '''
        Roda o vídeo no runloop.
        Recomendado usar apenas em testes
    '''
    cv.imshow("RGB", cv.cvtColor(data, cv.COLOR_BGR2RGB))

def prettyDepth(depth: np.ndarray, smoothness=0) -> np.ndarray:
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

def controlarKinect(dev: freenect.DevPtr, k: int):
    '''
        Controlador geral do Kinect
        Args:
            dev: Ponteiro de dispositivo do Kinect
            k: Código Unicode do caracter
                Use a função ord(caracter) para descobrir o código
        Botões:
        q: Encerra o runloop
        w: Sobe o motor da câmera em 1 grau
        x: Desce o motor da câmera em 1 grau
        s: Nivela a câmera
        l: Cicla o led
    '''
    k = ord(k)
    if k == ord('w'):
        moverCorpo(dev, 1, True)
    if k == ord('x'):
        moverCorpo(dev, -1, True)
    if k == ord('s'):
        moverCorpo(dev, 0)
    if k == ord("l"):
        ciclarLed(dev)
    if k == ord('q'):
        raise freenect.Kill


'''
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