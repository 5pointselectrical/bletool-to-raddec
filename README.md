# What is this?
This is a pair of scripts designed to convert output from [GL-iNet's BleTool](https://github.com/gl-inet/bletool) into [encoded raddecs](https://github.com/reelyactive/raddec) that are compatible with [Pareto Anywhere](https://github.com/reelyactive/pareto-anywhere). They are designed specifically to pick up advertising packets from [Minew's](https://www.minew.com/) beacons.

# How does it work?
runme.sh is a launcher. Its purpose is to make sure BleTool is on and in discovery mode, set BleTool into listen mode, filter out all mac addresses that aren't Minew's beacons, and then run the main raddec.py script.

raddec.py is the Micropython script. It takes the JSON produced by BleTool, converts it into the encoded raddec format, then sends it over to a remote Pareto Anywhere server. The hardware this is designed to run on is unlikely to support a local instance of Pareto Anywhere.

# Hardware
This was programmed for the Spitz v2, but anything that supports GL.iNet's BleTool should work. 

# Dependencies
* gl-bletool
* MicroPython

MicroPython was selected over CPython for storage reasons. This script is easily converted to run on CPython, should you prefer that and have an SD card handy.

# Instructions
0. The scripts are intended to be run straight on your OpenWrt-supporting router.
1. Make sure port 50001 is open on your Pareto Anywhere server.
2. Replace "aabbccddeeff" in raddec.py with the MAC address of your own router. Make sure it's all lowercase, with no :
3. Modify raddec.py to set the IP address of your server.
4. Execute runme.sh
