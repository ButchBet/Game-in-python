import pygame, sys
pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height)) # surface
pygame.display.set_caption("Pressed")

# Create colors 
white = pygame.Color(255, 255, 255)
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
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            y -= 10
            print("Up")
        if pressed[pygame.K_a]:
            x -= 10
            print("Left")
        if pressed[pygame.K_s]:
            y += 10
            print("Down")
        if pressed[pygame.K_d]:
            x += 10
            print("Right")
        rect = pygame.Rect(x, y, 50, 50)
        pygame.draw.rect(surface, red, rect)
    pygame.display.update()