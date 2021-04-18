import sys
import pygame
pygame.init()

width = 400
height = 500
surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption('Pygame')

## Working with the colors
## Using a class .Color
red = pygame.Color(255, 180, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
# Using a tuple
my_color = (200, 90, 130)

stare = pygame.image.load('images/stare.png') # surface
rect = stare.get_rect()
rect.center = (width // 2, height // 2)

runing = pygame.image.load('images/run.png')
rectangle = pygame.image.load('images/rectangle.png') 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(red)
    surface.blit(runing, (100, 100))
    surface.blit(stare, rect)
    
    #surface.blit(rectangle, (0, 0))
    pygame.display.update()