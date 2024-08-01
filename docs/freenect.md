# Freenect

Freenect is an open source driver for the Microsoft Kinect camera. It was developed by the Open Kinect community. You can check more about it in [their website](https://openkinect.org/wiki/Main_Page).

The freenect driver have many wrappers, including one for python. The main point of this repository is to document how the python wrapper works.

# Functions

## With runloop()

The freenect runloop is the main body. Every loop it calls a function to handle the video and depth. It also gives you the Device Pointer, which allow you to control / read stuff like the motor, accelerometer and LED.

Useful if your project relys heavily in the Kinect. If you only need the video/depth map, check how to avoid using the runloop in a section below.

### _freenect.runloop(depth=None, video=None, body=None, dev=None)_
**arguments: function, function, function, freenect.DevPtr**

This is the main function. It's pretty much a while True. The functions are supposed to handle the depth, video and everything else, in order. This is pretty much the only way to get a **freenect.DevPtr**.

If you have multiple kinects, you can specify which kinect you are using by providing the device context.

    Args:
        depth: A function that takes (dev, depth, timestamp), corresponding to C function. If None (default), then you won't get a callback for depth.

        video: A function that takes (dev, video, timestamp), corresponding to C function. If None (default), then you won't get a callback for video.

        body: A function that takes (dev, ctx) and is called in the body of process_events

        dev: Optional freenect device context. If supplied, this function will use it instead of creating and destroying its own...



### _freenect.get\_accel(dev)_
**arguments: freenect.DevPtr**

**returns: (int x, int y, int z)**

Return the (x,y,z) of the accelerometer

x : Horizontal axis rotation

y : Vertical axis rotation

z : Longitudinal axis rotation

The coordinates indicate how much it rotated in the axis in a range of (-10, 10), following this diagram:
![Diagram](https://www.mathworks.com/help/simulink/supportpkg/android_ref/simulinkandroidsupportpackage_galaxytab2_accelerometer.png)

The screen side equals kinect's camera side. For more information, look up "accelerometer coordinate systems".


### _freenect.set\_tilt\_degs(dev, angle)_
**arguments: freenect.DevPtr, int**

Sets Kinect's camera angle, in degrees.

The angle should be in the range: -30 < α < 30

Note that the leveling is not related to the base, but related to ground level.


### _freenect.set\_led(dev, option)_
**arguments: freenect.DevPtr, freenect.freenect_led_option**

Changes Kinect's LED. The LED options are:

    freenect.LED_OFF
    freenect.LED_GREEN
    freenect.LED_RED
    freenect.LED_YELLOW
    freenect.LED_BLINK_GREEN 
    freenect.LED_BLINK_RED_YELLOW


## Without runloop()

The following functions doesn't need the runloop. It's handy if you only need the video and depth.

### _freenect.sync\_get\_video(index=0, format=)_
**returns: numpy.ndarray video, int timestamp**

Returns the BGR video as a 480x640x3 numpy array and the timestamp.
Please note that it returns the video as a BGR video, instead of RGB. You can use cv2.cvtcolor(video, cv2.BGR2RGB).

### _freenect.sync\_get\_depth()_
**return: numpy.ndarray video, int timestamp**

Returns the depth map as a 480x640 numpy array and the timestamp.


