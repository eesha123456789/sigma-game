from array import *
import pygame #user interface

#make this bigger so we can have a menu on top of the screen
WIDTH, HEIGHT = 1285, 660
WORDLE_BG_SIZE = (300,390)
#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init() #initializes all modules to get everything started

#distance from the left for the first letter
letter_x_pos = 500
#distance from the top of the screen fro the first row
letter_y_pos = 13
#between each letter in a row
LETTER_X_SPACING = 9
#between each row
LETTER_Y_SPACING = -11
LETTER_SIZE = 50

LETTER_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 40)

class WordleLetter:
    def __init__(self, text, bg_pos):
        self.text = text
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_pos = bg_pos
        self.bg_x = bg_pos[0]
        self.bg_y = bg_pos[1]
        self.bg_rect = (self.bg_x, self.bg_y, LETTER_SIZE, LETTER_SIZE) #left, top, width, height 
        #might need more tuning to center the letters
        self.text_pos = (self.bg_x + 25, self.bg_y + 25)

        self.surface = LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.surface.get_rect(center = self.text_pos)

    def draw(self):
        # Puts the letter on the screen at the desired positions.
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        self.surface = LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.surface, self.text_rect)

        
        pygame.display.update()
