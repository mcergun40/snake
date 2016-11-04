#! /usr/bin/python

import pygame, sys, time

print "Hello Python Game!"


aqua        = (  0, 255, 255 )
black       = (  0,   0,   0 )
blue        = (  0,   0, 255 )
fuchsia     = (255,   0, 255 )
gray        = (128, 128, 128 )
green       = (  0, 128,   0 )
lime        = (  0, 255,   0 )
maroon      = (128,   0,   0 )
navy_blue   = (  0,   0, 128 )
olive       = (128, 128,   0 )
purple      = (128,   0, 128 )
red         = (255,   0,   0 )
silver      = (192, 192, 192 )
teal        = (  0, 128, 128 )
white       = (255, 255, 255 )
yellow      = (255, 255,   0 )

# initialize snake
pygame.init()

window_size = (800, 640)
surface = pygame.display.set_mode(window_size)
pygame.display.set_caption("Snake")

# set frame per seconds
fps = pygame.time.Clock()

# Load sounds
sound_crash = pygame.mixer.Sound("boom.wav")

x = y = 100
speed_x = speed_y = 0
step_x = step_y = 0
barier_x = barier_y = 320

STEP = 3

# main loop
while True:
    surface.fill(black)
    pygame.draw.rect(surface, red, (320, 320, 30, 30))
    
    for event in pygame.event.get():
        #print event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and not step_y:
                step_y = STEP
                step_x = 0
            elif event.key == pygame.K_UP and not step_y:
                step_y = -STEP
                step_x = 0
            elif event.key == pygame.K_RIGHT  and not step_x:
                step_x = STEP
                step_y = 0
            elif event.key == pygame.K_LEFT  and not step_x:
                step_x = -STEP
                step_y = 0
        elif event.type == pygame.KEYUP:
            #speed_x = 0
            #speed_y = 0
            pass

    x += step_x
    y += step_y

    pygame.draw.rect(surface, green, (x, y, 20, 20))
    
    if (x < barier_x + 30 and x + 20 > barier_x) and (y < barier_y + 30 and y + 20 > barier_y):
        print "CRASH!!!!!!!!!!!"
        sound_crash.play()
        time.sleep(1)
        break
        
    pygame.display.update()
    fps.tick(60)