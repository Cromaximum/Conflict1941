# coding=utf-8
import math
import random
import time
import sys

def sleep_seconds(seconds):
    time.sleep(seconds)

def cool_text(text):
    for char in text:
        sleep_seconds(.1)
        sys.stdout.write(char)
        sys.stdout.flush()