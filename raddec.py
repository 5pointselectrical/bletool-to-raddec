import sys
import ubinascii
import ujson
import usocket
import gc
radflag="100"
#timeflag="f00"
packflag="f10"
numrec="01"
numpack="1"
length="000"
checkstring="00"
IP_ADDRESS="127.0.0.1"
RECEIVER_MAC="aabbccddeeff"
def iter2(c, s):
    while True:
        v = c()
        if v == s:
            raise StopIteration
        yield v
try:
       for line in iter2(sys.stdin.readline, b''):
           dict=ujson.loads(line)
           beaconid=dict['mac'].replace(':','')
           beacontype=str('{:02x}'.format(2))
           beacon=beacontype+beaconid
           numdec=str('{:02x}'.format(1))
           rectype=str('{:02x}'.format(2))
           recid=RECEIVER_MAC
           rssi=str('{:x}'.format(dict['rssi']+127))
           rec=numrec+rssi+numdec+rectype+recid
           packet=dict['data']
           packlength=str('{:02x}'.format(int(len(packet)/2)))
           base=radflag+length+beacon+rec
           data=packflag+numpack+packlength+packet
           lengthint=int((len(base+data+checkstring))/2)
           length=str('{:03x}'.format(lengthint))
           newbase=radflag+length+beacon+rec
           database=newbase+data
           index=0
           checksum=0
           while index < int(lengthint - 1):
                 checksum +=int(database[index*2:index*2+2],16)
                 index+=1
           checkstring=str('{:02x}'.format(checksum%256))
           raddec=ubinascii.unhexlify(database+checkstring)
           sockaddr = usocket.getaddrinfo(IP_ADDRESS,50001)[0][-1]
           sock = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
           sock.sendto(raddec, sockaddr)
           print(raddec)
           sock.close()
           gc.collect()
except KeyboardInterrupt:
   print("/nGoodbye")
