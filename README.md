
# Readme
A working recipe to display raster images on a ssd1306 display using CircuitPython.
Developed for use with Trinket M0. As this is a minimal environment for CircuitPython support, better performance is expected with better hardware. 

![White Text](images/LogoWhiteText.png?raw=True)
![Black Text](images/LogoBlackText.png?raw=True)


As configured, this updates the image shown on a ssd1306 one line at a time. Uses I2C bus. Included image file is example used for demo at local Python club. 

## Tested environment specs:

 1. [CircuitPython 2.3.1](https://github.com/adafruit/circuitpython/releases/tag/2.3.1) -adafruit_ssd1306 library didn't work with the newly released 3.0.0; Not sure if framebuf.py is 3.0.0 compatible. 
 2. In the lib directory the following are required:
	 1. From the v2 [circuit python library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases):
		 - adafruit_bus_device/
		 - adafruit_register/
		 - adafruit_ssd1306.mpy
	2. [framebuf.mpy](https://github.com/adafruit/micropython-adafruit-framebuf/releases)
3. In the main CIRCUITPY directory of the device place:
	1. main.py (From this repo)
	2. image_to_display.txt


	 

## Current limitations:
 - Each image refresh is slow. Working with the Arduino libraries, this display is very responsive. It's not clear yet if this is a limitation of my hardware, or of the libraries being used. Takes ~1sec for oled.show() to complete. Due to limited flash memory of the Trinket M0, a [pure Python implementation of framebuf module](https://github.com/adafruit/micropython-adafruit-framebuf). I suspect a device supporting the native C module will refresh nearly instantly.
- As written, loading the full 128x64 image into RAM consumes all memory and dumps uc into the REPL (white LED). Working with 64x64 images completely fit into ram. Used tuples of 8bit binary literals when testing.

## Areas for improvement:
 - Process used to generate image is slow. Although accurate scaling of images will likely remain a manual task, once the image is the correct size, a program could be written that converts a multicolored image into a monochrome binary image easily interpreted for display on the ssd1306.
 - Use binary file rather than text file for image. Current image is 8K, but should reduce to 1K.

