#!/usr/bin/env python3

import sys
import argparse
from datetime import datetime

import serial
import requests


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--baudrate', type=int, default=9600)
    parser.add_argument('-p', '--port', required=True)
    parser.add_argument('-u', '--data-url', required=True)
    argv = parser.parse_args(sys.argv[1:] or args)

    with serial.Serial(port=argv.port, baudrate=argv.baudrate, timeout=10) as ser:
        with requests.Session() as s:
            while True:
                value = ser.readline().decode()
                print(datetime.now().isoformat(timespec='seconds'), value)
                res = s.post(argv.data_url,
                             json={
                                 'data': {
                                     'value': value,
                                     'timestamp': datetime.now().isoformat(timespec='seconds')
                                 }
                             })
                res.raise_for_status()


if __name__ == '__main__':
    main()
