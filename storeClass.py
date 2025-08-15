from array import *
import pygame #user interface
import sys #allows us to exit

import tkinter
from tkinter import *
from tkinter import ttk

import main

pygame.init() #initializes all modules to get everything started
state=""

#constants

#hex colors
TITLE_PINK = (255, 139, 191)
BG_PINK = (253, 233, 242)

#make this bigger so we can have a menu on top of the screen
WIDTH, HEIGHT = 1285, 660
WORDLE_BG_SIZE = (300,390)
#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seldrow!")


# 2nd parameter is the font size
SMALL_DISPLAY_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 18)
TITLE_FONT = pygame.font.Font("fonts/Aloevera-OVoWO.ttf", 100)
INVENTORY_BUTTON_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 60)

#shop images
SHOP = pygame.image.load("bg_folder/shop.png")
SHOP = pygame.transform.scale(SHOP, (1285, 660))
SHOP_RECT = SHOP.get_rect(center = (WIDTH//2, HEIGHT//2))

#shop buttons
CLOTHES = pygame.image.load("image_folder/buttons/clothes_button.png")
CLOTHES = pygame.transform.scale(CLOTHES, (200, 70))
CLOTHES_RECT = CLOTHES.get_rect(center = (110, HEIGHT//2-220))

HAIR = pygame.image.load("image_folder/buttons/hair_button.png")
HAIR = pygame.transform.scale(HAIR, (200, 110))
HAIR_RECT = HAIR.get_rect(center = (WIDTH//2 + 330, HEIGHT//2))

ACCESSO = pygame.image.load("image_folder/buttons/acc_button.png")
ACCESSO = pygame.transform.scale(ACCESSO, (300, 85))
ACCESSO_RECT = ACCESSO.get_rect(center = (WIDTH//2 -170, HEIGHT-60))

PETS = pygame.image.load("image_folder/buttons/pets_button.png")
PETS = pygame.transform.scale(PETS, (180, 90))
PETS_RECT = PETS.get_rect(center = (WIDTH-110, HEIGHT//2-235))


#prices
FIVE_TEXT = SMALL_DISPLAY_FONT.render("""5 C""", True, "black", "white")
FIVE_RECT = FIVE_TEXT.get_rect()

TEN_TEXT = SMALL_DISPLAY_FONT.render("""10 C""", True, "black", "white")
TEN_RECT = TEN_TEXT.get_rect()

FIFTEEN_TEXT = SMALL_DISPLAY_FONT.render("""15 C""", True, "black", "white")
FIFTEEN_RECT = FIFTEEN_TEXT.get_rect()

TWENTY_TEXT = SMALL_DISPLAY_FONT.render("""20 C""", True, "black", "white")
TWENTY_RECT = TWENTY_TEXT.get_rect()

TWENTYFIVE_TEXT = SMALL_DISPLAY_FONT.render("""25 C""", True, "black", "white")
TWENTYFIVE_RECT = TWENTYFIVE_TEXT.get_rect()

THIRTY_TEXT = SMALL_DISPLAY_FONT.render("""30 C""", True, "black", "white")
THIRTY_RECT = THIRTY_TEXT.get_rect()

FORTY_TEXT = SMALL_DISPLAY_FONT.render("""40 C""", True, "black", "white")
FORTY_RECT = FORTY_TEXT.get_rect()

FIFTY_TEXT = SMALL_DISPLAY_FONT.render("""50 C""", True, "black", "white")
FIFTY_RECT = FIFTY_TEXT.get_rect()

NINENINE_TEXT = SMALL_DISPLAY_FONT.render("""99 C""", True, "black", "white")
NINENINE_RECT = NINENINE_TEXT.get_rect()

#clothes
CLOTHES1 = pygame.image.load("image_folder/clothes/default_outfit.png").convert()
CLOTHES1.set_colorkey(CLOTHES1.get_at((0,0)))
CLOTHES1 = pygame.transform.scale(CLOTHES1, (200, 300))
CLOTHES1_RECT = CLOTHES1.get_rect(center = (100, 200))

CLOTHES2 = pygame.image.load("image_folder/clothes/barney.png").convert()
CLOTHES2.set_colorkey(CLOTHES2.get_at((0,0)))
CLOTHES2 = pygame.transform.scale(CLOTHES2, (200, 300))
CLOTHES2_RECT = CLOTHES2.get_rect(center = (250, 200))

CLOTHES3 = pygame.image.load("image_folder/clothes/greentan_outfit.png").convert()
CLOTHES3.set_colorkey(CLOTHES3.get_at((0,0)))
CLOTHES3 = pygame.transform.scale(CLOTHES3, (200, 300))
CLOTHES3_RECT = CLOTHES3.get_rect(center = (400, 200))

CLOTHES4 = pygame.image.load("image_folder/clothes/jeantop.png").convert()
CLOTHES4.set_colorkey(CLOTHES4.get_at((0,0)))
CLOTHES4 = pygame.transform.scale(CLOTHES4, (200, 300))
CLOTHES4_RECT = CLOTHES4.get_rect(center = (550, 200))

CLOTHES5 = pygame.image.load("image_folder/clothes/pink_dress.png").convert()
CLOTHES5.set_colorkey(CLOTHES5.get_at((0,0)))
CLOTHES5 = pygame.transform.scale(CLOTHES5, (200, 300))
CLOTHES5_RECT = CLOTHES5.get_rect(center = (700, 200))

CLOTHES6 = pygame.image.load("image_folder/clothes/redblue_outfit.png").convert()
CLOTHES6.set_colorkey(CLOTHES6.get_at((0,0)))
CLOTHES6 = pygame.transform.scale(CLOTHES6, (200, 300))
CLOTHES6_RECT = CLOTHES6.get_rect(center = (850, 200))

#hair
H1 = pygame.image.load("image_folder/hair/blackpony.png").convert()
H1.set_colorkey(H1.get_at((0,0)))
H1 = pygame.transform.scale(H1, (200, 300))
H1_RECT = H1.get_rect(center = (100, 250))

H2 = pygame.image.load("image_folder/hair/blackspiky.png").convert()
H2.set_colorkey(H2.get_at((0,0)))
H2 = pygame.transform.scale(H2, (200, 300))
H2_RECT = H2.get_rect(center = (250, 250))

H3 = pygame.image.load("image_folder/hair/blondcurly.png").convert()
H3.set_colorkey(H3.get_at((0,0)))
H3 = pygame.transform.scale(H3, (200, 300))
H3_RECT = H3.get_rect(center = (400, 250))

H4 = pygame.image.load("image_folder/hair/blondpony.png").convert()
H4.set_colorkey(H4.get_at((0,0)))
H4 = pygame.transform.scale(H4, (200, 300))
H4_RECT = H4.get_rect(center = (550, 250))

H5 = pygame.image.load("image_folder/hair/bluestring.png").convert()
H5.set_colorkey(H5.get_at((0,0)))
H5 = pygame.transform.scale(H5, (200, 300))
H5_RECT = H5.get_rect(center = (700, 250))

H6 = pygame.image.load("image_folder/hair/brownbob.png").convert()
H6.set_colorkey(H6.get_at((0,0)))
H6 = pygame.transform.scale(H6, (200, 300))
H6_RECT = H6.get_rect(center = (850, 250))

H7 = pygame.image.load("image_folder/hair/brownsplit.png").convert()
H7.set_colorkey(H7.get_at((0,0)))
H7 = pygame.transform.scale(H7, (200, 300))
H7_RECT = H7.get_rect(center = (100, 500))

H8 = pygame.image.load("image_folder/hair/farquaad.png").convert()
H8.set_colorkey(H8.get_at((0,0)))
H8 = pygame.transform.scale(H8, (200, 300))
H8_RECT = H8.get_rect(center = (250, 500))

#accessories
A1 = pygame.image.load("image_folder/accessories/green_550.png").convert()
A1.set_colorkey(A1.get_at((0,0)))
A1 = pygame.transform.scale(A1, (250, 375))
A1_RECT = A1.get_rect(center = (100, 50))

A2 = pygame.image.load("image_folder/accessories/white_550.png").convert()
A2.set_colorkey(A2.get_at((0,0)))
A2 = pygame.transform.scale(A2, (250, 375))
A2_RECT = A2.get_rect(center = (250, 50))

A3 = pygame.image.load("image_folder/accessories/pink_dunks.png").convert()
A3.set_colorkey(A3.get_at((0,0)))
A3 = pygame.transform.scale(A3, (250, 375))
A3_RECT = A3.get_rect(center = (400, 50))

A4 = pygame.image.load("image_folder/accessories/panda_dunks.png").convert()
A4.set_colorkey(A4.get_at((0,0)))
A4 = pygame.transform.scale(A4, (250, 375))
A4_RECT = A4.get_rect(center = (550, 50))

A5 = pygame.image.load("image_folder/accessories/bluebow.png").convert()
A5.set_colorkey(A5.get_at((0,0)))
A5 = pygame.transform.scale(A5, (200, 300))
A5_RECT = A5.get_rect(center = (700, 300))

A6 = pygame.image.load("image_folder/accessories/flowers.png").convert()
A6.set_colorkey(A6.get_at((0,0)))
A6 = pygame.transform.scale(A6, (200, 300))
A6_RECT = A6.get_rect(center = (850, 300))

A7 = pygame.image.load("image_folder/accessories/shrek.png").convert()
A7.set_colorkey(A7.get_at((0,0)))
A7 = pygame.transform.scale(A7, (200, 300))
A7_RECT = A7.get_rect(center = (100, 520))

A8 = pygame.image.load("image_folder/accessories/strawhat.png").convert()
A8.set_colorkey(A8.get_at((0,0)))
A8 = pygame.transform.scale(A8, (200, 300))
A8_RECT = A8.get_rect(center = (250, 520))

P1 = pygame.image.load("image_folder/pets/dog.png").convert()
P1.set_colorkey(P1.get_at((0,0)))
P1 = pygame.transform.scale(P1, (175, 175))
P1_RECT = P1.get_rect(center = (100, 250))

P2 = pygame.image.load("image_folder/pets/cat.png").convert()
P2.set_colorkey(P2.get_at((0,0)))
P2 = pygame.transform.scale(P2, (175, 175))
P2_RECT = P2.get_rect(center = (250, 250))

P3 = pygame.image.load("image_folder/pets/hamster.png").convert()
P3.set_colorkey(P3.get_at((0,0)))
P3 = pygame.transform.scale(P3, (175, 175))
P3_RECT = P3.get_rect(center = (400, 250))

P4 = pygame.image.load("image_folder/pets/walrus.png").convert()
P4.set_colorkey(P4.get_at((0,0)))
P4 = pygame.transform.scale(P4, (130, 100))
P4_RECT = P4.get_rect(center = (550, 250))

P5 = pygame.image.load("image_folder/pets/fish.png").convert()
P5.set_colorkey(P5.get_at((0,0)))
P5 = pygame.transform.scale(P5, (175, 175))
P5_RECT = A5.get_rect(center = (700, 290))

#inventory

INVENTORY_BOX_COLOR = TITLE_PINK
CLOTHES_STORAGE_RECT = pygame.Rect(210,HEIGHT//2-80,360,80)
ACCESSO_STORAGE_RECT = pygame.Rect(680,HEIGHT//2-80,360,80)
HAIR_STORAGE_RECT = pygame.Rect(210,HEIGHT//2+80,360,80)
PETS_STORAGE_RECT = pygame.Rect(680,HEIGHT//2+80,360,80)

def store():
    global state
    state="store"
    #BUTTONS
    SCREEN.blit(SHOP, SHOP_RECT)
    SCREEN.blit(CLOTHES, CLOTHES_RECT)
    SCREEN.blit(HAIR, HAIR_RECT)
    SCREEN.blit(PETS, PETS_RECT)
    SCREEN.blit(ACCESSO, ACCESSO_RECT)
    main.sidebar_display()
    pygame.display.update()
    while state =="store":
        main.sidebar_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CLOTHES_RECT.collidepoint(event.pos):
                    state="shop_clothes"
                    shop_clothes()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
               if HAIR_RECT.collidepoint(event.pos):
                   state="shop_hair"
                   shop_hair()
                   
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ACCESSO_RECT.collidepoint(event.pos):
                    state="shop_accessories"
                    shop_accessories()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
               if PETS_RECT.collidepoint(event.pos):
                   state="shop_pets"
                   shop_pets()

def not_enough_coins():
    notEnoughCoinsPopup = tkinter.Tk()
    placement = ttk.Frame(notEnoughCoinsPopup, padding=75)
    placement.grid()
    ttk.Label(placement, background= "pink", font="Times", text="Not enough coins to purchase this item").grid(column=0, row=0)
    ttk.Button(placement, text="Ok", padding=10, command=notEnoughCoinsPopup.destroy).grid(column=0, row=2)
    notEnoughCoinsPopup.mainloop() 
   
def already_purchased():
    alreadyPurchasedPopup = tkinter.Tk()
    placement = ttk.Frame(alreadyPurchasedPopup, padding=75)
    placement.grid()
    ttk.Label(placement, background= "pink", font="Times", text="You have already purchased this item. It is in your inventory.").grid(column=0, row=0)
    ttk.Button(placement, text="Ok", padding=10, command=alreadyPurchasedPopup.destroy).grid(column=0, row=2)
    alreadyPurchasedPopup.mainloop() 
    
def successfully_purchased():
    #update number of coins on the screen
    main.show_coins()
    pygame.display.update()
    successfullyPurchasedPopup = tkinter.Tk()
    placement = ttk.Frame(successfullyPurchasedPopup, padding=75)
    placement.grid()
    ttk.Label(placement, background= "pink", font="Times", text="This item has been added to your inventory.").grid(column=0, row=0)
    ttk.Button(placement, text="Ok", padding=10, command=successfullyPurchasedPopup.destroy).grid(column=0, row=2)
    successfullyPurchasedPopup.mainloop() 
            
def shop_clothes():
    global state
    SCREEN.fill("white")
    CLOTHES_TEXT = TITLE_FONT.render("""clothes""", True, "pink", "white")
    CLOTHES_TEXT_RECT = CLOTHES_TEXT.get_rect()
    CLOTHES_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2-250)
    SCREEN.blit(CLOTHES_TEXT,CLOTHES_TEXT_RECT)
    
    
    #add new clothes to store here
    SCREEN.blit(CLOTHES1, CLOTHES1_RECT)
    SCREEN.blit(CLOTHES2, CLOTHES2_RECT)
    SCREEN.blit(CLOTHES3, CLOTHES3_RECT)
    SCREEN.blit(CLOTHES4, CLOTHES4_RECT)
    SCREEN.blit(CLOTHES5, CLOTHES5_RECT)
    SCREEN.blit(CLOTHES6, CLOTHES6_RECT)
    
    #prices
    FIVE_RECT.center = (100, 350)
    SCREEN.blit(FIVE_TEXT, FIVE_RECT)
    
    NINENINE_RECT.center = (250, 350)
    SCREEN.blit(NINENINE_TEXT, NINENINE_RECT)
    
    FIFTEEN_RECT.center = (400, 350)
    SCREEN.blit(FIFTEEN_TEXT, FIFTEEN_RECT)
    
    TWENTYFIVE_RECT.center = (550, 350)
    SCREEN.blit(TWENTYFIVE_TEXT, TWENTYFIVE_RECT)
    
    TWENTY_RECT.center = (700, 350)
    SCREEN.blit(TWENTY_TEXT, TWENTY_RECT)
    
    FIFTY_RECT.center = (850, 350)
    SCREEN.blit(FIFTY_TEXT, FIFTY_RECT)
    
    main.show_coins()
    main.sidebar_display()
    pygame.display.update()
    
    db_coins = main.db.reference("/Players/" + main.name + "/Coins").get()
    print(main.name)
    print(db_coins)
    while state == "shop_clothes":
        main.sidebar_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                           
            if main.db.reference("/Players/" + main.name +"/"+"Clothes").get() is None:
                #add clothes here when u make more
                main.db.reference("/Players/" + main.name + "/" + "Clothes").update({"Clothes1": 0})
                main.db.reference("/Players/" + main.name + "/" + "Clothes").update({"Clothes2": 0})
                main.db.reference("/Players/" + main.name + "/" + "Clothes").update({"Clothes3": 0})
                main.db.reference("/Players/" + main.name + "/" + "Clothes").update({"Clothes4": 0})
                main.db.reference("/Players/" + main.name + "/" + "Clothes").update({"Clothes5": 0})
                main.db.reference("/Players/" + main.name + "/" + "Clothes").update({"Clothes6": 0})
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CLOTHES1_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Clothes/Clothes1").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 5:
                        not_enough_coins()
                           
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-5
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Clothes").update({"Clothes1": 1})
                        print("clothes 1 updated")
                        successfully_purchased()
                        
                if CLOTHES2_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Clothes/Clothes2").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 99:
                        not_enough_coins()
                        
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-99
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Clothes").update({"Clothes2": 1})
                        print("clothes 2 updated")
                        successfully_purchased()
                
                if CLOTHES3_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Clothes/Clothes3").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 15:
                        not_enough_coins()
                                      
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-15
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Clothes").update({"Clothes3": 1})
                        print("clothes 3 updated")
                        successfully_purchased()
                
                if CLOTHES4_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Clothes/Clothes4").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 25:
                        not_enough_coins()
                    
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-25
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Clothes").update({"Clothes4": 1})
                        print("clothes 4 updated")
                        successfully_purchased()
                
                if CLOTHES5_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name +"/"+"Clothes/Clothes5").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 20:
                        not_enough_coins()
                        
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-20
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Clothes").update({"Clothes5": 1})
                        print("clothes 5 updated")
                        successfully_purchased()
                        
                if CLOTHES6_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Clothes/Clothes6").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 50:
                        not_enough_coins()
                                            
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-50
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Clothes").update({"Clothes6": 1})
                        print("clothes 6 updated") 
                        successfully_purchased()                       
                    
def shop_accessories():
    global state
    SCREEN.fill("white")
    ACCESSO_TEXT = TITLE_FONT.render("""accessories""", True, "pink", "white")
    ACCESSO_TEXT_RECT = ACCESSO_TEXT.get_rect()
    ACCESSO_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2-250)
    SCREEN.blit(ACCESSO_TEXT,ACCESSO_TEXT_RECT)
    
    #add new accessories to store here
    SCREEN.blit(A1, A1_RECT)
    SCREEN.blit(A2, A2_RECT)
    SCREEN.blit(A3, A3_RECT)
    SCREEN.blit(A4, A4_RECT)
    SCREEN.blit(A5, A5_RECT)
    SCREEN.blit(A6, A6_RECT)
    SCREEN.blit(A7, A7_RECT)
    SCREEN.blit(A8, A8_RECT)
    
    #prices
    TWENTYFIVE_RECT.center = (100, 350)
    SCREEN.blit(TWENTYFIVE_TEXT, TWENTYFIVE_RECT)
    
    TWENTY_RECT.center = (250, 350)
    SCREEN.blit(TWENTY_TEXT,TWENTY_RECT)
    
    THIRTY_RECT.center = (400, 350)
    SCREEN.blit(THIRTY_TEXT, THIRTY_RECT)
    
    TWENTYFIVE_RECT.center = (550, 350)
    SCREEN.blit(TWENTYFIVE_TEXT, TWENTYFIVE_RECT)
    
    FIVE_RECT.center = (700, 350)
    SCREEN.blit(FIVE_TEXT, FIVE_RECT)
    
    FIFTEEN_RECT.center = (850, 350)
    SCREEN.blit(FIFTEEN_TEXT, FIFTEEN_RECT)
    
    TEN_RECT.center = (100, 550)
    SCREEN.blit(TEN_TEXT, TEN_RECT)
    
    TWENTY_RECT.center = (250, 550)
    SCREEN.blit(TWENTY_TEXT, TWENTY_RECT)
    
    main.sidebar_display()
    main.show_coins()
    pygame.display.update()
    
    db_coins = main.db.reference("/Players/" + main.name + "/Coins").get()
    while state == "shop_accessories":
        main.sidebar_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                           
            if main.db.reference("/Players/" + main.name +"/"+"Accessories").get() is None:
                #add accessories here when u make more
                main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A1": 0})
                main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A2": 0})
                main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A3": 0})
                main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A4": 0})
                main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A5": 0})
                main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A6": 0})
                main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A7": 0})
                main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A8": 0})
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A1_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Accessories/A1").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 25:
                        not_enough_coins()
                           
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-25
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A1": 1})
                        print("A 1 updated")
                        successfully_purchased()
                        
                if A2_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Accessories/A2").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 20:
                        not_enough_coins()
                        
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-20
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A2": 1})
                        print("A 2 updated")
                        successfully_purchased()
                
                if A3_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Accessories/A3").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 30:
                        not_enough_coins()
                                      
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-30
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A3": 1})
                        print("A 3 updated")
                        successfully_purchased()
                
                if A4_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Accessories/A4").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 25:
                        not_enough_coins()
                    
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-25
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A4": 1})
                        print("A 4 updated")
                        successfully_purchased()
                
                if A5_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Accessories/A5").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 5:
                        not_enough_coins()
                        
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-5
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A5": 1})
                        print("A 5 updated")
                        successfully_purchased()
                        
                if A6_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Accessories/A6").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 15:
                        not_enough_coins()
                                            
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-15
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A6": 1})
                        print("A 6 updated") 
                        successfully_purchased() 
                                              
                if A7_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Accessories/A7").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 10:
                        not_enough_coins()
                                            
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-10
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A7": 1})
                        print("A 7 updated")  
                        successfully_purchased()                      
                
                if A8_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Accessories/A8").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 20:
                        not_enough_coins()
                                            
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-20
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Accessories").update({"A8": 1})
                        print("A 8 updated")  
                        successfully_purchased()

def shop_hair():
    global state
    SCREEN.fill("white")
    HAIR_TEXT = TITLE_FONT.render("""hair""", True, "pink", "white")
    HAIR_TEXT_RECT = HAIR_TEXT.get_rect()
    HAIR_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2-250)
    SCREEN.blit(HAIR_TEXT, HAIR_TEXT_RECT)
    
    #add new hair to store here
    SCREEN.blit(H1, H1_RECT)
    SCREEN.blit(H2, H2_RECT)
    SCREEN.blit(H3, H3_RECT)
    SCREEN.blit(H4, H4_RECT)
    SCREEN.blit(H5, H5_RECT)
    SCREEN.blit(H6, H6_RECT)
    SCREEN.blit(H7, H7_RECT)
    SCREEN.blit(H8, H8_RECT)
    
    #prices
    TWENTY_RECT.center = (100, 350)
    SCREEN.blit(TWENTY_TEXT, TWENTY_RECT)
    
    TWENTY_RECT.center = (250, 350)
    SCREEN.blit(TWENTY_TEXT,TWENTY_RECT)
    
    FIFTEEN_RECT.center = (400, 350)
    SCREEN.blit(FIFTEEN_TEXT, FIFTEEN_RECT)
    
    TWENTY_RECT.center = (550, 350)
    SCREEN.blit(TWENTY_TEXT, TWENTY_RECT)
    
    FIFTY_RECT.center = (700, 350)
    SCREEN.blit(FIFTY_TEXT, FIFTY_RECT)
    
    FIFTEEN_RECT.center = (850, 350)
    SCREEN.blit(FIFTEEN_TEXT, FIFTEEN_RECT)
    
    TEN_RECT.center = (100, 550)
    SCREEN.blit(TEN_TEXT, TEN_RECT)
    
    NINENINE_RECT.center = (250, 550)
    SCREEN.blit(NINENINE_TEXT, NINENINE_RECT)
    
    main.sidebar_display()
    main.show_coins()
    pygame.display.update()
    
    db_coins = main.db.reference("/Players/" + main.name + "/Coins").get()
    while state == "shop_hair":
        main.sidebar_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                           
            if main.db.reference("/Players/" + main.name +"/"+"Hair").get() is None:
                #add hair here when u make more
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H1": 0})
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H2": 0})
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H3": 0})
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H4": 0})
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H5": 0})
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H6": 0})
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H7": 0})
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H8": 0})
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if H1_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Hair/H1").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 20:
                        not_enough_coins()
                           
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-20
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H1": 1})
                        print("H 1 updated")
                        successfully_purchased()
                        
                if H2_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Hair/H2").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 20:
                        not_enough_coins()
                        
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-20
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H2": 1})
                        print("H 2 updated")
                        successfully_purchased()
                
                if H3_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Hair/H3").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 15:
                        not_enough_coins()
                                      
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-15
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H3": 1})
                        print("H 3 updated")
                        successfully_purchased()
                
                if H4_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Hair/H4").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 20:
                        not_enough_coins()
                    
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-20
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H4": 1})
                        print("H 4 updated")
                        successfully_purchased()
                
                if H5_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Hair/H5").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 50:
                        not_enough_coins()
                        
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-50
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H5": 1})
                        print("H 5 updated")
                        successfully_purchased()
                        
                if H6_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Hair/H6").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 15:
                        not_enough_coins()
                                            
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-15
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H6": 1})
                        print("H 6 updated") 
                        successfully_purchased() 
                                              
                if H7_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Hair/H7").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 10:
                        not_enough_coins()
                                            
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-10
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H7": 1})
                        print("H 7 updated")  
                        successfully_purchased()                      
                
                if H8_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Hair/H8").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 99:
                        not_enough_coins()
                                            
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-99
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H8": 1})
                        print("H 8 updated")  
                        successfully_purchased()
                
def shop_pets():
    global state
    SCREEN.fill("white")
    PETS_TEXT = TITLE_FONT.render("""pets""", True, "pink", "white")
    PETS_TEXT_RECT = PETS_TEXT.get_rect()
    PETS_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2-250)
    SCREEN.blit(PETS_TEXT, PETS_TEXT_RECT)
    
    #add new pets to store here
    SCREEN.blit(P1, P1_RECT)
    SCREEN.blit(P2, P2_RECT)
    SCREEN.blit(P3, P3_RECT)
    SCREEN.blit(P4, P4_RECT)
    SCREEN.blit(P5, P5_RECT)

    
    #prices
    TWENTY_RECT.center = (100, 350)
    SCREEN.blit(TWENTY_TEXT, TWENTY_RECT)
    
    TWENTY_RECT.center = (250, 350)
    SCREEN.blit(TWENTY_TEXT,TWENTY_RECT)
    
    FIFTEEN_RECT.center = (400, 350)
    SCREEN.blit(FIFTEEN_TEXT, FIFTEEN_RECT)
    
    TWENTY_RECT.center = (550, 350)
    SCREEN.blit(TWENTY_TEXT, TWENTY_RECT)
    
    FIFTY_RECT.center = (700, 350)
    SCREEN.blit(FIFTY_TEXT, FIFTY_RECT)
    
    main.sidebar_display()
    main.show_coins()
    pygame.display.update()
    
    db_coins = main.db.reference("/Players/" + main.name + "/Coins").get()
    while state == "shop_pets":
        main.sidebar_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                           
            if main.db.reference("/Players/" + main.name +"/"+"Hair").get() is None:
                #add hair here when u make more
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H1": 0})
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H2": 0})
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H3": 0})
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H4": 0})
                main.db.reference("/Players/" + main.name + "/" + "Hair").update({"H5": 0})
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if P1_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Pets/P1").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 20:
                        not_enough_coins()
                           
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-20
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Pets").update({"P1": 1})
                        print("P 1 updated")
                        successfully_purchased()
                if P2_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Pets/P2").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 20:
                        not_enough_coins()
                           
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-20
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Pets").update({"P2": 1})
                        print("P 2 updated")
                        successfully_purchased()
                if P3_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Pets/P3").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 15:
                        not_enough_coins()
                           
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-20
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Pets").update({"P3": 1})
                        print("P 3 updated")
                        successfully_purchased()
                if P4_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Pets/P4").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 20:
                        not_enough_coins()
                           
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-20
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Pets").update({"P4": 1})
                        print("P 4 updated")
                        successfully_purchased()
                if P5_RECT.collidepoint(event.pos):
                    if main.db.reference("/Players/" + main.name+"/"+"Pets/P5").get() == 1:
                        already_purchased()
                        
                    elif db_coins < 50:
                        not_enough_coins()
                           
                    else: 
                        dbcoins = main.db.reference("/Players/" + main.name + "/Coins").get()-20
                        print(dbcoins)
                        main.db.reference("/Players/" + main.name + "/").update({"Coins": dbcoins})
                        main.db.reference("/Players/" + main.name + "/" + "Pets").update({"P5": 1})
                        print("P 5 updated")
                        successfully_purchased()
        
                        
                