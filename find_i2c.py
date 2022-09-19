import machine

sda_pin = machine.Pin(23)
scl_pin = machine.Pin(22)

i2c = machine.I2C(sda = sda_pin, scl = scl_pin, freq = 10000)

devices = i2c.scan()

if len(devices) == 0:
 print("No i2c device !")
else:
 print('i2c devices found:',len(devices))
for device in devices:
 print("At address: ",hex(device))

