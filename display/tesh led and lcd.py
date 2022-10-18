import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_ht16k33 import segments
import adafruit_displayio_sh1106
import time

displayio.release_displays()

i2c = busio.I2C(board.GP5, board.GP4)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)


WIDTH = 130 #should be 128, but at the right side of the screen there are some disturb
HEIGHT = 64
BORDER = 2
WHITE = 0xFFFFFF
BLACK = 0x000000

display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = WHITE  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = BLACK  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
splash.append(inner_sprite)

# Draw a label
text = "Hi GIPT!"
text_area = label.Label(terminalio.FONT, text=text, color=WHITE, x=WIDTH // 2 - 20, y=10)
splash.append(text_area)

text = "I2C with sh1106"
text_area = label.Label(terminalio.FONT, text=text, color=WHITE, x=6, y=20)
splash.append(text_area)

text = "Hello Thor!"
text_area = label.Label(terminalio.FONT, text=text, color=WHITE, x=10, y=30)
splash.append(text_area)
text = "Hello Cuong!"
text_area = label.Label(terminalio.FONT, text=text, color=WHITE, x=10, y=40)
splash.append(text_area)
text = "Hello Hybert!"
text_area = label.Label(terminalio.FONT, text=text, color=WHITE, x=10, y=50)
splash.append(text_area)

i2c2 = busio.I2C(board.GP3, board.GP2)

display2 = segments.Seg14x4(i2c2)
# Display connected to I2C pins.
# display = segments.Seg14x4(board.I2C())

# This section displays four 0's across the display. The code shows four
# different ways to use the set_digit_raw function. Each is labeled below.
# 16-bit Hexadecimal number
display2.set_digit_raw(0, 0x2D3F)
time.sleep(1)
# 16-bit Binary number
display2.set_digit_raw(1, 0b0010110100111111)
time.sleep(1)
# 8-bit Binary Tuple
display2.set_digit_raw(2, (0b00101101, 0b00111111))
time.sleep(1)
# 8-bit Hexadecimal List
display2.set_digit_raw(3, [0x2D, 0x3F])
time.sleep(1)

# Scroll "Hello, world!" across the display. Setting the loop parameter to false allows you to
# tell the marquee function to run only once. By default, marquee loops indefinitely.
display2.marquee("XIN CHAO --GIPT----", loop=0)
time.sleep(1)
display2.marquee("XIN CHAO **THOR****", loop=0)
time.sleep(1)
display2.marquee("XIN CHAO \"\"CUONG\"\"\"\"", loop=0)
time.sleep(1)
display2.marquee("MINH LA __HIEN____", loop=0)
# Delay between.
time.sleep(2)

# Scroll special characters, uppercase and lowercase letters, and numbers across
# the display in a loop. This section will continue to run indefinitely.
display2.marquee("  ".join(chr(character) for character in range(ord("!"), ord("z") + 1)))