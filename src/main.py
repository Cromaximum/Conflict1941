# coding=utf-8
import sys
import os
from DE_infantry import *
from util import *
from world import *

#TODO
#Loop nation selection if soviet selected and display error
#Loop Char creation screen and display non valid input error


#Game Loop
game = True

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
	global game
	global main_char
	clear()
	print("[1] German")
	print("[2] Soviet")
	ans = raw_input("Option: ")
	if(ans == '1'):
		while(game):
			clear()
			print(print_soldier(main_char))
			print("[1] Accept")
			print("[2] Re-Roll")
			ans = raw_input("Option: ")
			if(ans == '1'):
				game = False
				clear()
			elif(ans == '2'):
				main_char = create_new_Soldier_DE('Squad Leader')
			else:
				warning_text("Input not valid")

	elif(ans == '2'):
		pass
	else:
		clear()
		print("Input not valid")
		


while(game):
	print("~~ Conflict 1941 ~~")
	print("[1] New Game")
	print("[2] Credits")
	print("[3] Exit Game")
	ans = raw_input("Option: ")
	if(ans == '3'):
		sys.exit()
	elif(ans == '2'):
		clear()
		print("Author: Maxwell Rhinelander")
		print("Version x.x.x")
		raw_input("Press Any Key to Continue... ")
		clear()
	elif(ans == '1'):
		char_creation()
		clear()

	else:
		clear()
		warning_text("Non-Valid Input")

print("Prost!")
