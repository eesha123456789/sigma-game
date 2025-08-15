from array import *
import pygame #user interface
import sys #allows us to exit

import main

pygame.init() #initializes all modules to get everything started

#make this bigger so we can have a menu on top of the screen
WIDTH, HEIGHT = 1285, 660
#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seldrow!")


# 2nd parameter is the font size
TITLE_FONT = pygame.font.Font("fonts/Aloevera-OVoWO.ttf", 100)

#Character Picking variables
character_picked=""
state = ""

C1 = pygame.image.load("image_folder/characters/C1.png").convert()
C1 = pygame.transform.scale(C1, (200,300))
C1_RECT = C1.get_rect(center = ((WIDTH/2)-500, (HEIGHT/2)+100))

C2 = pygame.image.load("image_folder/characters/C2.png").convert()
C2 = pygame.transform.scale(C2, (200,300))
C2_RECT = C2.get_rect(center = ((WIDTH/2)-300, (HEIGHT/2)+100))

C3 = pygame.image.load("image_folder/characters/C3.png").convert()
C3 = pygame.transform.scale(C3, (200,300))
C3_RECT = C3.get_rect(center = ((WIDTH/2)-100, (HEIGHT/2)+100))

C4 = pygame.image.load("image_folder/characters/C4.png").convert()
C4 = pygame.transform.scale(C4, (200,300))
C4_RECT = C4.get_rect(center = ((WIDTH/2)+100, (HEIGHT/2)+100))

C5 = pygame.image.load("image_folder/characters/C5.png").convert()
C5 = pygame.transform.scale(C5, (200,300))
C5_RECT = C5.get_rect(center = ((WIDTH/2)+300, (HEIGHT/2) + 100))

C6 = pygame.image.load("image_folder/characters/C6.png").convert()
C6 = pygame.transform.scale(C6, (200,300))
C6_RECT = C6.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2) +100))



#different center for character that is on the side

P1 = pygame.image.load("image_folder/characters/C1.png").convert()
P1.set_colorkey(P1.get_at((0,0)))
P1 = pygame.transform.scale(P1, (200,300))
P1_RECT = P1.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2)))

P2 = pygame.image.load("image_folder/characters/C2.png").convert()
P2.set_colorkey(P2.get_at((0,0)))
P2 = pygame.transform.scale(P2, (200,300))
P2_RECT = P2.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2)))

P3 = pygame.image.load("image_folder/characters/C3.png").convert()
P3.set_colorkey(P3.get_at((0,0)))
P3 = pygame.transform.scale(P3, (200,300))
P3_RECT = P3.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2)))

P4 = pygame.image.load("image_folder/characters/C4.png").convert()
P4.set_colorkey(P4.get_at((0,0)))
P4 = pygame.transform.scale(P4, (200,300))
P4_RECT = P4.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2)))

P5 = pygame.image.load("image_folder/characters/C5.png").convert()
P5.set_colorkey(P5.get_at((0,0)))
P5 = pygame.transform.scale(P5, (200,300))
P5_RECT = P5.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2) ))

P6 = pygame.image.load("image_folder/characters/C6.png").convert()
P6.set_colorkey(P6.get_at((0,0)))
P6 = pygame.transform.scale(P6, (200,300))
P6_RECT = P6.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2)))

PLATFORM = pygame.image.load("image_folder/Platform.PNG").convert()
PLATFORM = pygame.transform.scale(PLATFORM, (200,100))
PLATFORM_RECT = PLATFORM.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2)+180))

#different expressions
E1 = pygame.image.load("image_folder/expressions/e1.png").convert()
#make the parts with the transcolor transparent
E1.set_colorkey(E1.get_at((0,0)))
#transform and scale still need to do
E1 = pygame.transform.scale(E1, (200,300))
E1_RECT = E1.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2)))

E2 = pygame.image.load("image_folder/expressions/e2.png").convert()
E2.set_colorkey(E2.get_at((0,0)))
E2 = pygame.transform.scale(E2, (200,300))
E2_RECT = E2.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2)))

E3 = pygame.image.load("image_folder/expressions/e3.png").convert()
E3.set_colorkey(E3.get_at((0,0)))
E3 = pygame.transform.scale(E3, (200,300))
E3_RECT = E3.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2)))

E4 = pygame.image.load("image_folder/expressions/e4.png").convert()
E4.set_colorkey(E4.get_at((0,0)))
E4 = pygame.transform.scale(E4, (200,300))
E4_RECT = E4.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2)))

E5 = pygame.image.load("image_folder/expressions/e5.png").convert()
E5.set_colorkey(E5.get_at((0,0)))
E5 = pygame.transform.scale(E5, (200,300))
E5_RECT = E5.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2)))

E6 = pygame.image.load("image_folder/expressions/e6.png").convert()
E6.set_colorkey(E6.get_at((0,0)))
E6 = pygame.transform.scale(E6, (200,300))
E6_RECT = E6.get_rect(center = ((WIDTH/2)+500, (HEIGHT/2)))


def pick_character():
    global state, character_picked
    state="pick_character"
    SCREEN.fill("white")
    HEADING_TEXT = TITLE_FONT.render("""Pick a character to start""", True, "pink", None)
    HEADING_TEXT_RECT = HEADING_TEXT.get_rect()
    HEADING_TEXT_RECT.center = (WIDTH // 2, HEIGHT - 550)
    SCREEN.blit(HEADING_TEXT, HEADING_TEXT_RECT)
        
    SCREEN.blit(C1, C1_RECT)
    SCREEN.blit(C2, C2_RECT)
    SCREEN.blit(C3, C3_RECT)
    SCREEN.blit(C4, C4_RECT)
    SCREEN.blit(C5, C5_RECT)
    SCREEN.blit(C6, C6_RECT)

    pygame.display.update()
    while state=="pick_character":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if C1_RECT.collidepoint(event.pos):
                    character_picked="C1"
                elif C2_RECT.collidepoint(event.pos):
                    character_picked="C2"
                elif C3_RECT.collidepoint(event.pos):
                    character_picked="C3"
                elif C4_RECT.collidepoint(event.pos):
                    character_picked="C4"
                elif C5_RECT.collidepoint(event.pos):
                    character_picked="C5"
                elif C6_RECT.collidepoint(event.pos):
                    character_picked="C6"
                    
                if character_picked != "":
                    main.state="menu"
                    state="picked_character"
                    main.db.reference("/Players/" + main.name + "/").update({"Coins":0})
                    main.db.reference("/Players/"+ main.name +"/").update({"Character": character_picked})
                    main.menu()
     
def show_character():
    #white box above characters 
    #use this to cover up head accessories when changing them in inventory
    #(x, y, width, height)
    WHITE_BOX_RECT=pygame.Rect((WIDTH/2)+400,(HEIGHT/2)-180,200, 200)
    pygame.draw.rect(SCREEN, "white", WHITE_BOX_RECT)
    character_picked = main.db.reference("/Players/" + main.name +"/"+"Character").get()
    SCREEN.blit(PLATFORM, PLATFORM_RECT)
    if character_picked == "C1":
        SCREEN.blit(P1, P1_RECT)
    elif character_picked == "C2":
        SCREEN.blit(P2, P2_RECT)
    elif character_picked == "C3":
        SCREEN.blit(P3, P3_RECT)
    elif character_picked == "C4":
        SCREEN.blit(P4, P4_RECT)
    elif character_picked == "C5":
        SCREEN.blit(P5, P5_RECT)
    elif character_picked == "C6":
        SCREEN.blit(P6, P6_RECT) 
    
    #facial expressions
    db_coins = main.db.reference("/Players/" + main.name + "/Coins").get()
    if db_coins < 10:
        SCREEN.blit(E1, E1_RECT)
    
    if db_coins >= 10 and db_coins < 20:
        SCREEN.blit(E2, E2_RECT)
        
    if db_coins >= 20 and db_coins < 30:
        SCREEN.blit(E3, E3_RECT)
        
    if db_coins >= 30 and db_coins < 40:
        SCREEN.blit(E4, E4_RECT)
    
    if db_coins >= 40 and db_coins < 50:
        SCREEN.blit(E5, E5_RECT)
    
    if db_coins >= 50:
        SCREEN.blit(E6, E6_RECT)
        
    #adding stuff on top
    clothes = main.db.reference("/Players/" + main.name +"/Cur Clothes").get()
    if clothes != None and clothes != "":
        c = pygame.image.load("image_folder/clothes/" + clothes).convert()
        c.set_colorkey(c.get_at((0,0)))
        c = pygame.transform.scale(c, (200, 300))
        c_rect = c.get_rect(center = ((WIDTH/2)+500, HEIGHT/2 ))
        SCREEN.blit(c, c_rect)
    
    hair = main.db.reference("/Players/" + main.name +"/Cur Hair").get()
    if hair != None and hair != "":
        h = pygame.image.load("image_folder/hair/" + hair).convert()
        h.set_colorkey(h.get_at((0,0)))
        h = pygame.transform.scale(h, (200, 300))
        h_rect = h.get_rect(center = ((WIDTH/2)+500, HEIGHT/2 -63))
        SCREEN.blit(h, h_rect)
        
    #head stuff
    accesso_top = main.db.reference("/Players/" + main.name +"/Cur A Top").get()
    if accesso_top != None and accesso_top != "":
        a = pygame.image.load("image_folder/accessories/" + accesso_top).convert()
        a.set_colorkey(a.get_at((0,0)))
        a = pygame.transform.scale(a, (200, 300))
        a_rect = a.get_rect(center = ((WIDTH/2)+500, HEIGHT/2 -63))
        SCREEN.blit(a, a_rect)
     
    #shoes
    accesso_bottom = main.db.reference("/Players/" + main.name +"/Cur A Bottom").get()   
    if accesso_bottom != None and accesso_bottom != "":
        a2 = pygame.image.load("image_folder/accessories/" + accesso_bottom).convert()
        a2.set_colorkey(a2.get_at((0,0)))
        a2 = pygame.transform.scale(a2, (200, 300))
        a2_rect = a2.get_rect(center = ((WIDTH/2)+500, HEIGHT/2+5))
        SCREEN.blit(a2, a2_rect)
    
    # white box to cover up prev pet
    WHITE_BOX_RECT_2=pygame.Rect((WIDTH/2)+450,(HEIGHT/2)-290,100, 130)
    pygame.draw.rect(SCREEN, "white", WHITE_BOX_RECT_2)

    #pets
    pets = main.db.reference("/Players/" + main.name +"/Cur Pet").get()   
    if pets != None and pets != "":
        p = pygame.image.load("image_folder/pets/" + pets).convert()
        p.set_colorkey(p.get_at((0,0)))
        p = pygame.transform.scale(p, (100, 100))
        p_rect = p.get_rect(center = ((WIDTH/2)+500, HEIGHT/2-210))
        SCREEN.blit(p, p_rect)
    pygame.display.update()
                  