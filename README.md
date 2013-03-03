## MF DoS

A PoC script to exhaust all TN3270 connections to a mainframe

**Requirements**: Python and the IP/Port of mainframe           

**Created by**: Soldier of Fortran (@mainframed767)                

**Use**: Given an IP and port this script will try to exhaust all available connections.

## Example

Boring mode:

./MFDoS.py -t 192.168.0.32 -p 23

SuperScary(tm) movie mode

./MFDoS.py -t 10.10.10.53 -p 2323 -s


## Arguments:

  -h, --help            show this help message and exit

  -t TARGET, --target TARGET target IP address/Hostname

  -s, --scary           Scary Ironic ASCII to impress your boss

  -p PORT, --port PORT  target port
