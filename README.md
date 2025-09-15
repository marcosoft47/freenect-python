# Freenect's Python Wrapper
Everything I gathered from freenect's python wrapper

 **Note:** The file `eznect.py` was made to gather useful functions. Feel free to add it in your projects!

# Installation

To install freenect, you will need to download the drivers and the python wrapper.

The drivers can be downloaded with your favorite package manager, or by [building the source](https://github.com/OpenKinect/libfreenect)

    sudo dnf install libfreenect

The python wrapper is supposed to be downloaded with the source, but I never managed to download it right. You can install with your package manager (there's no python wrapper in apt, sorry debian/ubuntu users)

    sudo dnf install python3-libfreenect

# How to use it

Check the [docs folder](https://github.com/marcosoft47/freenect-python/tree/main/docs) and the other examples in the examples folder.

# Troubleshooting
## Fixnect

Sometimes, you may get a libusb error, saying access denied. This happens because libusb doesn't have the proper permissions to read the Kinect camera. The following command may fix it:

    sudo chmod -R 777 /dev/bus/usb/

It might not be a good idea to use `chown` instead of chmod. It will make your USB ports much more vulnerable.

Since it happens frequently, I suggest you to make it an alias. Add the following to your `.bashrc` (or similar) file, so you can just run `fixnect` in your terminal

    alias fixnect="sudo chmod -R 777 /dev/bus/usb/"

## Autocomplete / Intelisense not working

Pylance doesn't recognize freenect properly. Use Jedi instead.

In VS Code, go to: Settings > python.languageserver > jedi

## Your english sucks

lmao cry about it

## RTFM

I tried my best to compile every (useful) technical detail in the docs folder.