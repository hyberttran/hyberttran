# SPDX-FileCopyrightText: 2022 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board,busio

from adafruit_ht16k33 import segments

# Create the display object.
# Display connected to STEMMA QT connector.
i2c = busio.I2C(board.GP5,board.GP4)
display = segments.Seg14x4(i2c)
# Display connected to I2C pins.
# display = segments.Seg14x4(board.I2C())

# This section displays four 0's across the display. The code shows four
# different ways to use the set_digit_raw function. Each is labeled below.
# 16-bit Hexadecimal number
display.set_digit_raw(0, 0x2D3F)
time.sleep(1)
# 16-bit Binary number
display.set_digit_raw(1, 0b0010110100111111)
time.sleep(1)
# 8-bit Binary Tuple
display.set_digit_raw(2, (0b00101101, 0b00111111))
time.sleep(1)
# 8-bit Hexadecimal List
display.set_digit_raw(3, [0x2D, 0x3F])
time.sleep(1)

# Delay between.
time.sleep(2)

# Scroll "Hello, world!" across the display. Setting the loop parameter to false allows you to
# tell the marquee function to run only once. By default, marquee loops indefinitely.
display.marquee("XIN CHAO --GIPT----", loop=0)
time.sleep(1)
display.marquee("XIN CHAO **THOR****", loop=0)
time.sleep(1)
display.marquee("XIN CHAO \"\"CUONG\"\"\"\"", loop=0)
time.sleep(1)
display.marquee("MINH LA __HIEN____", loop=0)
# Delay between.
time.sleep(2)

# Scroll special characters, uppercase and lowercase letters, and numbers across
# the display in a loop. This section will continue to run indefinitely.
display.marquee("  ".join(chr(character) for character in range(ord("!"), ord("z") + 1)))