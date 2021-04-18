import sys
import pygame
pygame.init()

width = 400
height = 500
surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption('Pygame')

## Working with the colors
## Using a class .Color
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
# Using a tuple
my_color = (200, 90, 130)

surface2 = pygame.Surface((200, 200)) # (width, height)
surface2.fill(green)

rect = surface2.get_rect()
rect.center = (width // 2, height // 2)
print(rect.x)
print(rect.y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(white)

    surface.blit(surface2, rect)

    pygame.draw.rect(surface2, red, (100, 50, 80, 40))

    pygame.display.update()