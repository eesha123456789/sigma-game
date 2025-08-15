from array import *
import pygame #user interface
import sys #allows us to exit
import main
import characterClass

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

TITLE_FONT = pygame.font.Font("fonts/Aloevera-OVoWO.ttf", 100)
INVENTORY_BUTTON_FONT = pygame.font.Font("fonts/FredokaOne-Regular.otf", 60)




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

#pets

PETS1 = pygame.image.load("image_folder/pets/dog.png").convert()
PETS1.set_colorkey(PETS1.get_at((0,0)))
PETS1 = pygame.transform.scale(PETS1, (175, 175))
PETS1_RECT = PETS1.get_rect(center = (100, 250))

PETS2 = pygame.image.load("image_folder/pets/cat.png").convert()
PETS2.set_colorkey(PETS2.get_at((0,0)))
PETS2 = pygame.transform.scale(PETS2, (175, 175))
PETS2_RECT = PETS2.get_rect(center = (250, 250))

PETS3 = pygame.image.load("image_folder/pets/hamster.png").convert()
PETS3.set_colorkey(PETS3.get_at((0,0)))
PETS3 = pygame.transform.scale(PETS3, (175, 175))
PETS3_RECT = PETS3.get_rect(center = (400, 250))

PETS4 = pygame.image.load("image_folder/pets/walrus.png").convert()
PETS4.set_colorkey(PETS4.get_at((0,0)))
PETS4 = pygame.transform.scale(PETS4, (130, 100))
PETS4_RECT = PETS4.get_rect(center = (550, 250))

PETS5 = pygame.image.load("image_folder/pets/fish.png").convert()
PETS5.set_colorkey(PETS5.get_at((0,0)))
PETS5 = pygame.transform.scale(PETS5, (175, 175))
PETS5_RECT = A5.get_rect(center = (700, 290))


#inventory

INVENTORY_BOX_COLOR = TITLE_PINK
CLOTHES_STORAGE_RECT = pygame.Rect(210,HEIGHT//2-80,360,80)
ACCESSO_STORAGE_RECT = pygame.Rect(680,HEIGHT//2-80,360,80)
HAIR_STORAGE_RECT = pygame.Rect(210,HEIGHT//2+80,360,80)
PETS_STORAGE_RECT = pygame.Rect(680,HEIGHT//2+80,360,80)

               
def inventory():
    global state
    state="inventory"
    SCREEN.fill(BG_PINK)
    INVENTORY_TEXT = TITLE_FONT.render("""INVENTORY""", True, TITLE_PINK, None)
    INVENTORY_TEXT_RECT = INVENTORY_TEXT.get_rect()
    INVENTORY_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2-200)
    SCREEN.blit(INVENTORY_TEXT,INVENTORY_TEXT_RECT)
    main.sidebar_display()
    
    #buttons
    pygame.draw.rect(SCREEN, INVENTORY_BOX_COLOR, CLOTHES_STORAGE_RECT, 100)
    CLOTHES_TEXT = INVENTORY_BUTTON_FONT.render("     clothes", True,"black")
    SCREEN.blit(CLOTHES_TEXT, CLOTHES_STORAGE_RECT)
    
    pygame.draw.rect(SCREEN, INVENTORY_BOX_COLOR, ACCESSO_STORAGE_RECT, 100)
    ACCESSO_TEXT = INVENTORY_BUTTON_FONT.render(" accessories", True,"black")
    SCREEN.blit(ACCESSO_TEXT, ACCESSO_STORAGE_RECT)
    
    pygame.draw.rect(SCREEN, INVENTORY_BOX_COLOR, HAIR_STORAGE_RECT, 100)
    HAIR_TEXT = INVENTORY_BUTTON_FONT.render("        hair", True,"black")
    SCREEN.blit(HAIR_TEXT, HAIR_STORAGE_RECT)
    
    pygame.draw.rect(SCREEN, INVENTORY_BOX_COLOR, PETS_STORAGE_RECT, 100)
    PETS_TEXT = INVENTORY_BUTTON_FONT.render("        pets", True,"black")
    SCREEN.blit(PETS_TEXT, PETS_STORAGE_RECT)
    
    pygame.display.update()
    
    main.sidebar_function()
    while state =="inventory":
        main.sidebar_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CLOTHES_STORAGE_RECT.collidepoint(event.pos):
                    state="my_clothes"
                    my_clothes()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HAIR_STORAGE_RECT.collidepoint(event.pos):
                    state="my_hair"
                    my_hair()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ACCESSO_STORAGE_RECT.collidepoint(event.pos):
                    state="my_accessories"
                    my_accessories()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PETS_STORAGE_RECT.collidepoint(event.pos):
                    state="my_pets"
                    my_pets()

def my_clothes():
    SCREEN.fill("white")
    TITLE_TEXT = TITLE_FONT.render("""my clothes""", True, "pink", None)
    TITLE_TEXT_RECT = TITLE_TEXT.get_rect()
    TITLE_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2-250)
    SCREEN.blit(TITLE_TEXT, TITLE_TEXT_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Clothes/Clothes1").get() == 1:
        SCREEN.blit(CLOTHES1, CLOTHES1_RECT)
        
    if main.db.reference("/Players/" + main.name + "/" + "Clothes/Clothes2").get() == 1:
        SCREEN.blit(CLOTHES2, CLOTHES2_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Clothes/Clothes3").get() == 1:
        SCREEN.blit(CLOTHES3, CLOTHES3_RECT)
        
    if main.db.reference("/Players/" + main.name + "/" + "Clothes/Clothes4").get() == 1:
        SCREEN.blit(CLOTHES4, CLOTHES4_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Clothes/Clothes5").get() == 1:
        SCREEN.blit(CLOTHES5, CLOTHES5_RECT)
        
    if main.db.reference("/Players/" + main.name + "/" + "Clothes/Clothes6").get() == 1:
        SCREEN.blit(CLOTHES6, CLOTHES6_RECT)
    
    main.sidebar_display()
    characterClass.show_character()
    
    pygame.display.update()
    while state=="my_clothes":
        main.sidebar_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if main.db.reference("/Players/" + main.name +"/Cur Clothes").get() is None:
                main.db.reference("/Players/" + main.name + "/").update({"Cur Clothes": ""})
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CLOTHES1_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Clothes": "default_outfit.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if CLOTHES2_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Clothes": "barney.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if CLOTHES3_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Clothes": "greentan_outfit.png"})
                    characterClass.show_character()
                    pygame.display.update()
                    
                if CLOTHES4_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Clothes": "jeantop.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if CLOTHES5_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Clothes": "pink_dress.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if CLOTHES6_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Clothes": "redblue_outfit.png"})
                    characterClass.show_character()
                    pygame.display.update()

def my_hair():
    SCREEN.fill("white")
    TITLE_TEXT = TITLE_FONT.render("""my hair""", True, "pink", None)
    TITLE_TEXT_RECT = TITLE_TEXT.get_rect()
    TITLE_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2-250)
    SCREEN.blit(TITLE_TEXT, TITLE_TEXT_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Hair/H1").get() == 1:
        SCREEN.blit(H1, H1_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Hair/H2").get() == 1:
        SCREEN.blit(H2, H2_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Hair/H3").get() == 1:
        SCREEN.blit(H3, H3_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Hair/H4").get() == 1:
        SCREEN.blit(H4, H4_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Hair/H5").get() == 1:
        SCREEN.blit(H5, H5_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Hair/H6").get() == 1:
        SCREEN.blit(H6, H6_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Hair/H7").get() == 1:
        SCREEN.blit(H7, H7_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Hair/H8").get() == 1:
        SCREEN.blit(H8, H8_RECT)
    
    main.sidebar_display()
    characterClass.show_character()
    
    pygame.display.update()
    while state=="my_hair":
        main.sidebar_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if main.db.reference("/Players/" + main.name +"/Cur Hair").get() is None:
                main.db.reference("/Players/" + main.name + "/").update({"Cur Hair": ""})
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if H1_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Hair": "blackpony.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if H2_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Hair": "blackspiky.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if H3_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Hair": "blondcurly.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if H4_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Hair": "blondpony.png"})
                    characterClass.show_character()
                    pygame.display.update()
                    
                if H5_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Hair": "bluestring.png"})
                    characterClass.show_character()
                    pygame.display.update()
                    
                if H6_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Hair": "brownbob.png"})
                    characterClass.show_character()
                    pygame.display.update()
                    
                if H7_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Hair": "brownsplit.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if H8_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Hair": "farquaad.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
def my_accessories():
    global state
    SCREEN.fill("white")
    TITLE_TEXT = TITLE_FONT.render("""my accessories""", True, "pink", None)
    TITLE_TEXT_RECT = TITLE_TEXT.get_rect()
    TITLE_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2-250)
    SCREEN.blit(TITLE_TEXT, TITLE_TEXT_RECT)
    
    #put all the ones that the player has on the screen
    if main.db.reference("/Players/" + main.name + "/" + "Accessories/A1").get() == 1:
        SCREEN.blit(A1, A1_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Accessories/A2").get() == 1:
        SCREEN.blit(A2, A2_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Accessories/A3").get() == 1:
        SCREEN.blit(A3, A3_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Accessories/A4").get() == 1:
        SCREEN.blit(A4, A4_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Accessories/A5").get() == 1:
        SCREEN.blit(A5, A5_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Accessories/A6").get() == 1:
        SCREEN.blit(A6, A6_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Accessories/A7").get() == 1:
        SCREEN.blit(A7, A7_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Accessories/A8").get() == 1:
        SCREEN.blit(A8, A8_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Accessories/A1").get() == 1:
        SCREEN.blit(A1, A1_RECT)
        
    main.sidebar_display()
    characterClass.show_character()
    
    pygame.display.update()
    while state=="my_accessories":
        main.sidebar_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if main.db.reference("/Players/" + main.name +"/Cur A Top").get() is None:
                main.db.reference("/Players/" + main.name + "/").update({"Cur A Top": ""})
            
            if main.db.reference("/Players/" + main.name +"/Cur A Bottom").get() is None:
                main.db.reference("/Players/" + main.name + "/").update({"Cur A Bottom": ""})
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A1_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur A Bottom": "green_550.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if A2_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur A Bottom": "white_550.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if A3_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur A Bottom": "pink_dunks.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if A4_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur A Bottom": "panda_dunks.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if A5_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur A Top": "bluebow.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if A6_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur A Top": "flowers.png"})
                    characterClass.show_character()
                    pygame.display.update()
                    
                if A7_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur A Top": "shrek.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if A8_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur A Top": "strawhat.png"})
                    characterClass.show_character()
                    pygame.display.update()
        
def my_pets():
    global state
    SCREEN.fill("white")
    TITLE_TEXT = TITLE_FONT.render("""my pets""", True, "pink", None)
    TITLE_TEXT_RECT = TITLE_TEXT.get_rect()
    TITLE_TEXT_RECT.center = (WIDTH // 2, HEIGHT // 2-250)
    SCREEN.blit(TITLE_TEXT, TITLE_TEXT_RECT)
    
    #put all the ones that the player has on the screen
    if main.db.reference("/Players/" + main.name + "/" + "Pets/P1").get() == 1:
        SCREEN.blit(PETS1, PETS1_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Pets/P2").get() == 1:
        SCREEN.blit(PETS2, PETS2_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Pets/P3").get() == 1:
        SCREEN.blit(PETS3, PETS3_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Pets/P4").get() == 1:
        SCREEN.blit(PETS4, PETS4_RECT)
    
    if main.db.reference("/Players/" + main.name + "/" + "Pets/P5").get() == 1:
        SCREEN.blit(PETS5, PETS5_RECT)
    
        
    main.sidebar_display()
    characterClass.show_character()
    
    pygame.display.update()
    while state=="my_pets":
        main.sidebar_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if main.db.reference("/Players/" + main.name +"/Cur Pet").get() is None:
                main.db.reference("/Players/" + main.name + "/").update({"Cur Pet": ""})

                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PETS1_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Pet": "dog.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if PETS2_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Pet": "cat.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if PETS3_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Pet": "hamster.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if PETS4_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Pet": "walrus.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                if PETS5_RECT.collidepoint(event.pos):
                    main.db.reference("/Players/" + main.name + "/").update({"Cur Pet": "fish.png"})
                    characterClass.show_character()
                    pygame.display.update()
                
                
                

