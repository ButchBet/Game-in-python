import pygame, sys
pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Time")

# Create the colors
yellow = pygame.Color(255, 180, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    time = pygame.time.get_ticks() // 1000
    print(time)
    surface.fill(yellow)
    pygame.display.update()
