identify-usb-driver
===================

This script automates the process of identifing the location of a usb devices sys and dev folders.

Originally written to location the correct driver folder and hook into bind/unbind events.

The script leverages output from lsusb to locate a device by it's vendorId and (optionally) it's productId.

The script is **not** smart enough to handle a situation where multiple devices result from the initial output and will simply take the last one. To avoid this, you can provide the productId as well or enhance the script logic.

Usage:
```bash
./identify.sh -m {Vid} [-p {Pid}]
```

Parameters:
| option | expected value | required? |
| --- | --- | --- |
| -m | manufacturer id in hex | ✅ |
| -p | product id in hex | |

Output:
```
sys: /sys/bus/usb/devices/1-1
dev: /dev/bus/usb/001/002
```
