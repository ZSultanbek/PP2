import pygame
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (20, 20, 40)

# paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound(r'labka9\songs2\(Untitled)break.mp3')

# Block settings
initial_block_count = 40  # Initial number of blocks
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for _ in range(initial_block_count)]

# Game over Screen
losefont = pygame.font.SysFont('impact', 40)
losetext = losefont.render('Game Over', True, (255, 30, 55))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('impact', 40)
wintext = losefont.render('You win GIVE ME MY 100 POINTS', True, (80, 60, 100))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

balltimer = 0
paused = False

# Button parameters
button_width = 200
button_height = 50
button_color = (100, 100, 100)
button_highlight_color = (150, 150, 150)
button_font = pygame.font.SysFont(None, 30)

def draw_button(surface, text, rect, button_color, text_color):
    pygame.draw.rect(surface, button_color, rect)
    pygame.draw.rect(surface, (0, 0, 0), rect, 2)
    text_surf = button_font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                append = 1
            elif event.button == 3:
                append = -1
            if paused:
                # Check if the buttons were clicked
                if ball_speed_button.collidepoint(mouse_pos):
                    ballSpeed += append
                elif paddle_speed_button.collidepoint(mouse_pos) and paddleSpeed > 1:
                    paddleSpeed += append
                elif ball_rad_button.collidepoint(mouse_pos) and paddleSpeed > 1:
                    ballRadius += append
                    ball_rect = int(ballRadius * 2 ** 0.5)
                    ball = pygame.Rect(ball.x, ball.y, ball_rect, ball_rect)
                    
                

    screen.fill(bg)

    if not paused:
        [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]  # drawing blocks
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx

        if ball.centery < ballRadius + 50:
            dy = -dy

        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)
            color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for _ in range(initial_block_count)]   
                

        hitIndex = ball.collidelist(block_list)

        if balltimer >= 5:
            ballSpeed += 1
            balltimer = 0

        if hitIndex != -1:
            hitRect = block_list.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
            
            #hitRect = block_list[hitIndex]
            #hitColor = color_list[hitIndex]
            #color_list[hitIndex] = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            balltimer += 1
            collision_sound.play()

        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)

        if ball.bottom > H:
            screen.fill((30, 10, 10))
            screen.blit(losetext, losetextRect)
        elif not len(block_list):
            screen.fill((255, 205, 225))
            screen.blit(wintext, wintextRect)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed
    else:
        # If paused, display a pause message
        pause_font = pygame.font.SysFont('impact', 60)
        pause_text = pause_font.render('Paused', True, (255, 255, 255))
        pause_rect = pause_text.get_rect(center=(W // 2, H // 2))
        screen.blit(pause_text, pause_rect)

        
        button_y = H // 2 - 300
        info = pygame.Rect(W // 2 - (button_width+300) // 2, button_y, button_width+300, button_height)
        draw_button(screen, f"To increase LEFTCLICK of mouse, to decrease RIGHTCLICK of mouse ", info, button_color, (255, 255, 255))

        # Draw settings buttons
        button_y = H // 2 - 100
        ball_speed_button = pygame.Rect(W // 4 - button_width // 2, button_y, button_width, button_height)
        draw_button(screen, f"Change Ball Speed ({ballSpeed + 1})", ball_speed_button, button_color, (255, 255, 255))

        button_y += 100
        paddle_speed_button = pygame.Rect(W // 4 - button_width // 2, button_y, button_width, button_height)
        draw_button(screen, f"Change Paddle Speed ({paddleSpeed - 1})", paddle_speed_button, button_color, (255, 255, 255))
        
        button_y += 100
        ball_rad_button = pygame.Rect(W // 4 - button_width // 2, button_y, button_width, button_height)
        draw_button(screen, f"CHange Ball Size ({ballRadius - 1})", ball_rad_button, button_color, (255, 255, 255))


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
