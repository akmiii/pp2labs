import pygame
from random import randint, choice
import time
import psycopg2
from config import params

name = input('Enter your name: ')

pygame.init()

#Initialization
WIDTH, HEIGHT = 800, 600
FPS = 45

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racer')

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

#Loading the images
background_img = pygame.image.load("img/racer/AnimatedStreet.png")
player_img = pygame.image.load('img/racer/Player.png')
enemy_img = pygame.image.load("img/racer/Enemy.png")
coin_img = pygame.transform.scale(pygame.image.load("img/racer/coin.png"), (25, 25))
coin_img2 = pygame.transform.scale(pygame.image.load("img/racer/fire.png"), (25, 25))
coin_img3 = pygame.transform.scale(pygame.image.load("img/racer/profits.png"), (25, 25))
background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

#The list of the coins
coin_list = [coin_img, coin_img2, coin_img3]
flag = False

#For movement of the background
bgY = 0
bgY2 = -background.get_height()
BGSPEED = 5

#Loading the Sound
sound = pygame.mixer.Sound('music/biting.wav')
crash = pygame.mixer.Sound('music/crash.wav')
pygame.mixer.music.load('music/tokyo_drift.mp3')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 400
        self.y = 500
        self.speed = 10
        self.image = pygame.transform.scale(player_img, (40, 90))
        self.surf = pygame.Surface((40, 90), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT] and self.rect.right <= WIDTH:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_UP] and self.rect.top >= 0:
            self.rect.move_ip(0,-self.speed)
        if keys[pygame.K_DOWN] and self.rect.bottom <= HEIGHT:
            self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(self.image, (0, 0))
        screen.blit(self.surf, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = randint(7, 10)
        self.x = randint(80, WIDTH - 80)
        self.y = -100
        self.image = pygame.transform.scale(enemy_img, (40, 90))
        self.surf = pygame.Surface((40, 90), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    
    def move(self):
        self.rect.move_ip(0, self.speed)
    
    def draw(self):
        self.surf.blit(self.image, (0, 0))
        screen.blit(self.surf, self.rect)

    def remove(self):
        if self.rect.top > HEIGHT:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.speed = 10
        self.x = randint(80, WIDTH - 80)
        self.y = -100
        self.image = img
        self.surf = pygame.Surface((25, 25), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    
    def move(self):
        self.rect.move_ip(0, self.speed)
    
    def draw(self):
        self.surf.blit(self.image, (0, 0))
        screen.blit(self.surf, self.rect)
    
    def remove(self):
        if self.rect.top > HEIGHT:
            self.kill()

    def weight(self):
        global SCORE
        if self.image == coin_img:
            SCORE += 1
        elif self.image == coin_img2:
            SCORE += 5
        elif self.image == coin_img3:
            SCORE += 10

#Creating the Clock
clock = pygame.time.Clock()


db = psycopg2.connect(**params)
cursor = db.cursor()

# create_table = '''
# CREATE TABLE racer(
#     person_name VARCHAR PRIMARY KEY,
#     highscore INT NOT NULL
# );
# '''
# cursor.execute(create_table)

# drop_table = '''DROP TABLE racer'''
# cursor.execute(drop_table)

insert = '''
    INSERT INTO racer VALUES (%s, %s)
'''

#Creating the font for texts
font = pygame.font.SysFont("Times New Roman", 25)
font_large = pygame.font.SysFont("Times New Roman", 75)

#Losing text
game_over = font_large.render("GAME OVER", False, BLACK)

player = Player()

restart = True

while restart:
    finished = False
    lose = False

    enemies = pygame.sprite.Group([Enemy() for _ in range(3)])
    coins = pygame.sprite.Group([Coin(choice(coin_list)) for _ in range(4)])

    pygame.mixer.music.play(-1)

    SCORE = 0
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                restart = False
                finished = True

            #restart by tapping the space    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                finished = True

        screen.blit(background, (0, bgY))
        screen.blit(background, (0, bgY2))

        #Movement of the background
        if bgY > background.get_height():
            bgY = -background.get_height()
        if bgY2 > background.get_height():
            bgY2 = -background.get_height()

        bgY += BGSPEED
        bgY2 += BGSPEED

        #Text
        text = font.render(f"SCORE: {SCORE}", False, RED)
        screen.blit(text, (50, 20))

        #Drawing and moving of the player
        player.draw()
        player.move()
        
        #Showing at most 3 enemies
        if len(enemies) < 3:
            enemies.add(Enemy())

        #Showing at most 4 coins
        if len(coins) < 4:
            coins.add(Coin(choice(coin_list)))

        #Drawing and moving of the enemies
        for enemy in enemies:
            enemy.draw()
            enemy.move()
            enemy.remove()

        #Drawing and moving of the coins
        for coin in coins:
            coin.draw()
            coin.move()
            coin.remove()
        
        #Collision with the enemies
        if pygame.sprite.spritecollide(player, enemies, False): #Find sprites in a group that intersect another sprite
            crash.play()
            lose = True

        for coin in coins:

            #Collision with the coins
            if pygame.sprite.collide_rect(player, coin): #Collision detection between two sprites, using rects
                sound.play()
                coin.weight()
                coin.kill()
                coins.add(Coin(choice(coin_list)))

        #To not having the double cars
        for enemy in enemies:
            for enemy2 in enemies:
                if enemy != enemy2 and pygame.sprite.collide_rect(enemy, enemy2): #Collision detection between two sprites, using rects
                    enemy2.kill()

        #Increasing enemy's speed
        for enemy in enemies:
            if SCORE % 10 == 0 and SCORE != 0:
                enemy.speed += 2

        #Texts
        losing = font.render(f'You lost with {SCORE} points', True, BLACK)
        tapping = font.render(f'TAP SPACE TO RESTART', True, PURPLE)

        while lose:
            pygame.draw.rect(screen, WHITE, (100, 100, 600, 300))
            pygame.mixer.music.pause()

            #Texts
            text_pos = game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))
            screen.blit(game_over, (text_pos[0], text_pos[1] - 70))
            screen.blit(losing, (295, 290))
            screen.blit(tapping, (250, 330))
            
            pygame.display.update()
            time.sleep(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    finished = True
                    lose = False
                    win = False

                #restart by tapping the space   
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    lose = False
                    win = False
                    finished = True

            try:
                get = f'''
                    SELECT highscore FROM racer WHERE person_name = '{name}';
                '''
                cursor.execute(get)
                output = cursor.fetchone()
                scorePlayer = output[0]
                #print(output)
                flag = True
            except:
                pass

            if flag == True:
                if SCORE > scorePlayer:
                    update = f'''
                    UPDATE racer SET highscore = {SCORE} WHERE person_name = '{name}';
                '''
                    cursor.execute(update)
            else:
                cursor.execute(insert, (f'{name}', f'{SCORE}'))    
            


            pygame.display.flip()
            cursor.close()
            db.commit()
            db.close()    

        pygame.display.flip()
    pygame.display.flip()
pygame.quit()