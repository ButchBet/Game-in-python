import pygame, sys

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height)) # surface
pygame.display.set_caption("Key events")

# Create colors 
white = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)

# Creater the movement helpers
x = 175
y = 225
rect = pygame.Rect(x, y, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            surface.fill(white)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                y -= 10
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x -= 10
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += 10
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += 10
        rect = pygame.Rect(x, y, 50, 50)
        pygame.draw.rect(surface, red, rect)
        if event.type == pygame.KEYUP:
            ##print('Upushed key!')
            pass
    pygame.display.update()