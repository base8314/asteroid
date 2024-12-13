from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, asteroid_RADIUS):
         super().__init__(x,y,asteroid_RADIUS)
         self.radius = asteroid_RADIUS
    
    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        new_velocity_1 = self.velocity.rotate (random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity =1.2* new_velocity_1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = 1.2* new_velocity_2