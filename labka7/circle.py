import pygame

pygame.init()



w, h = 500, 500
screen = pygame.display.set_mode((w, h))
bg = (205, 200, 202)
screen.fill(bg)
rad = 25
done = False
coor = (250, 250)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        screen.fill(bg)
        
        new_coor = coor
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and coor[0]+20 < 475:
                new_coor = (coor[0]+20, coor[1])
            if event.key == pygame.K_LEFT and coor[0]-20 > 25:
                new_coor = (coor[0]-20, coor[1])
            if event.key == pygame.K_UP and coor[1]-20 > 25:
                new_coor = (coor[0], coor[1]-20)
            if event.key == pygame.K_DOWN and coor[1]+20 < 475:
                new_coor = (coor[0], coor[1]+20)

        pygame.draw.circle(screen, (240, 10, 40), new_coor, rad)
        coor = new_coor
    pygame.display.update()