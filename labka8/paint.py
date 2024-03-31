import pygame
import sys


# Class for drawing
class drawing(object):
 
    def __init__(self):
        self.color = (0, 0, 0)
        self.width = 10
        self.height = 10
        self.rad = 6
        self.tick = 0
        self.time = 0
        self.play = False
        self.mode = "draw"

    # Drawing Function with different modes
    def draw(self, screen, pos):
        if self.mode == "draw":
            pygame.draw.circle(screen, self.color, (pos[0], pos[1]), self.rad)

        elif self.mode == "rect":
            pygame.draw.rect(screen, self.color, 
                                pygame.rect.Rect(pos[0], pos[1], self.rad*2, self.rad*2),
                                self.rad)

        elif self.mode == "circ":
            pygame.draw.circle(screen, self.color, (pos[0], pos[1]),
                                self.rad*2, self.rad)

        if self.color == (255, 255, 255):
            pygame.draw.circle(screen, self.color, (pos[0], pos[1]), 20)
 
    # detecting clicks
    def click(self, screen, list, list2):
        pos = pygame.mouse.get_pos()  #getting position of mouse
 
        if pygame.mouse.get_pressed() == (1, 0, 0) and pos[0] < 400:
            if pos[1] > 25:
                self.draw(screen, pos)
        elif pygame.mouse.get_pressed() == (1, 0, 0):
            for button in list:
                if pos[0] > button.x and pos[0] < button.x + button.width:
                    if pos[1] > button.y and pos[1] < button.y + button.height:
                        self.color = button.color2
            for button in list2:
                if pos[0] > button.x and pos[0] < button.x + button.width:
                    if pos[1] > button.y and pos[1] < button.y + button.height:
                        if self.tick == 0:
                            if button.action == 1:
                                screen.fill((255, 255, 255))
                                self.tick += 1
                            if button.action == 2 and self.rad > 4:
                                self.rad -= 1
                                self.tick += 1
                                pygame.draw.rect(
                                    screen, (255, 255, 255), (410, 308, 80, 35))
 
                            if button.action == 3 and self.rad < 20:
                                self.rad += 1
                                self.tick += 1
                                pygame.draw.rect(
                                    screen, (255, 255, 255), (410, 308, 80, 35))
 
 
                            if button.action == 4:
                                self.tick +=1
                                self.mode = "rect"
                            if button.action == 5:
                                self.tick +=1
                                self.mode = "circ"
                            if button.action == 6:
                                self.tick +=1
                                self.mode = "draw"
                                pygame.draw.circle(screen, self.color, (pos[0], pos[1]),
                                                    self.rad, self.rad)
 
 
 


# Class for buttons
class button(object):
 
    def __init__(self, x, y, width, height, color, color2, outline=0, action=0, text=''):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.outline = outline
        self.color2 = color2
        self.action = action
        self.text = text

    # Class for drawing buttons
    def draw(self, screen):
 
        pygame.draw.rect(screen, self.color, (self.x, self.y,
                                           self.width, self.height), self.outline)
        font = pygame.font.SysFont('centrury', 30)
        text = font.render(self.text, 1, self.color2)
        pygame.draw.rect(screen, (255, 255, 255), (410, 446, 80, 35))
        screen.blit(text, (int(self.x+self.width/2-text.get_width()/2),
                        int(self.y+self.height/2-text.get_height()/2)))



def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()
    run = True
    while run: 
        keys = pygame.key.get_pressed()  
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
                sys.exit()
 
        draw(screen)
 
        if 0 < player1.tick < 40:
            player1.tick += 1
        else:
            player1.tick = 0
 
        if 0 < player1.time < 4001:
            player1.time += 1
        elif 4000 < player1.time < 4004:
            player1.time = 4009
        else:
            player1.time = 0
            player1.play = False
 
    
                
        
        pygame.display.flip()
        
        clock.tick(60)

 
def drawHeader(screen):
    # Drawing header space
    pygame.draw.rect(screen, (175, 171, 171), (0, 0, 500, 25))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 400, 25), 2)
    pygame.draw.rect(screen, (0, 0, 0), (400, 0, 100, 25), 2)
 
    # Printing header
    font = pygame.font.SysFont('centrury', 30)
 
    canvasText = font.render('Canvas', 1, (0, 0, 0))
    screen.blit(canvasText, (int(200 - canvasText.get_width() / 2),
                          int(26 / 2 - canvasText.get_height() / 2) + 2))
 
    toolsText = font.render('Tools', 1, (0, 0, 0))
    screen.blit(toolsText, (int(450 - toolsText.get_width() / 2),
                         int(26 / 2 - toolsText.get_height() / 2 + 2)))
 
 

def draw(screen):
    player1.click(screen, Buttons_color, Buttons_other)
 
    pygame.draw.rect(screen, (0, 0, 0), (1000, 0, 100, 500),
                     2)  # Drawing button space
    pygame.draw.rect(screen, (255, 255, 255), (1000, 0, 100, 500),)
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 400, 500),
                     2)  # Drawing canvas space
    drawHeader(screen)
 
    for button in Buttons_color:
        button.draw(screen)
 
    for button in Buttons_other:
        button.draw(screen)
 
    pygame.display.update()
 
 
# Defining color buttons
redButton = button(453, 30, 40, 40, (205, 30, 30), (205, 30, 30))
blueButton = button(407, 30, 40, 40, (40, 35, 225), (40, 35, 225))
greenButton = button(407, 76, 40, 40, (30, 185, 50), (30, 185, 50))
orangeButton = button(453, 76, 40, 40, (255, 192, 100), (255, 192, 100))
yellowButton = button(407, 122, 40, 40, (230, 225, 70), (230, 225, 70))
purpleButton = button(453, 122, 40, 40, (112, 78, 160), (112, 78, 160))
blackButton = button(407, 168, 40, 40, (45, 30, 65), (45, 30, 65))
whiteButton = button(453, 168, 40, 40, (5, 5, 5), (255, 255, 255), 1)
 
# Defining other buttons
clrButton = button(407, 214, 86, 40, (201, 201, 201), (0, 0, 0), 0, 1, 'Clear')
 
smallerButton = button(407, 260, 40, 40, (201, 201, 201), (0, 0, 0), 0, 2, '-')
biggerButton = button(453, 260, 40, 40, (201, 201, 201), (0, 0, 0), 0, 3, '+')

rectButton = button(407, 306, 40, 40, (201, 201, 201), (0, 0, 0), 0, 4, '[]')
circButton = button(453, 306, 40, 40, (201, 201, 201), (0, 0, 0), 0, 5, 'O')
drawButton = button(430, 352, 40, 40, (201, 201, 201), (0, 0, 0), 0, 6, '.')
 
Buttons_color = [blueButton, redButton, greenButton, orangeButton,
                 yellowButton, purpleButton, blackButton, whiteButton]
Buttons_other = [clrButton, smallerButton, biggerButton, rectButton, circButton, drawButton]
 
player1 = drawing()

main()