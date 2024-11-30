# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT }")
    
    #Setting Resolution of screen
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    
    game_clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Fill Screen With Black
        screen.fill((0,0,0))
        player= Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)

        #update the display
        player.draw(screen)
        pygame.display.flip()
        
        game_clock.tick(FPS)
        dt = game_clock.get_time()/1000

if __name__== "__main__":
    main()