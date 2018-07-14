"""
Display image stored locally
Image file expected to be a text file consisting of zeros and ones

Simplified image creation process:
Create monochrome raster image. GIMP works well in Linux.
Convert image to simplified binary image.
- There are multiple tools for this, but the following website is recommended:
- http://makertum.com/en/bytearray-maker/
- Edit syntax so image is just zeros and ones

The image creation process could be more streamlined, but this gets 
the job done. This could also be generalized for reuse, but it should be
better understood how to figure out how to update the display faster before 
going too far down that path.

Written by: Carlin Kartchner
"""

import board
import busio as io
import adafruit_ssd1306

i2c = io.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

def show_img(file, invert=False):
    """
    Read locally stored image
    Update ssd1306 display one line at a time 
    :file: name of image file in same directory as main.py
    :invert: switch whether the pixel is on/off when displayed
    """
    f = open(file, 'r')
    row = 0
    col = 0
    for line in f:
        line=line.rstrip()
        for p in line:
            print(p)
            oled.pixel(col, row, int(p))
            oled.show()
            col += 1
        row += 1
        col = 0

file = '128x64_rtp_python_club_logo.txt'
while 1:
    show_img(file)
    show_img(file, True)
