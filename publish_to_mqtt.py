import serial, minimalmodbus

usb2s = '/dev/ttyUSB0'

instrument = minimalmodbus.Instrument(usb2s,102) # slave 102 is the grass area sensor 

instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.stopbits = 1
instrument.serial.parity   = serial.PARITY_NONE
instrument.mode = minimalmodbus.MODE_RTU 
instrument.serial.timeout = 0.5

ga_moisture = instrument.read_register(0,0)
ga_temperature = instrument.read_register(1,0)

# time.sleep(0.1) # small timeout to avoid minimalmodbus.NoResponseError
# instrument.address = 103 # slave 103 is the flower garden sensor
# fg_moisture = instrument.read_register(0,0)
# fg_temperature = instrument.read_register(1,0)

# print(f" grass area moisture reading: {ga_moisture} %")
# print(f" grass area temperature reading: {ga_temperature} {chr(176)}C")
# print(f" flower garden moisture reading: {fg_moisture} %")
# print(f" flower temperature reading: {fg_temperature} {chr(176)}C")

import paho.mqtt.publish as paho_publisher

mqtt_server = "192.168.2.8"
mqtt_port = 1883
mqtt_topic = "backyard_soil_sensors"
mqtt_client="achtertuin_hm"



msgs = [
         #  {
         #      "topic":f"{mqtt_topic}/l4",
         #      "payload":fg_temperature
         #  },
         #  {
         #      "topic":f"{mqtt_topic}/l5",
         #      "payload":fg_moisture
         #  },
           {
               "topic":f"{mqtt_topic}/l1",
               "payload":ga_moisture
           },
           {
               "topic":f"{mqtt_topic}/l3",
               "payload":ga_temperature
           }
       ]

paho_publisher.multiple(msgs,
                       hostname=mqtt_server,
                       port=mqtt_port,
                       client_id=mqtt_client)
