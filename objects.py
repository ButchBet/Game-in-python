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


# Represent a rectangle
# Using class .Rect
rect = pygame.Rect(100, 150, 120, 60) # (x, y, width, height)
rect.center = (width // 2, height // 2) # (x//2, y//2) Using double / cause 
# need that return be integer number

# Using a tuple (We can't use atributes of the .Rect class)
rect2 = (100, 100, 80, 40)  # integers elements (x, y, width, height)

print(rect.y)
print(rect.x)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(white)
    # draw
    # 1. where to print it
    # 2. what's the color
    # 3. the figure
    pygame.draw.rect(surface, red, (100, 100, 80, 40))

    pygame.draw.circle(surface, green, (200, 300), 100) # (x, y), radius 

    pygame.draw.line(surface, blue, (100, 200), (200, 300), 2) # (a dot), (b dot), width
       
    pygame.display.update()