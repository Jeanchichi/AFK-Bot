#-*- coding: utf-8 -*-

import keyboard
import random
import time

        
letter = ['Z', 'Q', 'S', 'D', 'C', 'space']
def selectRandom(letter):
    return random.choice(letter)

time.sleep(10.0)
while True:
    time.sleep(1.0)
    keyboard.press_and_release(selectRandom(letter))
    