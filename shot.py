import pygame
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y,shot_radius):
        super().__init__(x,y,shot_radius)
        self.radius = shot_radius
     
        self.velocity
    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius)

    def update(self,dt):
        self.position += (self.velocity * dt)