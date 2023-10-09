import pygame
import random
import os
os.chdir('C:\\Users\\Hugo\\github\\crocodile-game')

# Initialize pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 300
FLOOR_Y = HEIGHT - 30
CROC_Y = FLOOR_Y - 20
SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crocodile Game')

# Load crocodile and obstacle (cactus) images
# NOTE: You'll need to provide your own images or draw shapes instead
croc_image = pygame.image.load('C:\\Users\\Hugo\\github\\crocodile-game\\crocodile.png')
croc_rect = croc_image.get_rect(topleft=(50, CROC_Y))
poop_image = pygame.image.load('C:\\Users\\Hugo\\github\\crocodile-game\\poop.png')
poop_rect = poop_image.get_rect(topleft=(WIDTH, CROC_Y))

jump = False
jump_height = 10
jump_count = 10
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jump:
                jump = True

    if jump:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            poop_rect.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jump = False
            jump_count = 10

    screen.blit(croc_image, croc_rect)

    poop_rect.x -= SPEED
    if poop_rect.x < -poop_rect.width:
        poop_rect.x = WIDTH
        poop_rect.y = CROC_Y - random.randint(0, 30)
    screen.blit(poop_image, poop_rect)

    if croc_rect.colliderect(poop_rect):
        running = False

    pygame.draw.line(screen, BLACK, (0, FLOOR_Y), (WIDTH, FLOOR_Y))
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
