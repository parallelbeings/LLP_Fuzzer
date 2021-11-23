
# LLP USB

Low Level protocol(LLP) USB fuzzer can test the USB Standard Chapter 9 implemntation on device enumeration for USB device targets. The fuzzer sends from an USB host (Linux) an setup requests to the target device and  checks whether the wlength value is checked for. If the wlength value accepts arbitary length value then the device reads the controlled length value and responds back. This can lead to a potential buffer over read which can contain sensitive data. 

The fuzzer can be used in an linux environment with wlength set to 4095 bytes( Max support by the device drivers) or by issuing wlength requests upto 65535 bytes in a raspi system with modified linux driver. To setup a modifed driver in raspi-3/4 use this awesome script created by [Horac](https://github.com/h0rac/usb-tester/blob/main/prereq-pi.sh). You can also try out his fuzzer for more test coverage on USB devices. 

**Requirements:**

- pyusb
- python3

**Example usage:** 

`usage: usb_device_fuzzer.py [-h] -v IDVENDOR -p IDPRODUCT`

The idvendor and product vendor of the target device can be obtained from running 'lsusb' or dmesg logs in your linux system. 

`user@linux:~/LLP_Fuzzer$ sudo python3 usb_device_fuzzer.py -v 0x05a7 -p 0x40fe`

**To check for buffer over read in responses:**

If the recived size exceeds the normal response length, there can be a potential buffer overflow, In the below example, there is a request sent(-->) for "Get Descriptor" with wlength set to 4095 bytes, the target responded back with 4095 bytes. 

```
user@linux:~/LLP_Fuzzer$ sudo python3 usb_device_fuzzer.py -v 0x1fc9 -p 0x0021
Fuzzing Started
Fuzzing Get Status with values 0x80 started
Fuzzing Get Status with values 0x80 completed
Fuzzing Get Status with values 0x81 started
Fuzzing Get Status with values 0x81 completed
Fuzzing Get Status with values 0x82 Started
Fuzzing Get Status with values 0x82 completed
Fuzzing Get Status with values 0x83 Started
Fuzzing Get Status with values 0x83 completed
Fuzzing Get descriptor with values 0x80 Started
Request Sent: 128 6 512 0 4095 Received: Size : 41 array('B', [9, 2, 41, 0, 1, 1, 0, 192, 50, 9, 4, 0, 0, 2, 3, 0, 0, 3, 9, 33, 0, 1, 0, 1, 34, 76, 0, 7, 5, 129, 3, 60, 0, 1, 7, 5, 2, 3, 60, 0, 1])
--> Request Sent: 128 6 513 0 4095 Received: Size : 4095 array('B', [70, 32, 0, 8, 208, 104, 70, 1, 240, 150, 251, 0, 32, 56, 117, 0, 240, 12, 248, 0, 224, 6, 36, 1, 152, 49, 104, 136, 66, 8, 191, 32, 70, 1, 208, 18, 240, 127, 249, 189, 232, 254, 131, 0, 152, 1, 240, 137, 187, 8, 185, 3, 32, 112, 71, 67, 104, 19, 177, 0, 104, 91, 105, 24, 71, 6, 32, 112, 71, 248, 181, 69, 246, 24, 20, 5, 70, 193, 242, 0, 68, 32, 104, 132, 176, 12, 38, 3, 144, 15, 122, 1, 32, 251, 9, 7, 240, 15, 2, 16, 47, 29, 209, 5, 241, 108,```





