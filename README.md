# LLP Fuzzer

Low Level protocol(LLP) fuzzer can be used to test USB, SPI, I2C and UART device side implementation in microcontrollers for security bugs.

LLP fuzzer can help developers to test their peripheral device side implemntation in microcontrollers for any security vulnerabilities. The fuzzer has support for three protocols( USB, SPI and I2C) used in modern microcontrollers. LLPF is a dumb fuzzer i.e Basically it iterates through the bytes(creates malfromed inputs) for the above protocol and see how the device responds. 

To monitor the devices while the fuzzer runs, we plan to use the below instrumentation techniques.

- To check for length of each response we get from the device. 
- To check whether the microcontroller resets. - Planned
- To check whether device works normally by sending a ping request after every fuzzed request.  - Planned

The instructions for using the fuzzer can be found below, 

- [USB device Fuzzer](https://github.com/Xen1thLabs-AE/LLP_Fuzzer/blob/main/usb.md)
- [SPI device Fuzzer](https://github.com/Xen1thLabs-AE/LLP_Fuzzer/blob/main/spi.md)
- [I2C device Fuzzer](https://github.com/Xen1thLabs-AE/LLP_Fuzzer/blob/main/i2c.md)


