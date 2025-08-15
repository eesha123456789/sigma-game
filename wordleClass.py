from array import *
import tkinter
import pygame #user interface
import sys #allows us to exit
import random #for random answer in words

from pygame import mixer
from tkinter import *
from tkinter import ttk

import main
import wordleletter
import keyboardClass
import characterClass

keyboard = keyboardClass.Keyboard()


pygame.init() #initializes all modules to get everything started
mixer.init() #for music

#constants

state=""

#hex colors
GREEN = "#77DD77"
YELLOW = "#FFDF00"
GREY = "#787c7e"

#make this bigger so we can have a menu on top of the screen
WIDTH, HEIGHT = 1285, 660
WORDLE_BG_SIZE = (300,390)
#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


# Different Screens Images and Pictures
NATURE_BG = pygame.image.load("bg_folder/nature_bg.png") 
NATURE_BG = pygame.transform.scale(NATURE_BG, (600,400))
NATURE_RECT = NATURE_BG.get_rect(center=(WIDTH//2, HEIGHT//2-120)) 

FOOD_BG = pygame.image.load("bg_folder/food_bg.png") 
FOOD_BG = pygame.transform.scale(FOOD_BG, (600,400))
FOOD_RECT = FOOD_BG.get_rect(center=(WIDTH//2, HEIGHT//2-120)) 

CATS_BG = pygame.image.load("bg_folder/cats_bg.png") 
CATS_BG = pygame.transform.scale(CATS_BG, (600,400))
CATS_RECT = CATS_BG.get_rect(center=(WIDTH//2, HEIGHT//2-120)) 

BACKGROUND = pygame.image.load("bg_folder/blankwordle.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, WORDLE_BG_SIZE)
BACKGROUND_RECT = BACKGROUND.get_rect(center=(WIDTH//2, HEIGHT//2-120)) 

WORDLE_WIN = pygame.image.load("bg_folder/wordle_win.png") 
WORDLE_WIN_RECT = WORDLE_WIN.get_rect(center=(WIDTH//2, HEIGHT//2)) 
WORDLE_LOSS = pygame.image.load("bg_folder/wordle_loss.png") 
WORDLE_LOSS_RECT = WORDLE_LOSS.get_rect(center=(WIDTH//2, HEIGHT//2)) 


#sound effects
eating = pygame.mixer.Sound("sounds/Eating.wav")
congrats = pygame.mixer.Sound("sounds/Congrats.wav")
error = pygame.mixer.Sound("sounds/Error.wav")
meow = pygame.mixer.Sound("sounds/Meow.wav")
water = pygame.mixer.Sound("sounds/Water.wav")
womp = pygame.mixer.Sound("sounds/Womp.wav")
elevator = pygame.mixer.Sound("sounds/Elevator.wav")

#bg SOunds
natureBG_Sound= pygame.mixer.Sound("Sounds/LionKing.wav")
foodBG_Sound= pygame.mixer.Sound("sounds/PapaPizzaria.wav")        
animalsBG_Sound= pygame.mixer.Sound("sounds/Nyan_Cat.wav")
play_BG_Sounds=True

def soundCorrect(bg):
    if game_result == "":
        if bg == "nature":
            water.play()
        if bg == "food":
            eating.play()
        if bg == "animals":
            meow.play()
   
def backgroundSounds(bg):
    if bg == "nature":
        natureBG_Sound.set_volume(2)
        natureBG_Sound.play(-1)
    elif bg == "food":
        foodBG_Sound.play(-1)
    elif bg == "animals":
        animalsBG_Sound.set_volume(2)
        animalsBG_Sound.play(-1)



# 2nd parameter is the font size
LETTER_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 40)
DISPLAY_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 30)
RESULT_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 60)
wordle_start = False 

def initialWordle():
    BG_TEXT1 = DISPLAY_FONT.render("""Welcome to Seldrow! Pick a background.""", True, "black", "white")
    BG_TEXT_RECT1 = BG_TEXT1.get_rect()
    BG_TEXT_RECT1.center = (WIDTH // 2, HEIGHT // 2-100)
    SCREEN.blit(BG_TEXT1,BG_TEXT_RECT1)
    BG_TEXT2 = DISPLAY_FONT.render("""Press 1 to enter jumanji""", True, "black", "white")
    BG_TEXT_RECT2 = BG_TEXT2.get_rect()
    BG_TEXT_RECT2.center = (WIDTH // 2, HEIGHT // 2-50)
    SCREEN.blit(BG_TEXT2,BG_TEXT_RECT2)
    BG_TEXT3 = DISPLAY_FONT.render("""Press 2 if you're hungry""", True, "black", "white")
    BG_TEXT_RECT3 = BG_TEXT3.get_rect()
    BG_TEXT_RECT3.center = (WIDTH // 2, HEIGHT // 2)
    SCREEN.blit(BG_TEXT3,BG_TEXT_RECT3)
    BG_TEXT4 = DISPLAY_FONT.render("""Press 3 if you're a furry""", True, "black", "white")
    BG_TEXT_RECT4 = BG_TEXT4.get_rect()
    BG_TEXT_RECT4.center = (WIDTH // 2, HEIGHT // 2+50)
    SCREEN.blit(BG_TEXT4,BG_TEXT_RECT4)
    BG_TEXT5 = DISPLAY_FONT.render("""Press 4 if your BORRINGG (lameeee)""", True, "black", "white")
    BG_TEXT_RECT5 = BG_TEXT5.get_rect()
    BG_TEXT_RECT5.center = (WIDTH // 2, HEIGHT // 2+100)
    SCREEN.blit(BG_TEXT5,BG_TEXT_RECT5)

#distance from the left for the first letter
letter_x_pos = 500
#distance from the top of the screen fro the first row
letter_y_pos = 13
#between each letter in a row
LETTER_X_SPACING = 9
#between each row
LETTER_Y_SPACING = -11
LETTER_SIZE = 50

# Global variables
words = []
guesses_count = 0

#for login
username = ""
new_name = ""

#helps with preventing yellow square when the letter has alr been guessed correctly
used_letters = ""

# guesses variable stores all guesses, which are lists of letters..
guesses = [[]] * 6

current_guess = []
current_guess_string = ""
game_result = ""
curr_bg=""


def check_guess(guess, answer):
    # note: must use global keyword to change global variables in function
    global current_guess, guesses_count, current_guess_string, game_result, letter_x_pos, letter_y_pos, used_letters

    all_correct = True
    
    #helps with preventing yellow square when the letter has alr been guessed correctly
    used_letters = guess[0].text.lower() + guess[1].text.lower() + guess[2].text.lower() + guess[3].text.lower() + guess[4].text.lower()
    #iterate through each letter in the guess
    for i in range(5):
        cur_letter = guess[i].text.lower()
        #number of the same letter in a word
        num_letters = 0

        for letter in used_letters:
            if letter == cur_letter:
                num_letters += 1

        if cur_letter == answer[i]:
            guess[i].bg_color = GREEN
            guess[i].text_color = "white"
            #keyboard
            keyboard.updateKey(cur_letter, GREEN)
        
        # what should we do if there's two same letters in a word
        elif cur_letter in answer:
            used_num = 0
            for letter in used_letters:
                if letter == cur_letter:
                    used_num += 1
            if used_num <= num_letters:
                guess[i].bg_color = YELLOW
                guess[i].text_color = "white"
                all_correct = False
                #keyboard
                if keyboard.getKey(cur_letter).getColor() != GREEN:
                    keyboard.updateKey(cur_letter, YELLOW)
            else:
                guess[i].bg_color = GREY
                guess[i].text_color = "white"
                all_correct = False
                #keyboard
                if keyboard.getKey(cur_letter).getColor() != GREEN:
                    keyboard.updateKey(cur_letter, GREY)
                
        else: #letter not in answer
            guess[i].bg_color = GREY
            guess[i].text_color = "white"
            all_correct = False
            #keyboard
            if keyboard.getKey(cur_letter).getColor() != GREEN:
                    keyboard.updateKey(cur_letter, GREY)
        
        guess[i].draw()
        pygame.display.update()

    if all_correct == True:
        game_result = "W"
        end_display()
    elif all_correct == False and guesses_count >= 5:
        game_result = "L"
        end_display()

    guesses_count += 1
    letter_x_pos = 500
    letter_y_pos += (LETTER_Y_SPACING)
    current_guess = []
    current_guess_string = ""     

def add_new_letter():
    #adds new letter to the guess
    global letter_x_pos, current_guess_string, current_guess, guesses, letter_y_pos
    new_letter = wordleletter.WordleLetter(key_pressed, (letter_x_pos, guesses_count * 80 + letter_y_pos))
    letter_x_pos += (LETTER_X_SPACING + LETTER_SIZE)
    current_guess_string += key_pressed
    current_guess.append(new_letter)
    guesses_index = guesses_count - 1
    guesses[guesses_index].append(new_letter)

    for i in guesses:
        for j in i:
            j.draw()

def delete_letter():
    #deletes letter from guess
    global letter_x_pos, current_guess_string, current_guess, guesses
    current_guess_string = current_guess_string[:-1]
    #need to double check this
    guesses_index = guesses_count - 1
    del(guesses[guesses_index][len(current_guess) - 1])
    letter_x_pos -= (LETTER_X_SPACING + LETTER_SIZE)
    #just added
    current_guess[len(current_guess) - 1].bg_color = "white"
    current_guess[len(current_guess) - 1].text_color = "white"
    current_guess[len(current_guess) - 1].draw()
    
    pygame.display.update()
    current_guess.pop()

def reset():
    #resets variables after each game
    global guesses_count, current_answer, guesses, current_guess, current_guess_string, game_result, wordle_start, letter_y_pos, play_BG_Sounds, used_letters
    
    SCREEN.fill("white")
    main.sidebar_display()
    foodBG_Sound.stop()
    natureBG_Sound.stop()
    animalsBG_Sound.stop()
    initialWordle()
    if wordle_start == True:
        wordle_start = False
    pygame.display.update()
    
    letter_y_pos = 13
    guesses_count = 0
    current_answer = ""
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    play_BG_Sounds = True
    used_letters = ""
    
def end_display():
    global guesses_count, db_coins
    foodBG_Sound.stop()
    natureBG_Sound.stop()
    animalsBG_Sound.stop()
    if game_result == "W":
        #do this bc guesses_count is lower by the actual number for some reason
        num_guesses = guesses_count + 1
        db_coins = main.db.reference("/Players/" + main.name + "/Coins").get()
        if num_guesses == 1:
            main.coins = db_coins + 6
            main.db.reference("/Players/"+ main.name).update({"Coins": (main.coins)})
        if num_guesses == 2:
            main.coins = db_coins + 5
            main.db.reference("/Players/"+ main.name).update({"Coins": (main.coins)})
        if num_guesses == 3:
            main.coins = db_coins + 4
            main.db.reference("/Players/"+ main.name).update({"Coins": (main.coins)})
        if num_guesses == 4:
            main.coins = db_coins + 3
            main.db.reference("/Players/"+ main.name).update({"Coins": (main.coins)})
        if num_guesses == 5:
            main.coins = db_coins + 2
            main.db.reference("/Players/"+ main.name).update({"Coins": (main.coins)})
        if num_guesses == 6:
            main.coins = db_coins + 1
            main.db.reference("/Players/"+ main.name).update({"Coins": (main.coins)})
        
        SCREEN.blit(WORDLE_WIN, WORDLE_WIN_RECT)
        congrats.play()
    elif game_result == "L":
        SCREEN.blit(WORDLE_LOSS, WORDLE_LOSS_RECT)
        LOSS_TEXT = LETTER_FONT.render("""Welcome to Seldrow! Pick a background.)""", True, "black", "white")
        LOSS_TEXT_RECT = LOSS_TEXT.get_rect()
        LOSS_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2 + 40)
        answer_display = RESULT_FONT.render(current_answer, True, "black", "white")
        answer_display_rect = answer_display.get_rect()
        answer_display_rect.center = (WIDTH // 2, HEIGHT // 2-30)
        SCREEN.blit(answer_display, answer_display_rect)
        womp.play()
    pygame.display.update()


def wordle():
    global wordle_start, play_BG_Sounds, key_pressed, current_answer, guesses_count, state, character_picked
    state="wordle"
    SCREEN.fill("White")
    elevator.set_volume(0.4)
    elevator.play()
    main.sidebar_display()
    while state =="wordle":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if wordle_start == False:
                initialWordle()
                cur_bg = ""
                main.show_coins()      
                characterClass.show_character()

                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    cur_bg = "nature"
                    SCREEN.fill("white")
                    main.sidebar_display()
                    SCREEN.blit(NATURE_BG, NATURE_RECT)
                    main.show_coins()
                    characterClass.show_character()

                    keyboard.drawKeyboard()
                    with open("wordLists/nature.txt", "r") as natureWordsFile:
                        natureWords = natureWordsFile.read().splitlines()
                    current_answer = random.choice(natureWords)
                    wordle_start = True
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    cur_bg = "food"
                    SCREEN.fill("white")
                    main.sidebar_display()
                    SCREEN.blit(FOOD_BG, FOOD_RECT)
                    main.show_coins()
                    characterClass.show_character()

                    keyboard.drawKeyboard()
                    with open("wordLists/food.txt", "r") as foodWordsFile:
                        foodWords = foodWordsFile.read().splitlines()
                    current_answer = random.choice(foodWords)
                    wordle_start = True
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    cur_bg = "animals"
                    SCREEN.fill("white")
                    main.sidebar_display()
                    SCREEN.blit(CATS_BG, CATS_RECT)
                    main.show_coins()
                    characterClass.show_character()

                    keyboard.drawKeyboard()
                    with open("wordLists/animals.txt", "r") as animalWordsFile:
                        animalWords = animalWordsFile.read().splitlines()
                    current_answer = random.choice(animalWords)
                    wordle_start = True
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                    SCREEN.fill("white")
                    main.sidebar_display()
                    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
                    main.show_coins()
                    characterClass.show_character()

                    keyboard.drawKeyboard()
                    with open("wordLists/words.txt", "r") as allWordsFile:
                        allWords = allWordsFile.read().splitlines()
                    current_answer = random.choice(allWords)
                    wordle_start = True
                    
                pygame.display.update()
            if wordle_start == True:
                elevator.stop()
                if(play_BG_Sounds==True):
                    backgroundSounds(cur_bg)
                    play_BG_Sounds=False
                if game_result != "":
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        reset()
                if event.type == pygame.KEYDOWN:
                    #print(event.key)
                    if event.key == pygame.K_RETURN:
                        print(current_answer)
                        #if game is finished
                        if game_result != "":
                            end_display()
                        else:
                            if len(current_guess_string) == 5:
                                temp = False
                                with open("wordLists/words.txt",'r') as text_file:
                                    lines = text_file.read().splitlines()
                                for line in lines:
                                    if current_guess_string == line:
                                        check_guess(current_guess, current_answer)
                                        soundCorrect(cur_bg)
                                        temp = True
                                if temp == False:
                                    error.play()
                                    errorPopup = tkinter.Tk()
                                    placement = ttk.Frame(errorPopup, padding=75)
                                    placement.grid()
                                    ttk.Label(placement, background= "yellow", font="Times", text="Please enter a valid word.").grid(column=0, row=0)
                                    ttk.Button(placement, text="Ok", padding=10, command=errorPopup.destroy).grid(column=0, row=2)
                                    errorPopup.mainloop()           
                    
                    elif event.key == pygame.K_BACKSPACE:
                        if len(current_guess_string) > 0:
                            delete_letter()
                    else:
                        key_pressed = event.unicode.lower()
                        if key_pressed in "abcdefghijklmnopqrstuvwxyz" and key_pressed != "":
                            if len(current_guess_string) < 5:
                                add_new_letter()
        main.sidebar_function()
