import pygame
pygame.init()

NEXT = pygame.USEREVENT
songstart = 1
index = songstart-2
psmode=True
listofsongs = [r"labka7\songs\Stop My Plans.mp3", r"labka7\songs\Run Away.mp3",
               r"labka7\songs\In My Bathroom.mp3", r"labka7\songs\Jumpsuit in D minor harmonic.mp3",
               r"labka7\songs\InnerSide.mp3"]

listofnames = []
for i in listofsongs:
    listofnames.append( i[13:-4] )
#listofnames = ["Stop My Plans", "Run Away", "In My Bathroom", "Jumpsuit in D minor harmonic"]
    
def pause():
    global psmode
    if psmode==True:
        pygame.mixer.music.pause()
        psmode=False
    else:
        pygame.mixer.music.unpause()
        psmode=True 
    poss = pygame.mixer_music.get_pos()/1000
    new_poss = poss-2
    if new_poss < 0:
        new_poss = 0
    pygame.mixer.music.set_pos(new_poss)    

def nextsong(num = 1):
    global index, listofsongs, psmode
    pygame.mixer_music.unload()
    index += num
    if index >= len(listofsongs):
        index = len(listofsongs)-1
    if index < 0:
        index = 0
    pygame.mixer_music.load(listofsongs[index])

    if pygame.mixer.get_busy() == False:
        pygame.mixer_music.play()
        pygame.mixer_music.pause()
    if psmode == True:
        pygame.mixer_music.play()
    else:
        pygame.mixer_music.pause()

nextsong()

screen = pygame.display.set_mode((400, 300))
done = False
white = (255,255,255)


font = pygame.font.SysFont("centrury", 30)
text2=font.render(" PAUSE ", True, white)
text3=font.render(" NEXT ", True, white)
text4=font.render(" BACK ", True, white)

rect2 = text2.get_rect(topleft= (170,250))
rect3 = text3.get_rect(topleft= (280,260))
rect4 = text4.get_rect(topleft= (70,260))

bg = (127,100,127)
pygame.mixer.music.set_endevent(NEXT) 
screen = pygame.display.set_mode((400,300))
while not done:
    for event in pygame.event.get():
        screen.fill(bg)

        if psmode == True:
            pausecolor = (50, 250, 110)
        else:
            pausecolor = (255,30,110)
        screen.blit(text2, rect2)
        pygame.draw.rect(screen, pausecolor,rect2,2)
        pygame.draw.rect(screen, (255,0,0),rect3,2)
        screen.blit(text3, rect3)
        pygame.draw.rect(screen, (255,0,0),rect4,2)
        screen.blit(text4, rect4)
        textname = font.render(" {0} ".format(listofnames[index]), False, white, (0, 0, 0))
        rectname = textname.get_rect(topleft= (120, 80))   
        screen.blit(textname, rectname)

        if event.type == pygame.QUIT:
            done = True

            
        if event.type == NEXT:
            nextsong()
    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause()
            
            if event.key == pygame.K_RIGHT:
                nextsong()

            if event.key == pygame.K_LEFT:
                nextsong(-1)

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect2.collidepoint(event.pos):
                pause()
            if rect3.collidepoint(event.pos):
                nextsong()
            if rect4.collidepoint(event.pos):
                nextsong(-1)
    pygame.display.update()