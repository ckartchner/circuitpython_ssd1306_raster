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

For use with ssd1306

Written by: Carlin Kartchner
"""

import board
import busio as io
import adafruit_ssd1306
import random

# Board dimensions
xdim = 128
ydim = 64

i2c = io.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)


def inverter(p, invert):
    if invert:
        p = p ^ 1  # Bitwise XOR
    return p


def row_sweep(file, dir='t2b', invert=False):
    """
    Update dipslay one row at a time

    :file: name of image file in same directory as main.py
    :dir: direction row sweeps
    :invert: switch whether the pixel is on/off when displayed
    """
    f = open(file, 'r')
    col = 0
    if dir == 'b2t':
        sweep = range(ydim-1, -1, -1)
    else:  # t2b
        sweep = range(0, ydim)
    for row in sweep:
        pos = row * (xdim + 1)
        f.seek(pos, 0)
        line = f.readline()
        line = line.rstrip()
        for p in line:
            p = inverter(int(p), invert)
            oled.pixel(col, row, p)
            col += 1
        col = 0
        oled.show()


def col_sweep(file, dir='l2r', invert=False):
    """
    Update dipslay one column at a time

    :file: name of image file in same directory as main.py
    :dir: direction column sweeps
    :invert: switch whether the pixel is on/off when displayed
    """
    # Default sweep is left to right
    if dir == 'r2l':
        sweep = range(xdim-1, -1, -1)
    else:  # l2r
        sweep = range(0, xdim)
    for col in sweep:
        f = open(file, 'r')
        row = 0
        for line in f:
            p = inverter(int(line[col]), invert)
            oled.pixel(col, row, p)
            row += 1
        oled.show()


def call_rand(ival):
    """
    Randomly call row or column sweep

    :ival: boolean indicating if inversion should be done or not
    """
    updown = ['b2t', 't2b']
    leftright = ['r2l', 'l2r']
    dirs = updown + leftright
    dir = random.choice(dirs)
    if dir in updown:
        row_sweep(file, dir, ival)
    else:
        col_sweep(file, dir, ival)


file = '128x64_rtp_python_club_logo.txt'
# Quick start display
row_sweep(file, 't2b', False)
while 1:
    call_rand(True)
    call_rand(False)
