import pygame
import time



pygame.init()

def blitRotate(image, pos, originPos, angle, cent):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = cent)

    # rotate and blit the image
    return (rotated_image, rotated_image_rect)


done = False
image = pygame.image.load(r"labka7\images\mickeynohands.png")
lefthand = pygame.image.load(r"labka7\images\lefthand.png")
righthand = pygame.image.load(r"labka7\images\righthand.png")

height = image.get_height()/2
width = image.get_width()/2
hl = lefthand.get_height()/2
wl = lefthand.get_width()/2
hr = righthand.get_height()/2
wr = righthand.get_width()/2

screen = pygame.display.set_mode((width, height))
image = pygame.transform.scale(image, (width, height))
lefthand = pygame.transform.scale(lefthand, (wl, hl))
righthand = pygame.transform.scale(righthand, (wr, hr))

originl = (width/2-wl/2-10, height/2-hl/2-10)
originr = (width/2-wr/2-10, height/2-hr/2-10)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #real time
    timenow = time.localtime()
    timemin = timenow.tm_min
    timesec = timenow.tm_sec
    #calculating rotation based on time
    degrmin = 3 * timemin * (-1) - 27
    degrsec = 3 * timesec * (-1) + 29

    #rotating
    lefthandnew = pygame.transform.rotate(lefthand, degrsec)
    righthandnew = pygame.transform.rotate(righthand, degrmin)

    #calculating position
    posl = (lefthandnew.get_width()/2, lefthandnew.get_width()/2)
    posr = (righthandnew.get_width()/2, righthandnew.get_width()/2)

    #applying rotation and position on left and right hands
    rotatedl = blitRotate(lefthandnew, originl, posl, degrsec, (width/2, height/2))
    rotatedr = blitRotate(righthandnew, originr, posr, degrmin, (width/2, height/2))

    screen.blit(image, (0,0))
    screen.blit(rotatedl[0], rotatedl[1])
    screen.blit(rotatedr[0], rotatedr[1])




    pygame.display.flip()
