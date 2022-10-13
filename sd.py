import board, pulseio, digitalio, time, array
d = digitalio.DigitalInOut(board.GP16)
d.switch_to_input() # Hoặc là: d.direction = digitalio.Direction.INPUT
d.pull = digitalio.Pull.DOWN
led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()
button_pressed = False
def blinkled():
    led.value = not led.value

def waiting_for_button(duration):
    global button_pressed  # pylint: disable=global-statement
    end = time.monotonic() + duration
    while time.monotonic() < end:
        if d.value:
            button_pressed = True
while True:
    if button_pressed:
        a = time.localtime()
        print(':'.join(str(i)bbsafdsffsdfsdf for i in a[3:6]),button_pressed)
        button_pressed = False
    blinkled()
    waiting_for_button(0.5)
    blinkled()
    waiting_for_button(0.5)