import pygame
import sys
import random

pygame.init()

#predefined variables
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

frameps = pygame.time.Clock()
FPS = 15


#predefined colors
BLACK = (0, 20, 10)
RED = (255, 10, 40)
GREEN = (20, 255, 30)
BLUE = (30, 35, 255)
ORANGE1 = (195, 200, 120)
ORANGE2 = (205, 75, 100)
ORANGE3 = (255, 0, 30)
GREY = (30, 30, 40)
LIGHTGREY = (90, 90, 110)


#number of apples and timerr of apples
apples = 0
aptimer = 0
wallwidth = 10
level = 1
walltimer = 0

#classes for the player and apples
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = BLUE
        self.w = 10
        self.h = 10
        self.rectblock = pygame.rect.Rect(WIDTH/2, HEIGHT/2, self.w, self.h)
        self.direction = [0, 0]
        self.lastdir = [0, 0]

        self.body = [self.rectblock] 

        self.isdead = False

    def update(self, event):
        

        self.lastdir = self.direction

        #getting direction
        if event.key == pygame.K_RIGHT:
            self.direction = [self.w, 0]
        elif event.key == pygame.K_UP:
            self.direction = [0, -self.h]
        elif event.key == pygame.K_DOWN:
            self.direction = [0, self.h]
        elif event.key == pygame.K_LEFT:
            self.direction = [-self.w, 0]

        backwords = [(-1) * self.direction[0], self.direction[1] * (-1)]
        #making sure the player doesnt' go backwords
        if self.lastdir == backwords:
            self.direction = self.lastdir

        
    def move(self):

        #moving all parts of snake
        for i in range(len(self.body)):
            x1 = (self.body[i].x + self.direction[0])
            y1 = (self.body[i].y + self.direction[1])

        #deleting old parts
        if len(self.body) > apples:
            del self.body[0]

        #defining head of the snake and appending list of snakes body
        head = pygame.rect.Rect(x1, y1, 10, 10)
        self.body.append(head)

        #checking if the possition of the head is the same as other parts, if so snake is dead
        for i in self.body[:-2]:
            if i == head:
                self.isdead = True


        #check if out of bound and kill iff yes
        if self.body[-1].left < wallwidth:
            self.isdead = True
        elif self.body[-1].right > WIDTH-wallwidth:
            self.isdead = True
        elif self.body[-1].bottom > HEIGHT-wallwidth:
            self.isdead = True
        elif self.body[-1].top < wallwidth:
            self.isdead = True


    def draw(self, surface):
        for one in self.body:
            pygame.draw.rect(surface, self.color, one)

    

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ORANGE = ORANGE1
        self.color = ORANGE
        self.type = 1

    def update(self):
        #choosing random coordinates but it wont land on the player
        self.listx = [i for i in range(wallwidth+30, WIDTH-wallwidth-30, 10) if i not in [j.x for j in p1.body]]
        self.listy = [i for i in range(wallwidth+30, HEIGHT-wallwidth-30, 10) if i not in [j.y for j in p1.body]]
        self.listx1 = self.listx
        self.listy1 = self.listy
        if len(self.listx) == 0:
            self.listx1 = [i for i in range(wallwidth, WIDTH-wallwidth, 10) if i not in [j.x for j in p1.body]]
        if len(self.listy) == 0:
            self.listy1 = [i for i in range(wallwidth, WIDTH-wallwidth, 10) if i not in [j.y for j in p1.body]]
        self.x = round(random.choice(self.listx1))
        self.y = round(random.choice(self.listy1))

        self.rect = pygame.rect.Rect(self.x, self.y, 10, 10)

        #making new random apple
        rand = random.randint(1, 3)

        if rand == 1:
            self.color = ORANGE1
            self.type = 1
        elif rand == 2:
            self.color = ORANGE2
            self.type = 2
        elif rand == 3:
            self.color = ORANGE3
            self.type = 3

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class disApple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ORANGE = ORANGE1
        self.color = ORANGE
        self.type = 1
        self.colorchange = 2
        self.timer = 100
    
    def dissapear(self):
        if self.timer >= 0:
            #changing color with time
            color1 = [self.color[0], self.color[1], self.color[2]]
            clrtime = self.timer%5
            if clrtime <= 40:
                color1 = [color1[0]-self.colorchange, color1[1]-self.colorchange,color1[2]-self.colorchange]

        for i in range(3):
            if color1[i] < 0:
                color1[i] = 0


        color2 = (color1[0], color1[1], color1[2])
        self.color = color2

    def update(self):
        self.timer = 100
        #choosing random coordinates but it wont land on the player
        self.listx = [i for i in range(wallwidth+30, WIDTH-wallwidth-30, 10) if i not in [j.x for j in p1.body]]
        self.listy = [i for i in range(wallwidth+30, HEIGHT-wallwidth-30, 10) if i not in [j.y for j in p1.body]]
        self.listx1 = self.listx
        self.listy1 = self.listy
        if len(self.listx) == 0:
            self.listx1 = [i for i in range(wallwidth, WIDTH-wallwidth, 10) if i not in [j.x for j in p1.body]]
        if len(self.listy) == 0:
            self.listy1 = [i for i in range(wallwidth, WIDTH-wallwidth, 10) if i not in [j.y for j in p1.body]]
        self.x = round(random.choice(self.listx1))
        self.y = round(random.choice(self.listy1))

        self.rect = pygame.rect.Rect(self.x, self.y, 10, 10)

        #making new random apple
        rand = random.randint(1, 3)

        if rand == 1:
            self.color = ORANGE1
            self.type = 1
        elif rand == 2:
            self.color = ORANGE2
            self.type = 2
        elif rand == 3:
            self.color = ORANGE3
            self.type = 3

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)




#exit the game
def exitgame():
    #pausing game before exiting
    pygame.time.wait(1000)
    pygame.quit()
    sys.exit()


#gameover screen
def gameover(surface):
    if apples <= 50:
        surface.fill(RED)
    else:
        surface.fill(GREEN)
    #gameover text in the center
    font = pygame.font.SysFont("centrury", 50)
    text = font.render(" GAME OVER ", True, BLACK)
    recttext = (surface.get_width()/2-text.get_width()/2, surface.get_height()/2)
    surface.blit(text, recttext)

#drawing counter of apples and levels
def counterlvl(surface, count, height):
    font = pygame.font.SysFont("centrury", 20)
    text = font.render(" Level: {0}".format(count), True, BLACK, (220, 230, 255))
    recttext = text.get_rect(topleft = (WIDTH-text.get_width(), height))
    pygame.draw.rect(surface, RED, recttext, 2)
    surface.blit(text, recttext)
def counterscr(surface, count, height):
    font = pygame.font.SysFont("centrury", 20)
    text = font.render(" Score: {0}".format(count), True, BLACK, (220, 230, 255))
    recttext = text.get_rect(topleft = (WIDTH-text.get_width(), height))
    pygame.draw.rect(surface, RED, recttext, 2)
    surface.blit(text, recttext)


screen.fill(GREY)


#initilizing objects
p1 = Snake()
ap1 = Apple()
ap1.update()
disap1 = disApple()
disap1.update()


while True:
    p1.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            p1.update(event)



    screen.fill(GREY)
    pygame.draw.rect(screen, LIGHTGREY, pygame.rect.Rect(0, 0, WIDTH, HEIGHT), wallwidth)
    

    if p1.isdead:
        gameover(screen)

    #check collision to detect if player got apple 
    apcol = pygame.Rect.colliderect(p1.body[-1], ap1.rect)
    disapcol = pygame.Rect.colliderect(p1.body[-1], disap1.rect)
    if apcol or disapcol:

        
        if apcol:
            if ap1.type == 1:
                apples+=1
                walltimer+=1
            if ap1.type == 2:
                apples+=2
                walltimer+=2
            if ap1.type == 3:
                apples+=5
                walltimer+=5
            ap1.update()
        if disapcol:
            if disap1.type == 1:
                apples+=1
                walltimer+=1
            if disap1.type == 2:
                apples+=2
                walltimer+=2
            if disap1.type == 3:
                apples+=5
                walltimer+=5
            disap1.update()
        #speeding up game after some apples
        if walltimer >= 5:    
            FPS += 2
            level += 1
            if len(ap1.listx) > 1 or len(ap1.listy) > 1:
                wallwidth += 10
            walltimer = walltimer-5
            
    counterlvl(screen, level, 0)
    counterscr(screen, apples, 15)



    p1.draw(screen)
    ap1.draw(screen)
    disap1.draw(screen)

    if disap1.timer <= 0:
        disap1.timer = 100
        disap1.update()
    disap1.dissapear()
    disap1.timer-=1

    pygame.display.update()
    frameps.tick(FPS)
    

    if p1.isdead:
        exitgame()