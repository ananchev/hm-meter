import serial, minimalmodbus

# example device ID 103 on RPi UART
instrument = minimalmodbus.Instrument('/dev/ttyS0',103)

instrument.mode = minimalmodbus.MODE_RTU 
instrument.serial.baudrate = 9600      
instrument.serial.bytesize = 8
instrument.serial.stopbits = 1
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.timeout = 0.5

# holding register 2000, unsigned INT16
address = instrument.read_register(2000, functioncode=4)
print(f" instrument address: {address}")
# holding register 2001, unsigned INT16
baudrate = instrument.read_register(2001, functioncode=4)
print(f" baudrate: {baudrate}")