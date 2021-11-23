import spidev
import time
import crc16
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD
GPIO.setup(25, GPIO.OUT) # set a port/pin as an output

spi = spidev.SpiDev()
spi.open(0, 0)
spi.mode = 3
spi.max_speed_hz = 2000000


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

try:

    GPIO.output(25, 0)  # set GPIO24 to 1/GPIO.HIGH/True
    time.sleep(0.05)  # wait half a second
    GPIO.output(25, 1)  # set GPIO24 to 0/GPIO.LOW/False
    time.sleep(0.5)
    data = [0x5a, 0xa4, 0x10, 0x00, 0x03, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00,0xff, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00]
    crc_l_int, crc_h_int, crc_bytes= calculate_crc(data)
    data_crc = [0x5a, 0xa4, 0x10, 0x00, crc_h_int, crc_l_int ,0x03, 0x00, 0x00, 0x03,0x00, 0x00, 0x00, 0x00, 0xff,0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00]
    #data_check = [0x5a, 0xa4, 0x0c, 0x00, 0x2f, 0x65, 0x07, 0x00, 0x00, 0x02, 0x0c, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00]
    data_check = [0x5a, 0xa4, 0x10, 0x00, 0x4f, 0xed, 0x03, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00]
    print("Normal Request:", bytearray(data_check).hex())
    normal_request = spi.xfer2(data_check)
    ack_data = [0x5a, 0xa1]
    ack_request = spi.xfer2(ack_data)
    response_1 = spi.readbytes(74)
    # response_2 = bus.read_i2c_block_data(0x10, 0, 32)
    print("Normal Response:", bytearray(response_1).hex())
    time.sleep(5)
    ping = [0x5a, 0xa6]
    ping_request = spi.xfer2(ping)
    #time.sleep(0.5)
    print("Fuzz Request:", bytearray(data_crc).hex())
    fuzz_request = spi.xfer2(data_crc)
    #fuzz_request = spi.xfer2(data_crc)
    response_0 = spi.readbytes(500)
    print("Fuzz Response:", bytearray(response_0).hex())
    GPIO.cleanup()


except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()