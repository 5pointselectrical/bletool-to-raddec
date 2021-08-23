#!/bin/sh
bletool enable
bletool discovery
./ble_json.sh|python3 raddec.py
