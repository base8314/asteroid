# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT }")
    
    #Setting Resolution of screen
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Fill Screen With Black
        screen.fill((0,0,0))

        #update the display
        pygame.display.flip()


if __name__== "__main__":
    main()