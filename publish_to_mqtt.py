import serial, minimalmodbus

usb2s = '/dev/ttyUSB0'
instrument = minimalmodbus.Instrument(usb2s,102) # port name, Broadcast slave address
instrument.serial.baudrate = 4800      
instrument.serial.bytesize = 8
instrument.serial.stopbits = 1
instrument.serial.parity   = serial.PARITY_NONE
instrument.mode = minimalmodbus.MODE_RTU 
instrument.serial.timeout = 0.5

moisture = instrument.read_register(0,0)
print(f" moisture reading: {moisture} %")
temperature = instrument.read_register(1,0)
print(f" temperature reading: {temperature} {chr(176)}C")


import paho.mqtt.publish as paho_publisher

mqtt_server = "192.168.2.8"
mqtt_port = 1883
mqtt_topic = "hm-achter"
mqtt_client="tmp_achtertuin_hm"

msgs = [
           {
               "topic":"hm-achter/moisture",
               "payload":moisture
           },
           {
               "topic":"hm-achter/temperature",
               "payload":temperature
           }
       ]

paho_publisher.multiple(msgs, 
                       hostname="192.168.2.8", 
                       port=1883, 
                       client_id="tmp_achtertuin_hm")