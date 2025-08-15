from array import *
import tkinter
import pygame #user interface
import sys #allows us to exit

from pygame import mixer
from tkinter import *
from tkinter import ttk
import asyncio

#files booleans
import storeClass
import inventoryClass
import wordleClass
import leaderboardClass
import characterClass
import scrumRun

pygame.init() #initializes all modules to get everything started
mixer.init() #for music

boolFirebase=False
if boolFirebase==False:
    #firebase database
    import firebase_admin
    from firebase_admin import db,credentials

    #autheticate to firebase
    cred = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(cred,{"databaseURL":"https://seldrow-326de-default-rtdb.firebaseio.com/"})

    ref = db.reference("/")
    ref.get()
    
    boolFirebase=True

#constants
elevator = pygame.mixer.Sound("sounds/Elevator.wav")

#hex colors
TITLE_PINK = (255, 139, 191)

#make this bigger so we can have a menu on top of the screen
WIDTH, HEIGHT = 1285, 660
WORDLE_BG_SIZE = (300,390)
#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seldrow!")


#us!!
EESHA_PIC = pygame.image.load("image_folder/eesha.png")
EESHA_PIC = pygame.transform.scale(EESHA_PIC, (220,500))
EESHA_RECT = EESHA_PIC.get_rect(center = ((WIDTH * 4)//5, HEIGHT//2 + 50))

SOPHIA_PIC = pygame.image.load("image_folder/sophia.png")
SOPHIA_PIC = pygame.transform.scale(SOPHIA_PIC, (220,460))
SOPHIA_RECT = SOPHIA_PIC.get_rect(center = (WIDTH //5, HEIGHT//2 + 70))

#database images (including coin tracker)
COIN_TRACKER = pygame.image.load("image_folder/coin.png")
COIN_TRACKER = pygame.transform.scale(COIN_TRACKER, (180, 60))
COIN_TRACKER_RECT = COIN_TRACKER.get_rect(center = (WIDTH-100, HEIGHT-50))


# 2nd parameter is the font size
DISPLAY_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 30)
SMALL_DISPLAY_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 18)
TITLE_FONT = pygame.font.Font("fonts/Aloevera-OVoWO.ttf", 100)
LOGIN_FONT = pygame.font.Font("fonts/Aloevera-OVoWO.ttf", 30)
wordle_start = False 

#for login
username = ""
new_name = ""
state = ""

#database global variables
name = ""
coins = 0


#Character Picking variables
character_picked=""

#Side Bar
clicked_sidebar = False
SIDEBAR_BOX_COLOR = pygame.Color('lightskyblue3')

MENU_TAB_RECT = pygame.Rect(10,(HEIGHT/2)-250,200,40)
TUTORIAL_TAB_RECT = pygame.Rect(10,(HEIGHT/2)-200,200,40)
LEADERBOARD_TAB_RECT = pygame.Rect(10,(HEIGHT/2)-150,200,40)
STORE_TAB_RECT = pygame.Rect(10,(HEIGHT/2)-100,200,40)
INVENTORY_TAB_RECT = pygame.Rect(10,(HEIGHT/2)-50,200,40)
WORDLE_TAB_RECT= pygame.Rect(10,(HEIGHT/2),200,40)
SCRUMRUN_TAB_RECT = pygame.Rect(10,(HEIGHT/2)+50,200,40)
LOGOUT_TAB_RECT = pygame.Rect(10,(HEIGHT/2)+100,200,40)

DROPDOWN_IMAGE = pygame.image.load("image_folder/dropdown.png")
DROPDOWN_IMAGE = pygame.transform.scale(DROPDOWN_IMAGE, (50,50))
DROPDOWN_RECT = DROPDOWN_IMAGE.get_rect(center = (50, (HEIGHT/2) -300))


    
def login():
    global state, name, coins, username, new_name
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color("gray15")
    color1 = color_passive
    color2 = color_passive
    active1 = False
    active2 = False
    username=""
    
    while state=="login":
        NAME_RECT = pygame.Rect((WIDTH/2)-100,300,200,40)
        NEW_NAME_RECT = pygame.Rect((WIDTH/2)-100,500,200,40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if  event.type == pygame.MOUSEBUTTONDOWN:
                if NAME_RECT.collidepoint(event.pos):
                    active1 = True
                    active2 = False
                    new_name=""
                elif NEW_NAME_RECT.collidepoint(event.pos):
                    active2 = True
                    active1 = False
                    username=""
                else:
                    active1 = False
                    active2 = False
                    
            if(event.type == pygame.KEYDOWN):
                if event.key == pygame.K_RETURN:                  
                    if active1 and username!="":
                        name = username
                        #name_exists = 
                        if db.reference("/Players/" + name).get() is None:
                            noUsernamePopup = tkinter.Tk()
                            placement = ttk.Frame(noUsernamePopup, padding=75)
                            placement.grid()
                            ttk.Label(placement, background= "pink", font="Times", text="This username doesn't exist").grid(column=0, row=0)
                            ttk.Button(placement, text="Ok", padding=10, command=noUsernamePopup.destroy).grid(column=0, row=2)
                            noUsernamePopup.mainloop()
                        elif db.reference("/Players/" + name+"/"+"Character").get() is None:
                            state="character"
                            characterClass.pick_character()
                        else:
                            state ="menu"
                            menu()
                    elif active2 and new_name!="":
                        name = new_name
                        name_exists = db.reference("/Players/" + name).get()
                        if name_exists is not None:
                            alreadyExistsPopup = tkinter.Tk()
                            placement = ttk.Frame(alreadyExistsPopup, padding=75)
                            placement.grid()
                            ttk.Label(placement, background= "pink", font="Times", text="This username already exists").grid(column=0, row=0)
                            ttk.Button(placement, text="Ok", padding=10, command=alreadyExistsPopup.destroy).grid(column=0, row=2)
                            alreadyExistsPopup.mainloop()
                        elif db.reference("/Players/" + name+"/"+"Character").get() is None:
                            state ="character"
                            db.reference("/Players/").update({new_name: {"Coins":0}})
                            characterClass.pick_character()
                        
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif active2:
                    if(event.type == pygame.KEYDOWN):
                        if event.key == pygame.K_BACKSPACE:
                            new_name = new_name[:-1]
                        else:
                            new_name += event.unicode
            
        SCREEN.fill("white")
        if active1:
            color1 = color_active
        elif active2:
            color2 = color_active
        else:
            color1 = color_passive
            color2 = color_passive
        pygame.draw.rect(SCREEN, color1, NAME_RECT, 2)
        NAME_TEXT = DISPLAY_FONT.render(username, True,"black")
        SCREEN.blit(NAME_TEXT,NAME_RECT)
        NAME_RECT.w = max(100,NAME_TEXT.get_width()+10)
        
        pygame.draw.rect(SCREEN, color2, NEW_NAME_RECT, 2)
        NEW_NAME_TEXT = DISPLAY_FONT.render(new_name, True,"black")
        SCREEN.blit(NEW_NAME_TEXT,NEW_NAME_RECT)
        NEW_NAME_RECT.w = max(100,NEW_NAME_TEXT.get_width()+10)
        
        TITLE_TEXT = TITLE_FONT.render("""seldrow""", True, "pink", None)
        TITLE_TEXT_RECT = TITLE_TEXT.get_rect()
        TITLE_TEXT_RECT.center = (WIDTH // 2, HEIGHT - 550)
        SCREEN.blit(TITLE_TEXT, TITLE_TEXT_RECT)

        #idk if we should uselogin font here or display font
        LOGIN_TEXT = LOGIN_FONT.render("""Login""", True, "black", "white")
        LOGIN_TEXT_RECT = LOGIN_TEXT.get_rect()
        LOGIN_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2 - 100)
        SCREEN.blit(LOGIN_TEXT,LOGIN_TEXT_RECT)
        
        LOGIN_TEXT_2 = SMALL_DISPLAY_FONT.render("""enter your username""", True, "black", "white")
        LOGIN_TEXT_2_RECT = LOGIN_TEXT_2.get_rect()
        LOGIN_TEXT_2_RECT.center = (WIDTH // 2, HEIGHT // 2 - 65)
        SCREEN.blit(LOGIN_TEXT_2,LOGIN_TEXT_2_RECT)
        
        SIGNUP_TEXT = LOGIN_FONT.render("""Sign Up""", True, "black", "white")
        SIGNUP_TEXT_RECT = SIGNUP_TEXT.get_rect()
        SIGNUP_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2 + 100)
        SCREEN.blit(SIGNUP_TEXT,SIGNUP_TEXT_RECT)

        SIGNUP_TEXT_2 = SMALL_DISPLAY_FONT.render("""create new username""", True, "black", "white")
        SIGNUP_TEXT_2_RECT = SIGNUP_TEXT_2.get_rect()
        SIGNUP_TEXT_2_RECT.center = (WIDTH // 2, HEIGHT // 2 + 125)
        SCREEN.blit(SIGNUP_TEXT_2,SIGNUP_TEXT_2_RECT)

        SIGNUP_TEXT_3 = SMALL_DISPLAY_FONT.render("""(case sensitive)""", True, "black", "white")
        SIGNUP_TEXT_3_RECT = SIGNUP_TEXT_3.get_rect()
        SIGNUP_TEXT_3_RECT.center = (WIDTH // 2, HEIGHT // 2 + 150)
        SCREEN.blit(SIGNUP_TEXT_3,SIGNUP_TEXT_3_RECT)

        SCREEN.blit(EESHA_PIC, EESHA_RECT)
        SCREEN.blit(SOPHIA_PIC, SOPHIA_RECT)
        
        pygame.display.update()

def show_coins():
    SCREEN.blit(COIN_TRACKER, COIN_TRACKER_RECT)
    COINS_TEXT = LOGIN_FONT.render(str(db.reference("/Players/" + name + "/Coins").get()), True, "black", None)
    COINS_TEXT_RECT = COINS_TEXT.get_rect()
    COINS_TEXT_RECT.center = (WIDTH-75, HEIGHT-45)
    SCREEN.blit(COINS_TEXT,COINS_TEXT_RECT)  
    
def menu():
    global state
    SCREEN.fill("white")
    MENU_TEXT = TITLE_FONT.render("""MAIN MENU""", True, "black", "white")
    MENU_TEXT_RECT1 = MENU_TEXT.get_rect()
    MENU_TEXT_RECT1.center = (WIDTH // 2, HEIGHT // 2-200)
    SCREEN.blit(MENU_TEXT,MENU_TEXT_RECT1)
    MENU_TEXT2 = DISPLAY_FONT.render("""Press 1 for Tutorial""", True, "black", "white")
    MENU_TEXT_RECT2 = MENU_TEXT2.get_rect()
    MENU_TEXT_RECT2.center = (WIDTH // 2, HEIGHT // 2-150)
    SCREEN.blit(MENU_TEXT2,MENU_TEXT_RECT2)
    MENU_TEXT3 = DISPLAY_FONT.render("""Press 2 for Leaderboard""", True, "black", "white")
    MENU_TEXT_RECT3 = MENU_TEXT3.get_rect()
    MENU_TEXT_RECT3.center = (WIDTH // 2, HEIGHT // 2-100)
    SCREEN.blit(MENU_TEXT3,MENU_TEXT_RECT3)
    MENU_TEXT4 = DISPLAY_FONT.render("""Press 3 for Shop""", True, "black", "white")
    MENU_TEXT_RECT4 = MENU_TEXT4.get_rect()
    MENU_TEXT_RECT4.center = (WIDTH // 2, HEIGHT // 2-50)
    SCREEN.blit(MENU_TEXT4,MENU_TEXT_RECT4)
    MENU_TEXT5 = DISPLAY_FONT.render("""Press 4 for Inventory""", True, "black", "white")
    MENU_TEXT_RECT5 = MENU_TEXT5.get_rect()
    MENU_TEXT_RECT5.center = (WIDTH // 2, HEIGHT // 2)
    SCREEN.blit(MENU_TEXT5,MENU_TEXT_RECT5)
    MENU_TEXT6 = DISPLAY_FONT.render("""Press 5 for Seldrow""", True, "black", "white")
    MENU_TEXT_RECT6 = MENU_TEXT6.get_rect()
    MENU_TEXT_RECT6.center = (WIDTH // 2, HEIGHT // 2+50)
    SCREEN.blit(MENU_TEXT6,MENU_TEXT_RECT6)
    MENU_TEXT7 = DISPLAY_FONT.render("""Press 6 for Scrum Run""", True, "black", "white")
    MENU_TEXT_RECT7 = MENU_TEXT7.get_rect()
    MENU_TEXT_RECT7.center = (WIDTH // 2, HEIGHT // 2+100)
    SCREEN.blit(MENU_TEXT7,MENU_TEXT_RECT7)
    MENU_TEXT8 = DISPLAY_FONT.render("""Press 7 for Logout""", True, "black", "white")
    MENU_TEXT_RECT8 = MENU_TEXT8.get_rect()
    MENU_TEXT_RECT8.center = (WIDTH // 2, HEIGHT // 2+150)
    SCREEN.blit(MENU_TEXT8,MENU_TEXT_RECT8)
    characterClass.show_character()
    pygame.display.update()
    while state=="menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    state="tutorial"
                    tutorial()
                elif event.key == pygame.K_2:
                    
                    state="leaderboard"
                    leaderboardClass.leaderboard()
                elif event.key == pygame.K_3:
                    
                    state="store"
                    storeClass.store()
                elif event.key == pygame.K_4:
                    
                    state="inventory"
                    inventoryClass.inventory()
                elif event.key == pygame.K_5:
                    state="wordle"
                    wordleClass.wordle()
                elif event.key == pygame.K_6:
                    
                    state="scrumrun"
                    scrumRun.run()
                elif event.key == pygame.K_7:
                    logout()

def sidebar_function():
    global state, clicked_sidebar
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if DROPDOWN_RECT.collidepoint(event.pos):
                clicked_sidebar=True
        if clicked_sidebar == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if state=="wordle":
                    elevator.stop()
                    
                if MENU_TAB_RECT.collidepoint(event.pos):
                    state="menu"
                    clicked_sidebar=False
                    wordleClass.reset()
                    menu()
                    
                elif TUTORIAL_TAB_RECT.collidepoint(event.pos):
                    state="tutorial"
                    clicked_sidebar=False
                    wordleClass.reset()
                    tutorial()
                    
                elif LEADERBOARD_TAB_RECT.collidepoint(event.pos):
                    
                    state="leaderboard"
                    clicked_sidebar=False
                    wordleClass.reset()
                    leaderboardClass.leaderboard()
                    
                elif STORE_TAB_RECT.collidepoint(event.pos):
                    
                    state="store"
                    clicked_sidebar=False
                    wordleClass.reset()
                    storeClass.store()
                    
                elif INVENTORY_TAB_RECT.collidepoint(event.pos):
                    
                    state="inventory"
                    clicked_sidebar=False
                    wordleClass.reset()
                    inventoryClass.inventory()
                    
                elif WORDLE_TAB_RECT.collidepoint(event.pos):
                    state="wordle"
                    clicked_sidebar=False
                    wordleClass.reset()
                    wordleClass.wordle()
                elif SCRUMRUN_TAB_RECT.collidepoint(event.pos):
                    state="scrumrun"
                    clicked_sidebar=False
                    wordleClass.reset()
                    scrumRun.run()
                    
                elif LOGOUT_TAB_RECT.collidepoint(event.pos):
                    state="logout"
                    clicked_sidebar=False
                    wordleClass.reset()
                    logout()
                        
            pygame.draw.rect(SCREEN, SIDEBAR_BOX_COLOR, MENU_TAB_RECT, 2)
            MENU_TEXT = DISPLAY_FONT.render("Menu", True,"black")
            SCREEN.blit(MENU_TEXT, MENU_TAB_RECT)
                
            pygame.draw.rect(SCREEN, SIDEBAR_BOX_COLOR, TUTORIAL_TAB_RECT, 2)
            TUTORIAL_TEXT = DISPLAY_FONT.render("Tutorial", True,"black")
            SCREEN.blit(TUTORIAL_TEXT, TUTORIAL_TAB_RECT)
            
            pygame.draw.rect(SCREEN, SIDEBAR_BOX_COLOR, LEADERBOARD_TAB_RECT, 2)
            LEADERBOARD_TEXT = DISPLAY_FONT.render("Leaderboard", True,"black")
            SCREEN.blit(LEADERBOARD_TEXT, LEADERBOARD_TAB_RECT)
            
            pygame.draw.rect(SCREEN, SIDEBAR_BOX_COLOR, STORE_TAB_RECT, 2)
            STORE_TEXT = DISPLAY_FONT.render("Store", True,"black")
            SCREEN.blit(STORE_TEXT, STORE_TAB_RECT)
            
            pygame.draw.rect(SCREEN, SIDEBAR_BOX_COLOR, INVENTORY_TAB_RECT, 2)
            INVENTORY_TEXT = DISPLAY_FONT.render("Inventory", True,"black")
            SCREEN.blit(INVENTORY_TEXT, INVENTORY_TAB_RECT)
            
            pygame.draw.rect(SCREEN, SIDEBAR_BOX_COLOR, WORDLE_TAB_RECT, 2)
            WORDLE_TEXT = DISPLAY_FONT.render("Seldrow", True,"black")
            SCREEN.blit(WORDLE_TEXT, WORDLE_TAB_RECT)
            
            pygame.draw.rect(SCREEN, SIDEBAR_BOX_COLOR, SCRUMRUN_TAB_RECT, 2)
            SCRUMRUN_TEXT = DISPLAY_FONT.render("Scrum Run", True,"black")
            SCREEN.blit(SCRUMRUN_TEXT, SCRUMRUN_TAB_RECT)
            
            pygame.draw.rect(SCREEN, SIDEBAR_BOX_COLOR, LOGOUT_TAB_RECT, 2)
            LOGOUT_TEXT = DISPLAY_FONT.render("Logout", True,"black")
            SCREEN.blit(LOGOUT_TEXT, LOGOUT_TAB_RECT)

            pygame.display.update()
        #need to find a way to cover it up better
        if (event.type == pygame.MOUSEBUTTONDOWN) & (clicked_sidebar == True): 
            if not DROPDOWN_RECT.collidepoint(event.pos):
                if not MENU_TAB_RECT.collidepoint(event.pos):
                    if not TUTORIAL_TAB_RECT.collidepoint(event.pos):
                        if not LEADERBOARD_TAB_RECT.collidepoint(event.pos):
                            if not STORE_TAB_RECT.collidepoint(event.pos):
                                if not INVENTORY_TAB_RECT.collidepoint(event.pos):
                                    if not WORDLE_TAB_RECT.collidepoint(event.pos):
                                        if not SCRUMRUN_TAB_RECT.collidepoint(event.pos):
                                            if not LOGOUT_TAB_RECT.collidepoint(event.pos):
                                                clicked_sidebar=False
                                                WHITE_BOX_RECT=pygame.Rect(10,(HEIGHT/2)-250,200, 350)
                                                pygame.draw.rect(SCREEN, "white", WHITE_BOX_RECT)
                                                pygame.display.update()

def sidebar_display():
    global state, wordle_start, clicked_sidebar 
    DROPDOWN_IMAGE = pygame.image.load("image_folder/dropdown.png")
    DROPDOWN_IMAGE = pygame.transform.scale(DROPDOWN_IMAGE, (50,50))
    DROPDOWN_RECT = DROPDOWN_IMAGE.get_rect(center = (50, (HEIGHT/2) -300))
    SCREEN.blit(DROPDOWN_IMAGE, DROPDOWN_RECT)
    pygame.display.update()
    
#parameters are the name of the file               
def tutorial():
    global state
    SCREEN.fill("white")
    TUTORIAL_TEXT = TITLE_FONT.render("""TUTORIAL""", True, TITLE_PINK, "white")
    TUTORIAL_RECT = TUTORIAL_TEXT.get_rect()
    TUTORIAL_RECT.center = (WIDTH // 2, HEIGHT // 2-200)
    SCREEN.blit(TUTORIAL_TEXT,TUTORIAL_RECT)
    
    message = pygame.image.load("image_folder/tutorial.png").convert()
    message.set_colorkey(message.get_at((0,0)))
    message = pygame.transform.scale(message, (1000, 500))
    message_rect = message.get_rect(center = ((WIDTH/2)-100, HEIGHT/2 +50))
    SCREEN.blit(message, message_rect)
    
    characterClass.show_character()
    sidebar_display()
    pygame.display.update()
    while state=="tutorial":
        sidebar_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
               
def logout():
    global state, coins, name, username, new_name, character_picked, wordle_start
    state="login"
    name=""
    coins=0
    username=""
    new_name=""
    character_picked = ""
    #new
    wordle_start = False
    login()
    
    
state="login"
login()
async def main():
    global coins, name
    while True:
        coins = db.reference("/Players/" + name + "/Coins").get()
        if coins is None:
            coins = 0
        #print(coins)
        
        await asyncio.sleep(0)

asyncio.run(main())   