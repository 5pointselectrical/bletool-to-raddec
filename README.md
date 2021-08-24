# What is this?
This is a set of scripts designed to convert output from [GL-iNet's BleTool](https://github.com/gl-inet/bletool) into [encoded raddecs](https://github.com/reelyactive/raddec) that are compatible with [Pareto Anywhere](https://github.com/reelyactive/pareto-anywhere). They are designed specifically to pick up advertising packets from [Minew's](https://www.minew.com/) beacons.

# How does it work?
runme.sh is a launcher. Its purpose is to make sure BleTool is on and in discovery mode, then run the other two scripts. The output from ble_json.sh gets piped into raddec.py

ble_json.sh sets BleTool to listen mode, filters out all mac addresses that aren't Minew's beacons, then modifies the output into compact JSONs containing everything Pareto Anywhere needs. Note that the resulting JSONs are simplified from the format for decoded raddecs. To pick up all BLE advertising data, remove the grep command.

raddec.py is the Python 3 component. It takes the JSON produced by ble_json.sh, encodes it into the encoded raddec format, then sends it over to a remote Pareto Anywhere server, as well as printing out the resulting strings. The hardware this is designed to run on is unlikely to support a local instance of Pareto Anywhere.

# Hardware
This was programmed for the Spitz v2, but anything that supports GL.iNet's BleTool should work. An SD card is highly recommended if your router supports it. 

# Dependencies
* awk
* jq
* Python 3

Python 3 must be CPython. MicroPython does not work. I used the full Python3 installation on OpenWrt, but either the base or the light installation would likely work.

# Instructions
0. The scripts are intended to be run straight on your OpenWrt-supporting router.
1. Make sure port 50001 is open on your Pareto Anywhere server.
2. Replace "aabbccddeeff" in ble_json.sh with the MAC address of your own router. Make sure it's all lowercase, with no :
3. Modify raddec.py to set the IP address of your server.
4. Execute runme.sh
