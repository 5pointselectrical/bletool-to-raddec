#!/bin/sh
bletool enable
bletool discovery
bletool listen|grep "ac:23:3f"|micropython raddec.py
