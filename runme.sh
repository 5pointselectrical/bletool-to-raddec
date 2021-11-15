#!/bin/sh
MACADDR=$(cat /sys/class/net/eth0/address)
MACADDR=$(echo $MACADDR|sed s/://g)
bletool enable
bletool discovery
echo "Sending data to Pareto Anywhere"
bletool listen|grep "ac:23:3f"|micropython /root/raddec.py "$MACADDR" > /dev/null 2>&1
