#!/bin/sh
bletool listen|grep "ac:23:3f"|cut -c 26-|sed s/://g|awk '{ print strftime("{\"timestamp\": %s,"),"\"receiverId\":", "\"9483c40b81d1\",", $0; fflush(); }'|sed s/\"mac\"/\"transmitterId\":/g| sed s/' "address_type" 0,'//g|sed s/' "bonding" 255,'//g|sed s/' "packet_type" 3,'//g|sed s/\"rssi\"/\"rssi\":/g|sed s/' "packet_type" 0,'//g|sed s/\"data\"/\"packets\":/g|"jq" -c -a "{transmitterId: .transmitterId, transmitterIdType: 2, receiverId: .receiverId, receiverIdType: 2, rssi: .rssi, numberofDecodings: 1, packets: .packets, timestamp: .timestamp}"
