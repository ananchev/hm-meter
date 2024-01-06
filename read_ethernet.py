from pymodbus.client.tcp import ModbusTcpClient
from time import sleep

# Create a Modbus TCP client
client = ModbusTcpClient('192.168.2.167', port=1025, debug=True)
connection = client.connect()
if client.connect():
    print("connected")
    
sleep(0.5)

# read registers 0000 and 0001
# 0000 provides the real-time value of moisture content (10 times larger) 
# 0001 provides real-time value of soil temperature (10 times larger) 
try:
    print(f"Connection is {connection}, socket is {client.is_socket_open()}")
    result = client.read_holding_registers(address=0, count=1, slave=105)
    if result.isError():
        print("Error reading register!")
        exit

    print(result)
    sleep(1)
    # Close the connection
    client.close()

except Exception as e:
    print(e)