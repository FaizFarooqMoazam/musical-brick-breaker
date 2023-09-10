import pygame
import sys
import os
os.listdir()
# some comment

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
rows = 9
columns = 8

SCREENCOLOR = (10, 10, 30)
BALL = (30, 0, 255)
RED = (201, 5, 245)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game")

# Ball properties
ball_radius = 12
ball_speed = [5, 5]  # x and y direction speeds

# Paddle properties
paddle_width = 160
paddle_height = 25  
paddle_speed = 12
paddle_x = (SCREEN_WIDTH - paddle_width) // 2
paddle_y = SCREEN_HEIGHT - paddle_height - 8

# Brick properties
brick_width = SCREEN_WIDTH // columns
brick_height = 20  
brick_color = (146, 62, 230)  

#sounds
#hitsound = pygame.mixer.Sound("gameballtap.wav")

bricks = []
for row in range(rows):
    for col in range(columns):
        brick_x = col * brick_width
        brick_y = row * brick_height
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        bricks.append(brick)

def draw_bricks():
    for brick in bricks:
        pygame.draw.rect(screen, brick_color, brick)
        pygame.draw.rect(screen, SCREENCOLOR, brick, 2)

def break_brick():
    global ball_speed, count
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed[1] = -ball_speed[1]
            count += 1
            print('Score:', count)
#            hitsound.play()
count = 0

ball = pygame.Rect(SCREEN_WIDTH // 2 - ball_radius, SCREEN_HEIGHT // 2 - ball_radius, ball_radius * 2, ball_radius * 2)
paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

while True:
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        paddle.x -= paddle_speed
    if key[pygame.K_RIGHT]:
        paddle.x += paddle_speed
    if key[pygame.K_UP]:
        paddle.y -= paddle_speed
    if key[pygame.K_DOWN]:
        paddle.y += paddle_speed

    ball.x -= ball_speed[0]
    ball.y += ball_speed[1]

    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    break_brick()

    if ball.bottom >= SCREEN_HEIGHT:
        print("GAME OVER => tough luck")
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(SCREENCOLOR)

    draw_bricks() 
    pygame.draw.circle(screen, BALL, ball.center, ball_radius)
    pygame.draw.rect(screen, RED, paddle)

    pygame.display.flip()

    pygame.time.Clock().tick(100)

