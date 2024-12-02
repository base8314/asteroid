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
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)


    #Setting Resolution of screen
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    player= Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
    game_clock = pygame.time.Clock()
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Fill Screen With Black
        screen.fill((0,0,0))
        

        #update the display
        
        
        for updates in updatable:
            updates.update(dt)
        
        for drawings in drawable:
            drawings.draw(screen)
        
        pygame.display.flip()
        
        game_clock.tick(FPS)
        dt = game_clock.get_time()/1000

if __name__== "__main__":
    main()