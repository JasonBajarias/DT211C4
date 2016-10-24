#!/usr/bin/python3

#C13379416
#Jason Bajarias

import pwd, datetime, subprocess, os

#Runs script until user input exit
while True:

	#takes user input
	commands = input()
	
	#runs pwd command
	if commands == "pw":
		subprocess.call("pwd", shell = True)
	#runs ifconfig command
	elif commands == "ifc":
		subprocess.call("/sbin,ifconfig", shell = True)
	#runs datetime command
	elif commands == "dt":
		date = str(datetime.datetime.now()\
		.strftime("%Y-%m-%d %H:%M:%S"))\
		.replace("-","")
		date = date.replace(":","")
		date = date.replace(" ","")
		print(date)
	#exits from the script
	elif commands == "exit":
		break
	#error checks for unknown command
	else:
		print("Unkown Command")
 
