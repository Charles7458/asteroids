import pygame
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        else:
            rand_angle = random.uniform(20, 50) # random angle between 20 & 50
            
            vector1 = self.velocity.rotate(rand_angle) # generating two new velocities using current asteroids velocity vector()
            vector2 = self.velocity.rotate( -rand_angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            new_asteroid_1.velocity = vector1 * 1.2
            new_asteroid_2.velocity = vector2 * 1.2