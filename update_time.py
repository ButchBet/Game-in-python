import pygame, sys

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height)) # surface
pygame.display.set_caption("Update_time")

# Create colors 
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blude = pygame.Color(0, 0, 255)

# Create the text font
font = pygame.font.SysFont("freesansbold.ttf", 48)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(green)
    time = pygame.time.get_ticks() // 1000 #the time in seconds
    text = font.render(str(time), True, red)
    rect = text.get_rect()
    rect.center = (15, 15)
    surface.blit(text, rect)
    pygame.display.update()