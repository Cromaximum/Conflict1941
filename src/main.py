# coding=utf-8
import sys
import os
import random
from date import *
from DE_infantry import *
from util import *
from world import *

#TODO
#Loop nation selection if soviet selected and display error
#Loop Char creation screen and display non valid input error

#192.168.55.1


#Game Loop
clear()
main_menu = True
main_interface = True
char_selec = True


main_squad = create_new_squad_DE()
primary_date = date()

#Germany = True
#Soviet = False
nation = ''

main_char = create_new_Soldier_DE('Squad Leader')


ENDC = '\033[0m'
WARNING = '\033[93m'


def randomization_loop():
	global main_char
	main_char = create_new_Soldier_DE('Squad Leader')

def char_creation():
	global main_menu
	global main_interface
	global main_char
	global char_selec
	char_selec = True
	print("[1] German")
	print("[2] Soviet")
	ans = raw_input("Option: ")
	if(ans == '1'):
		clear()
		while(char_selec):
			clear()
			print(print_soldier(main_char))
			print("[1] Accept")
			print("[2] Re-Roll")
			ans = raw_input("Option: ")
			if(ans == '1'):
				char_selec = False
				main_interface = True
				main_menu = False
				clear()
			elif(ans == '2'):
				main_char = create_new_Soldier_DE('Squad Leader')
			else:
				warning_text("!!! Non-Valid Input [' + ans + ']")

	elif(ans == '2'):
		clear()
		warning_text("Soviet's Not Currently Supported")
	else:
		clear()
		print("Input not valid")
		
def main_interface_loop():
	global main_interface
	while(main_interface):
		clear()
		#sys.exit()
		print_date_c(primary_date)
		print('Squad Leader: ' + main_char.name)
		print("-----------")
		print("[1] Character Information...")
		print("[2] Squad Information...")
		print("[3] Wait...")
		print("[4] Quit...")
		print("-----------")
		print("")
		#iterate_by_hour(primary_date)
		ans = raw_input("Option: ")
		if(ans == '1'):
			clear()
			print_soldier(main_char)
			raw_input("Press Any Key to Continue... ")
		if(ans == '2'):
			clear()
			print('squad info')
		if(ans == '3'):
			pass
		if(ans == '4'):
			clear()
			sys.exit()
		else:
			warning_text("!!! Non-Valid Input [" + ans + ']')
			

while(main_menu):
	print("~~ Conflict 1941 ~~")
	print("[1] New Game")
	print("[2] Credits")
	print("[3] Exit Game")
	ans = raw_input("Option: ")
	if(ans == '3'):
		clear()
		sys.exit()
	elif(ans == '2'):
		clear()
		print("Author: Maxwell Rhinelander")
		print("Version x.X.x")
		raw_input("Press Any Key to Continue... ")
		clear()
	elif(ans == '1'):
		clear()
		while(char_selec):
			char_creation()
		while(main_interface):
			main_interface_loop()

	else:
		clear()
		warning_text("!!! Non-Valid Input [" + ans + ']')



