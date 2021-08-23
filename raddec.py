#To-do: Get timestamp code working properly. It currently causes crashes with Pareto Anywhere.
import sys
import json
import socket
radflag="100"
#timeflag="f00"
packflag="f10"
numrec="01"
numpack="1"
length="000"
checkstring="00"
IP_ADDRESS="[INSERT IP ADDRESS]"
try:
   for line in iter(sys.stdin.readline, b''):
      dict=json.loads(line)
      rssi=str('{:x}'.format(dict['rssi']+127))
      beaconid=dict['transmitterId']
      beacontype=str('{:02x}'.format(dict['transmitterIdType']))
      beacon=beacontype+beaconid
      numdec=str('{:02x}'.format(dict['numberofDecodings']))
      rectype=str('{:02x}'.format(dict['receiverIdType']))
      recid=dict['receiverId']
      rec=numrec+rssi+numdec+rectype+recid
      #timestamp=str('{:011x}'.format(dict['timestamp']))
      packet=dict['packets']
      packlength=str('{:02x}'.format(int(len(packet)/2)))
      base=radflag+length+beacon+rec
      #time=timeflag+timestamp
      data=packflag+numpack+packlength+packet
      lengthint=int((len(base+data+checkstring))/2)
      length=str('{:03x}'.format(lengthint))
      newbase=radflag+length+beacon+rec
      #timebase=newbase+time
      database=newbase+data
      #fullbase=newbase+time+data
      index=0
      checksum=0
      while index < int(lengthint - 1):
            checksum +=int(database[index*2:index*2+2],16)
            index+=1
      checkstring=str('{:02x}'.format(checksum%256))
      raddec=database+checkstring
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      sock.sendto(bytes.fromhex(raddec), (IP_ADDRESS, 50001))
      print(raddec)
except KeyboardInterrupt:
   sys.stdout.flush()
   pass
print("\nGoodbye")

