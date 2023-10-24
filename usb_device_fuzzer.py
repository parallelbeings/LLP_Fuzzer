#!/usr/bin/python3
# Modules used for USB Fuzzer

import argparse
import usb.core


def run_usb_fuzzer():
    """Run USB Fuzzer"""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--idVendor",
        required=True,
        help="Enter the vendor id(Vid) of USB target device",
    )
    parser.add_argument(
        "-p",
        "--idProduct",
        required=True,
        help="Enter the product id(Pid) of USB target device",
    )

    args1 = parser.parse_args()

    # Code to fuzz the USB device target in microcontrollers
    if args1.idVendor:
        args1.idVendor = int(args1.idVendor, 16)
    if args1.idProduct:
        args1.idProduct = int(args1.idProduct, 16)

    dev = usb.core.find(idVendor=args1.idVendor, idProduct=args1.idProduct)
    interface = 0

    if dev.is_kernel_driver_active(interface) is True:
        # tell the kernel to detach
        dev.detach_kernel_driver(interface)
        # claim the device
        usb.util.claim_interface(dev, interface)

    lang_id = 0x0
    length = 0xFFF
    size = 40

    print("Fuzzing Started")

    print("Fuzzing Get Status with values 0x80 started")
    for i in range(0, 65536, 1):
        try:
            send = dev.ctrl_transfer(0x80, 0, i, lang_id, length)
            if len(send) >= size:
                print(
                    "Request Sent:",
                    0x80,
                    0,
                    i,
                    lang_id,
                    length,
                    "Received: " "Size :",
                    len(send),
                    str(send),
                )
        except:
            pass
    print("Fuzzing Get Status with values 0x80 completed")

    print("Fuzzing Get Status with values 0x81 started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x81, 0, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x81 0 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get Status with values 0x81 completed")

    print("Fuzzing Get Status with values 0x82 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x82, 0, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x82 0 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get Status with values 0x82 completed")

    print("Fuzzing Get Status with values 0x83 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x83, 0, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x83 0 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get Status with values 0x83 completed")

    print("Fuzzing Get descriptor with values 0x80 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x80, 6, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x80 6 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get descriptor with values 0x80 completed")

    print("Fuzzing Get descriptor with values 0x81 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x81, 6, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x81 6 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get descriptor with values 0x81 completed")

    print("Fuzzing Get descriptor with values 0x82 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x82, 6, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x82 6 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get descriptor with values 0x82 completed")

    print("Fuzzing Get descriptor with values 0x83 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x83, 6, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x83 6 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get descriptor with values 0x83 completed")

    print("Fuzzing Get Configuration with values 0x80 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x80, 8, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x80 8 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get Configuration with values 0x80 completed")

    print("Fuzzing Get Configuration with values 0x81 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x81, 8, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x81 8 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get Configuration with values 0x81 completed")

    print("Fuzzing Get Configuration with values 0x82 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x82, 8, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x82 8 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get Configuration with values 0x82 completed")

    print("Fuzzing Get Configuration with values 0x83 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x83, 8, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x83 8 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get Configuration with values 0x83 completed")

    print("Fuzzing Get Interface with values 0x80 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x80, 10, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x80 10 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get Interface with values 0x80 completed")

    print("Fuzzing Get Interface with values 0x81 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x81, 10, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x81 10 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get Interface with values 0x81 completed")

    print("Fuzzing Get Interface with values 0x82 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x82, 10, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x82 10 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass
    print("Fuzzing Get Interface with values 0x82 completed")

    print("Fuzzing Get Interface with values 0x83 Started")
    for i in range(0, 65535, 1):
        try:
            send = dev.ctrl_transfer(0x83, 10, i, lang_id, length)
            if len(send) >= size:
                print(
                    f"Request Sent: 0x83 10 {i} {lang_id} {length}\n"
                    f"Received: {str(send)} Size: {len(send)}"
                )
        except:
            pass

    print("Fuzzing Get Interface with values 0x83 completed")


if __name__ == "__main__":
    run_usb_fuzzer()
