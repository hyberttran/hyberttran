import serial, time

ser = serial.Serial('com5', 115200,timeout=0)
sender = serial.Serial('com6', 115200,timeout=0)
time.sleep(0.5)
#sender.write(b'on')
i = 0
while True:
    if sender.in_waiting:
        print(i, sender.read_until(b'\r'))
        print(i, sender.read(10))
    else:
        print(i,"write")
        sender.write(b'on')
    time.sleep(2)
    i += 1
    #print(ser.readline())
    #a = sender.read()
    #sender.write(b'off')
    #time.sleep(1)
