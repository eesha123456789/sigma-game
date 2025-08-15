
from array import *
import pygame #user interface
from pygame import mixer
pygame.init() #initializes all modules to get everything started
mixer.init() #for music


#constants

#hex colors
GREY = "#787c7e"
LIGHT_GREY = "#cfcfcf"


#make this bigger so we can have a menu on top of the screen
WIDTH, HEIGHT = 1285, 660
#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


# 2nd parameter is the font size
KEYBOARD_FONT = pygame.font.Font("fonts/Square.ttf", 30)

# Global variables
words = []


#keyboard variables

#distance from the left for the first letter
kb_x_pos = 345
#distance from the top of the screen fro the first row
kb_y_pos = 430
#between each letter in a row
KEY_X_SPACING = 10
#between each row
KEY_Y_SPACING = 10
KEY_HEIGHT = 60
KEY_WIDTH = 50

class Key:
    def __init__(self, name, key_pos):
        self.name = name
        self.key_color = LIGHT_GREY
        self.letter_color = "black"
        self.key_pos = key_pos
        self.key_x = key_pos[0]
        self.key_y = key_pos[1]

        self.key_rect = (self.key_x, self.key_y, KEY_WIDTH, KEY_HEIGHT) #left, top, width, height 
        #might need more tuning to center the letters
        self.letter_pos = (self.key_x + 25, self.key_y + 30)

        self.surface = KEYBOARD_FONT .render(self.name, True, self.letter_color)
        self.letter_rect = self.surface.get_rect(center = self.letter_pos)
        
    def drawKey(self):
        pygame.draw.rect(SCREEN, self.key_color, self.key_rect)
        self.surface = KEYBOARD_FONT .render(self.name, True, self.letter_color)
        SCREEN.blit(self.surface, self.letter_rect)

        pygame.display.update()

    def update(self, bgColor):
        self.key_color = bgColor
        self.drawKey()

    def getColor(self):
        return self.key_color
