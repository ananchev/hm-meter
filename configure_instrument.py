import serial, minimalmodbus

usb2s = '/dev/ttyUSB0'

# broadcast address 0XFF (decimal 255) returns the device ID
instrument = minimalmodbus.Instrument(usb2s,104) # port name, Broadcast slave address


instrument.serial.baudrate = 9600      
instrument.serial.bytesize = 8
instrument.serial.stopbits = 1
instrument.serial.parity   = serial.PARITY_NONE
instrument.mode = minimalmodbus.MODE_RTU 

instrument.serial.timeout = 0.5

# set device id = 104
# register 07D0 is 2000 decimal 
instrument.write_register(2000,104,0)
print("New device id is set")
print("Modify the script using the new ID if furhter configuration is needed")

# # set baudrate = 9600
#     # Zero is 2400
#     # One is 4800
#     # Two is 9600
# # register 07D1 is 2001 decimal
# instrument.write_register(2001,2,0)
# print(f"new baudrate is 9600")