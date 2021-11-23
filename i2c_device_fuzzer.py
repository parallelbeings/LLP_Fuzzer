from smbus2 import SMBus
import time
import crc16
import re
from pprint import pprint

def calculate_crc(data):
    data_bytes = bytearray(data).hex()
    data_str = bytes.fromhex(data_bytes)
    crc_data = crc16.crc16xmodem(data_str)
    crc_hex = hex(crc_data)[2:]
    crc_bytes = bytes(crc_hex,encoding='utf8')
    crc_l = crc_bytes[:2].decode('ascii')
    crc_h = crc_bytes[2:4].decode('ascii')
    if crc_h == "":
        crc_l_int = int(crc_l, 16)
        crc_h_int = 00
    else:
        crc_l_int = int(crc_l, 16)
        crc_h_int = int(crc_h, 16)
    return crc_l_int, crc_h_int, crc_bytes


with SMBus(1) as bus: # 1 indicates /dev/i2c-1
    data = [0x5a, 0xa4, 0x0c, 0x00, 0x07, 0x00, 0x00, 0x02, 0x01, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00]
    crc_l_int, crc_h_int, crc_bytes= calculate_crc(data)
    data_crc = [0x5a, 0xa4, 0x0c, 0x00, crc_h_int, crc_l_int ,0x07, 0x00, 0x00, 0x02,0x01, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00]
    #data_check = [0x5a, 0xa4, 0x0c, 0x00, 0x2f, 0x65, 0x07, 0x00, 0x00, 0x02, 0x0c, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00]
    data_check = [0x5a, 0xa4, 0x10, 0x00, 0x4f, 0xed, 0x03, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00]
    normal_request = bus.write_i2c_block_data(0x10, 0, data_check)
    ack_data = [0x5a, 0xa1]
    bus.write_i2c_block_data(0x10, 0, ack_data)
    # response_2 = bus.read_i2c_block_data(0x10, 0, 32)
    print("Normal Request:", bytearray(data_check).hex())
    response_0 = bus.read_i2c_block_data(0x10, 0, 32)
    response_1 = bus.read_i2c_block_data(0x10, 0, 32)
    #response_2 = bus.read_i2c_block_data(0x10, 0, 32)
    print("Response_0:", bytearray(response_0).hex())
    print("Response_1:", bytearray(response_1).hex())
    #print("Response_1:", bytearray(response_2).hex())
    #time.sleep(1.0)
    #time.sleep(0.5)
    fuzz_request = bus.write_i2c_block_data(0x10, 0, data_crc)
    ack_data = [0x5a, 0xa1]
    bus.write_i2c_block_data(0x10, 0, ack_data)
    #bus.write_i2c_block_data(0x10, 0, ack_data)
    time.sleep(0.5)
    print("Fuzz Request:", bytearray(data_crc).hex())
    response_0_0 = bus.read_i2c_block_data(0x10, 0, 32)
    response_1_1 = bus.read_i2c_block_data(0x10, 0, 32)
    response_2_2 = bus.read_i2c_block_data(0x10, 0, 32)
    print("Fuzz Response:", bytearray(response_0_0).hex())
    print("Response_0:", bytearray(response_1_1).hex())
    print("Response_0:", bytearray(response_2_2).hex())
    #print("Response_1:", bytearray(response_2).hex())
    ack_data = [0x5a, 0xa1]
    bus.write_i2c_block_data(0x10, 0, ack_data)

"""
# NXP I2C ISP read/write command

#1. PING Command - Fuzz

for i in range(0,255,1):
    data = [i, 0xa6]
    request = bus.write_i2c_block_data(0x10, 0, data)
    print("Request:", bytearray(data))
    response = bus.read_i2c_block_data(0x10,0,32)
    print("Response:", bytearray(response))

    ack_data = [0x5a, 0xa1]
    ack = bus.write_i2c_block_data(0x10, 0, ack_data)
    print("Acknowledge:",bytearray(ack_data))
    #time.sleep(0.5)
    #exit(1)

#NXP Get Property Command Set

for i in range(0,255,1):
    data = [i, 0xa4, 0x0c, 0x00, 0x4b, 0x33, 0x07, 0x00, 0x00, 0x02, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    request = bus.write_i2c_block_data(0x10, 0, data)
    #print("Request:", bytearray(data).hex())
    ack_data = [0x5a, 0xa1]
    ack = bus.write_i2c_block_data(0x10, 0, ack_data)
    response = bus.read_i2c_block_data(0x10,0,len(data)+2)
    if response[0] != 0:
        print("Request:", bytearray(data).hex())
        print("Response:" , bytearray(response).hex())
    ack_data = [0x5a, 0xa1]
    ack = bus.write_i2c_block_data(0x10, 0, ack_data)
    #print("Acknowledge:",bytes(ack_data).hex())



from smbus2 import SMBus

with SMBus(1) as bus:
    # Write a block of 8 bytes to address 80 from offset 0
    data = [0x5a, 0xa6]
    bus.write_i2c_block_data(10, 0, data)

    # Read a block of 16 bytes from address 80, offset 0
    block = bus.read_i2c_block_data(10, 0, 16)
    # Returned value is a list of 16 bytes
    print(block)
"""
"""
--------------------------------------------------------------------------------------------
|Framing Packet Format (32 bytes)                                                          |
--------------------------------------------------------------------------------------------
|  Byte 0   |  Byte 1   | Byte 2 | Byte 3  | Byte 4   | Byte 5    |   Byte 6 to Byte n     | 
|           |           |        |         |          |           |                        |
|Start Byte |PacketType |Len_Low |Len_High |Crc16_low |Crc16_High |Command or Data Payload |                       
--------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------
|Command Packet Format (32 bytes)                                                    |
|-------------------------------------------------------------------------------------
|Command Header (4 bytes)    | 28 bytes for Parameters (Max 7 parameters             |
--------------------------------------------------------------------------------------
|Tag|Flags|Rsvd|Param Count  |Param 1|Param 2|Param 3|Param 4|Param 5|Param 6|Param 7|
|1    1     1      1byte      4byte   4byte   4byte   4byte   4byte   4byte   4byte  |
--------------------------------------------------------------------------------------
"""