import pygame, sys

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height)) # surface
pygame.display.set_caption("Sound")

# Create colors 
white = pygame.Color(0, 0, 0)

# Creating sound
pygame.mixer.music.load('sounds/Survivor - Eye Of The Tiger (Official HD Video).mp3')
pygame.mixer.music.set_volume(1.0) # 0.0 --> 1.0
pygame.mixer.music.play() # (times, from)

# Different mixer.music built in functions 
#pygame.mixer.music.rewind()
#pygame.mixer.music.pause()
#pyagme.mixer.music.stop()
#pygame.mixer.music.fadeout(30000)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(white)
    pygame.display.update()