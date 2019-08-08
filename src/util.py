# coding=utf-8
import math
import random
import time
import sys
import os

ENDC = '\033[0m'
WARNING = '\033[93m'

def sleep_seconds(seconds):
    time.sleep(seconds)

def cool_text(text):
    for char in text:
        sleep_seconds(.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def warning_text(string):
	print((WARNING + string.upper() + ENDC))
