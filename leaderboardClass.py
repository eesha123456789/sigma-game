from array import *
import pygame #user interface
import sys #allows us to exit

import main

state=""

#make this bigger so we can have a menu on top of the screen
WIDTH, HEIGHT = 1285, 660
WORDLE_BG_SIZE = (300,390)
#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

CUTE_BG = pygame.image.load("bg_folder/leaderboard_bg.jpg")
CUTE_BG = pygame.transform.scale(CUTE_BG, (WIDTH+100, HEIGHT+100))
CUTE_RECT = CUTE_BG.get_rect(center = ((WIDTH/4)+300,(HEIGHT/4)+125))

LEADERBOARD = pygame.image.load("image_folder/leaderboard.png")
LEADERBOARD = pygame.transform.scale(LEADERBOARD, (500, 600))
LEADERBOARD_RECT = LEADERBOARD.get_rect(center = (WIDTH//2, HEIGHT//2 - 20))



DISPLAY_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 30)

def leaderboard():
    global state
    state="leaderboard"
    main.SCREEN.blit(CUTE_BG, CUTE_RECT)
    main.SCREEN.blit(LEADERBOARD, LEADERBOARD_RECT)
    main.sidebar_display()
    
    coins_ref = main.db.reference("Players")
    #snapshot is in order from smallest to largest for the five richest players
    snapshot = coins_ref.order_by_child("Coins").limit_to_last(5).get()
    
    #where the last player starts on the screen
    #for when the number of total players < 5
    start_height = 50
    for key in snapshot:
        start_height += 100

    delta_height = 0
    for key in snapshot:
        print(key)
        PLAYER_NAME = DISPLAY_FONT.render(key, True, "black", None)
        NAME_RECT = PLAYER_NAME.get_rect()
        NAME_RECT.center = (WIDTH // 2 - 70, start_height + delta_height)
        SCREEN.blit(PLAYER_NAME,NAME_RECT)

        PLAYER_COINS = DISPLAY_FONT.render(str(main.db.reference("/Players/" + key + "/Coins").get()), True, "black", None)
        COINS_RECT = PLAYER_COINS.get_rect()
        COINS_RECT.center = (WIDTH // 2 + 150, start_height + delta_height)
        SCREEN.blit(PLAYER_COINS,COINS_RECT)

        #minus since snapshot goes from smallest to largest not largest to smallest
        delta_height -= 100
    pygame.display.update()
    while state=="leaderboard":
        main.sidebar_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()