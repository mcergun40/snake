#! /usr/bin/python

import pygame, sys

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
fps = pygame.time.Clock()

# main loop
while True:
    surface.fill(blue)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(60)