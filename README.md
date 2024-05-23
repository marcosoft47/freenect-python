# freenect-python
Everything I gathered from freenect's python wrapper
 **Note:** The File _eznect.py_ was made to simplify some stuff. Feel free to add it in your projects!

# Functions

## _freenect.sync\_get\_video()_
**returns: numpy.ndarray video, int timestamp**

Return the BGR video as a 480x640x3 numpy array and the timestamp.
Please note that it returns the video as a BGR video, instead of RGB. You could use cv2.cvtcolor(video, cv2.BGR2RGB)

## _freenect.get\_accel(DevPtr dev)_
**returns: (int x, int y, int z)**
Return the (x,y,z) of the accelerometer

x : Horizontal axis rotation
y : Vertical axis rotation
z : Longitudinal axis rotation

I have no idea what the coordinates numbers actually mean. Maybe distance from the axis?

For more information, look up "gyroscope coordinate systems". If you figure it out, please contact me and ELI5.