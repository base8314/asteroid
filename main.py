# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT }")
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    #Setting Resolution of screen
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    player= Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
    game_clock = pygame.time.Clock()
    field= AsteroidField()
    dt = 0
    running = True

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
        
        for asteroid in asteroids:
            if player.check_collisions(asteroid):
                print("Game over!")
                running = False
                break  # Exit the loop if a collision is detected

            for shot in shots:
                if shot.check_collisions(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        
        game_clock.tick(FPS)
        dt = game_clock.get_time()/1000

if __name__== "__main__":
    main()