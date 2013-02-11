## MF DoS

A PoC script to exhaust all TN3270 connections to a mainframe

**Requirements**: Python, s3270 and the IP/Port of mainframe           

**Created by**: Soldier of Fortran (@mainframed767)                

**Use**: Given an IP and port this script will try to exhaust all available connections.

## Example

Non-SSL standard port:

./MFDoS.py -t 192.168.0.32

Non-SSL, non-startard port and enabling ASCII art mode

./MFDoS.py -t 10.10.10.53:2323 -s

SSL Enable non-standard port and verbose

./MFDoS.py -t L:172.16.0.34:9922 -v

## Arguments:

  -h, --help            show this help message and exit

  -t TARGET, --target TARGET target IP address/Hostname and port: TARGET[:PORT] default port is 23. Add L: for SSL enabled TN3270 hosts. E.G. L:192.168.0.1:3270

  -s, --scary           Scary Ironic ASCII to impress your boss

  -v, --verbose         Be verbose

