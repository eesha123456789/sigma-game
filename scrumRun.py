import sys
import pygame
import random
import main

pygame.init()

#make this bigger so we can have a menu on top of the screen
WIDTH, HEIGHT = 1285, 660
#Variables for set up of dislay window (how it looks)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

game_font = pygame.font.Font("scrum_images/PressStart2P-Regular.ttf", 24)
state=""

class Cloud(pygame.sprite.Sprite):
    def __init__(self, image, x_pos, y_pos):
        super().__init__()
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.rect.x -= 1


class Scrummer(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.running_sprites = []
        self.ducking_sprites = []
        self.jumping_sprites = []

        self.running_sprites.append(pygame.transform.scale(pygame.image.load("scrum_images/scrummer1.png"), (80, 100)))
        self.running_sprites.append(pygame.transform.scale(pygame.image.load("scrum_images/scrummer2.png"), (80, 100)))

        self.ducking_sprites.append(pygame.transform.scale(pygame.image.load(f"scrum_images/scrummerduck1.png"), (110, 60)))
        self.ducking_sprites.append(pygame.transform.scale(pygame.image.load(f"scrum_images/scrummerduck2.png"), (110, 60)))
        
        self.jumping_sprites.append(pygame.transform.scale(pygame.image.load(f"scrum_images/scrummerjump.png"), (110, 60)))
        self.jumping_sprites.append(pygame.transform.scale(pygame.image.load(f"scrum_images/scrummerjump.png"), (110, 60)))


        self.x_pos = x_pos
        self.y_pos = y_pos
        self.current_image = 0
        self.image = self.running_sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.velocity = 50
        self.gravity = 1.4
        self.ducking = False
        self.jumping = False

    def jump(self):
        scrumJump.play()
        if self.rect.centery >= 360:
            while self.rect.centery - self.velocity > 40:
                self.rect.centery -= 1
                self.jumping = True
            

    def duck(self):
        self.ducking = True
        self.rect.centery = 380

    def unduck(self):
        self.ducking = False
        self.rect.centery = 360

    def apply_gravity(self):
        if self.rect.centery <= 360:
            self.rect.centery += self.gravity

    def update(self):
        self.animate()
        self.apply_gravity()

    def animate(self):
        self.current_image += 0.05
        if self.current_image >= 2:
            self.current_image = 0
        if self.rect.centery>360:
            self.jumping=False
            
        if self.ducking:
            self.image = self.ducking_sprites[int(self.current_image)]
        elif self.jumping:
            self.image = self.jumping_sprites[int((self.current_image))]
        else:
            self.image = self.running_sprites[int(self.current_image)]


class Poop(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.sprites = []
        for i in range(1, 7):
            current_sprite = pygame.transform.scale(pygame.image.load(f"scrum_images/poop.png"), (75, 75))
            self.sprites.append(current_sprite)
        self.image = random.choice(self.sprites)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.x_pos -= game_speed
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 1300
        self.y_pos = random.choice([280, 295, 350])
        self.sprites = []
        self.sprites.append(
            pygame.transform.scale(
                pygame.image.load("scrum_images/bird1.png"), (84, 62)))
        self.sprites.append(
            pygame.transform.scale(
                pygame.image.load("scrum_images/bird2.png"), (84, 62)))
        self.current_image = 0
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.animate()
        self.x_pos -= game_speed
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def animate(self):
        self.current_image += 0.025
        if self.current_image >= 2:
            self.current_image = 0
        self.image = self.sprites[int(self.current_image)]
        

# Variables


game_speed = 2
jump_count = 10
player_score = 0
game_over = False
obstacle_timer = 0
obstacle_spawn = False
obstacle_cooldown = 1300

# Surfaces

ground = pygame.image.load("scrum_images/ground.png")
ground = pygame.transform.scale(ground, (1280, 20))
ground_x = 0
ground_rect = ground.get_rect(center=(640, 400))
cloud = pygame.image.load("scrum_images/cloud.png")
cloud = pygame.transform.scale(cloud, (200, 80))

# Groups

cloud_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
runner_group = pygame.sprite.GroupSingle()
bird_group = pygame.sprite.Group()

# Objects
runner = Scrummer(50, 360)
runner_group.add(runner)

# Sounds
scrumLose = pygame.mixer.Sound("Sounds/scrumLose.mp3")
scrumCheckpoint = pygame.mixer.Sound("Sounds/scrumCheckpoint.mp3")
scrumJump = pygame.mixer.Sound("Sounds/scrumJump.mp3")

# Events
CLOUD_EVENT = pygame.USEREVENT
pygame.time.set_timer(CLOUD_EVENT, 3000)



def end_game():
    global player_score, game_speed, state, game_over
    game_over_text = game_font.render("Game Over!", True, "black")
    game_over_rect = game_over_text.get_rect(center=(640, 300))
    score_text = game_font.render(f"Score: {int(player_score)}", True, "black")
    score_rect = score_text.get_rect(center=(640, 340))
    SCREEN.blit(game_over_text, game_over_rect)
    SCREEN.blit(score_text, score_rect)
    game_speed = 2
    cloud_group.empty()
    obstacle_group.empty()
    game_over=True
    db_coins = main.db.reference("/Players/" + main.name + "/Coins").get() 
    main.coins = db_coins + (int)(player_score/10)
    main.db.reference("/Players/"+ main.name).update({"Coins": (main.coins)})
    main.sidebar_display()
    pygame.display.update()
    while state=="scrumEnd":
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state="scrumrun"
                    game_over = False
                    game_speed = 2
                    player_score = 0
                    run()
        main.sidebar_function()
    

def run():
    global state, game_over, runner, current_cloud_y, current_cloud, cloud_group, player_score, game_speed, obstacle_group, scrumLoses, scrumCheckpoint,obstacle_timer, obstacle_cooldown, obstacle_spawn, game_font, player_score_surface, ptero_group, runner_group, cloud_group, obstacle_group, ground, ground_x
    state="scrumrun"
    while state=="scrumrun":
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            runner.duck()
        else:
            if runner.ducking:
                runner.unduck()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == CLOUD_EVENT:
                current_cloud_y = random.randint(50, 300)
                current_cloud = Cloud(cloud, 1380, current_cloud_y)
                cloud_group.add(current_cloud)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    runner.jump()


        SCREEN.fill("white")

        # Collisions
        if pygame.sprite.spritecollide(runner_group.sprite, obstacle_group, False):
            game_over = True
            scrumLose.play()
        if game_over:
            state="scrumEnd"
            end_game()

        if not game_over:
            game_speed += 0.0002
            if round(player_score, 1) % 100 == 0 and int(player_score) > 0:
                scrumCheckpoint.play()

            if pygame.time.get_ticks() - obstacle_timer >= obstacle_cooldown:
                obstacle_spawn = True

            if obstacle_spawn:
                obstacle_random = random.randint(1, 50)
                if obstacle_random in range(1, 7):
                    new_obstacle = Poop(1280, 340)
                    obstacle_group.add(new_obstacle)
                    obstacle_timer = pygame.time.get_ticks()
                    obstacle_spawn = False
                elif obstacle_random in range(7, 10):
                    new_obstacle = Bird()
                    obstacle_group.add(new_obstacle)
                    obstacle_timer = pygame.time.get_ticks()
                    obstacle_spawn = False

            player_score += 0.1
            player_score_surface = game_font.render(
                str(int(player_score)), True, ("black"))
            SCREEN.blit(player_score_surface, (1150, 10))

            cloud_group.update()
            cloud_group.draw(SCREEN)

            bird_group.update()
            bird_group.draw(SCREEN)

            runner_group.update()
            runner_group.draw(SCREEN)

            obstacle_group.update()
            obstacle_group.draw(SCREEN)

            ground_x -= game_speed

            SCREEN.blit(ground, (ground_x, 360))
            SCREEN.blit(ground, (ground_x + 1280, 360))

            if ground_x <= -1280:
                ground_x = 0   
        pygame.display.update()     

    clock.tick(120)
    pygame.display.update()