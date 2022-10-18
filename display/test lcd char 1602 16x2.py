#!/usr/bin/python3
# -----------------------------------------------------------------------------
# CircuitPython library for the HD44780 with serial interface (PCF8574T)
#
# Sample code
#
# Website: https://github.com/bablokb/circuitpython-hd44780
#
# -----------------------------------------------------------------------------

import time, board, busio, sys
import hd44780

SLEEP = 5
COLS  = 16
ROWS  = 2

i2c = busio.I2C(board.GP21,board.GP20)
display = hd44780.HD44780(i2c)

while True:
  try:
    display.clear()
    display.write("Hello",1)
    display.write("CircuitPython",2)
    time.sleep(1)

    display.clear()
    display.write("backlight off!",1)
    time.sleep(0.5)
    display.backlight(False)
    time.sleep(2)

    display.clear()
    display.write("backlight on!",1)
    display.backlight(True)
    time.sleep(2)
  except:
    break

display.clear()
display.backlight(False)