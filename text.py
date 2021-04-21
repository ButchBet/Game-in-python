import sys
import pygame
pygame.init()

width = 400
height = 500
surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption('Text')

## Working with the colors
## Using a class .Color
red = pygame.Color(255, 180, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)

# 1. Get a font
font = pygame.font.SysFont("freesansbold", 48)

# 2. Create the text 
text = font.render('Oh! my bemo-baby', True, red) # --> surfice
rect = text.get_rect()
rect.center = (width // 2, height // 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(white)
    surface.blit(text, rect)
    pygame.display.update()