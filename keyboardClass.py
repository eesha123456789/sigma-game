

from array import *
import pygame #user interface
from pygame import mixer
pygame.init() #initializes all modules to get everything started
mixer.init() #for music

import keyClass

#constants

#keyboard variables
#between each letter in a row
KEY_X_SPACING = 10
#between each row
KEY_Y_SPACING = 10
KEY_HEIGHT = 60
KEY_WIDTH = 50

class Keyboard:
    def __init__(self):
        self.keys = {}

    def drawKeyboard(self):
        #distance from the left for the first letter
        kb_x_pos = 345
        #distance from the top of the screen fro the first row
        kb_y_pos = 430
        
        alphabet = "qwertyuiopasdfghjklzxcvbnm"
        for letter in alphabet:
            key = keyClass.Key(letter, (kb_x_pos,kb_y_pos))
            self.keys[letter] = key
            key.drawKey()
            kb_x_pos += KEY_WIDTH + KEY_X_SPACING

            if letter == "p":
                kb_y_pos += KEY_HEIGHT + KEY_Y_SPACING
                #x pos is good now
                kb_x_pos = 375

            if letter == "l":
                kb_y_pos += KEY_HEIGHT + KEY_Y_SPACING
                kb_x_pos = 435

    def updateKey(self, letter, keyColor):
        key = self.keys[letter]
        key.update(keyColor)

    def getKey(self, letter):
        return self.keys[letter]