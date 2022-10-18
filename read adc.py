import board
import digitalio
import pwmio
import analogio
import time

res = analogio.AnalogIn(board.A0)
led = pwmio.PWMOut(board.GP16, frequency=1000)
time.sleep(3)
while True:
    print(res.value, res.value/2**16)
    led.duty_cycle = res.value
    time.sleep(1)