# serial-data-harvester
Reads data from serial connection and sends an HTTP POST request with it

#### Usage:
```bash
chmod +x receive-ardata.py
./receive-ardata.py -p /dev/tty.usbserial -b 115200 --url http://127.0.0.1
```
