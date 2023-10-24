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

    bmRequestTypes = [0x80, 0x81, 0x82, 0x83]
    bRequests = [0, 6, 8, 10]

    for bmRequestType in bmRequestTypes:
        for bRequest in bRequests:
            print(
                f"Fuzzing Get Status with values bmRequestType=0x{bmRequestType:02X} and bRequest={bRequest} started"
            )
            for i in range(0, 65536, 1):
                if i > 10 and i % 100 == 0:
                    print(".", end="")
                try:
                    send = dev.ctrl_transfer(bmRequestType, 0, i, lang_id, length)
                    if len(send) >= size:
                        print(
                            f"Request Sent: {bmRequestType:02X} 0 {i} {lang_id} {length}\n"
                            f"Received: {str(send)} Size: {len(send)}"
                        )
                except:
                    pass
            print("")
            print(
                f"Fuzzing Get Status with values bmRequestType=0x{bmRequestType:02X} and bRequest={bRequest} completed"
            )


if __name__ == "__main__":
    run_usb_fuzzer()
