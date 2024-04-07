import pygame
import sys
import random

pygame.init()



#player and enemy and coin classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 50
        self.image = pygame.image.load(r"labka9\images2\player.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.center = (50, 25)
    
    def update(self):


        pressed_key = pygame.key.get_pressed()

        
        if pressed_key[pygame.K_LEFT]:
            if self.rect.bottomleft[0] > 0:
                self.rect.move_ip(-5, 0)
        if pressed_key[pygame.K_RIGHT]:
            if self.rect.bottomright[0] < width_screen:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


    #collision function to detect if player has died or not    
    def collision(self, rect1):
        self.collide = self.rect.colliderect(rect1)
        return self.collide





class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed=None):
        super().__init__()
        self.width = 100
        self.height = 50
        if speed == None:
            speed = 3
        self.speed = speed
        self.image = pygame.image.load(r"labka8\images1\enemy.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10, width_screen-100), -200)
    

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > height_screen:
            self.rect.bottom = 0
            self.rect.center = (random.randint(10, width_screen-100), -100) 

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self, speed=None):
        super().__init__()
        self.image1 = pygame.image.load(r"labka9\images2\coin.png")
        self.image2 = pygame.image.load(r"labka9\images2\coin2.png")
        self.image3 = pygame.image.load(r"labka9\images2\coin3.png")

        if speed==None:
            speed = 2
        self.speed = speed

        self.type = 1
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10, width_screen-100), -200)
    def update(self):
        

        self.rect.move_ip(0, self.speed)
        if self.rect.top > height_screen:
            self.rect.bottom = 0
            self.rect.center = (random.randint(10, width_screen-100), 0) 

    def newcoin(self):
        
        #choosing random coin
        rand = random.randint(1, 3)
        if rand == 1:
            self.image = self.image1
            self.type = 1
        elif rand == 2:
            self.image = self.image2
            self.type = 2
        else:
            self.image = self.image3
            self.type = 3
            

    def draw(self, surface):
        surface.blit(self.image, self.rect)




#predefined colors:
RED = (255, 5, 30)
BLACK = (0, 5, 20)
ORANGE = (226, 99, 16)



#exit the game
def exitgame():
    #pausing game before exiting
    pygame.time.wait(1000)
    pygame.quit()
    sys.exit()


#gameover screen
def gameover(surface):
    surface.fill(RED)

    #gameover text in the center
    font = pygame.font.SysFont("centrury", 50)
    text = font.render(" GAME OVER ", True, BLACK)
    recttext = (surface.get_width()/2-text.get_width()/2, surface.get_height()/2)
    surface.blit(text, recttext)

#drawing counter of coins
def counter(surface, coincount):
    font = pygame.font.SysFont("centrury", 30)
    text = font.render(" Coins: {0}".format(coincount), True, BLACK, (255, 255, 255))
    recttext = text.get_rect(topleft = (width_screen-text.get_width(), 10))
    pygame.draw.rect(surface, RED, recttext, 2)
    surface.blit(text, recttext)


#screen parameters
width_screen = 500
height_screen = 600
screen = pygame.display.set_mode((width_screen, height_screen))
background = pygame.image.load(r"labka9\images2\infroad.png")
background2 = pygame.image.load(r"labka9\images2\infroad.png")

frameps = pygame.time.Clock()
FPS = 60
pygame.display.set_caption("Game Of The Year!!!!!!!")

#variables for infinite background
start_height = -1800
temp_height = start_height
speed = 2

#creating player and enemy and coin
player1 = Player()
enemy1 = Enemy(speed+1)
coin1 = Coin(speed)


#moving player and enemy into the screen
player1.draw(screen)
player1.rect.move_ip(width_screen/2-player1.width, height_screen/1.3)


#timer to make game harder after some time
timerspeed = 0
acceleration = 1

#timer to spawn enemies over time
timerenem = 0
limitenem = 400

coincounter = 0



#background music
pygame.mixer_music.load(r"labka9\songs2\Jumpsuit in D minor harmonic.mp3")
pygame.mixer_music.set_volume(0.5)

#code exeqution
while True:
    if pygame.mixer_music.get_busy() == False:
        pygame.mixer_music.play()
    timerspeed+=1
    timerenem+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #makeing evething faster after some time
    if timerspeed == 500:
        speed += 1
        enemy1.speed = speed+acceleration
        coin1.speed = speed
        limitenem -= 5
        timerspeed = 0

    #reseting timer for spawning new enemy
    if timerenem == limitenem:
        enemy1.draw(screen)
        timerenem = 0

    #the height of the background for the motion effect
    temp_height += speed
    if temp_height >= 600:
        temp_height = start_height


    screen.blit(background, (0, temp_height))
    screen.blit(background2, (0, temp_height-2400))

    iscollided_enem = player1.collision(enemy1)
    iscollided_coin = player1.collision(coin1)

    if iscollided_enem:
        gameover(screen)
    
    if iscollided_coin:
        if coin1.type == 1:
            coincounter+=1
        elif coin1.type == 2:
            coincounter+=2
        elif coin1.type == 3:
            coincounter+=5
        coin1.newcoin()
        coin1.rect.move_ip(0, 500)

        if coincounter%21 == 20:
            acceleration += 1

    player1.update()
    enemy1.update()
    coin1.update()


    player1.draw(screen)
    enemy1.draw(screen)
    coin1.draw(screen)

    counter(screen, coincounter)

    pygame.display.update()
    frameps.tick(FPS)

    if iscollided_enem:
        counter(screen, coincounter)
        exitgame()