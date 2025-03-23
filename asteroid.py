import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20.0, 50.0)
            new_rotation_1 = pygame.Vector2(self.velocity[0], self.velocity[1]).rotate(random_angle)
            new_rotation_2 = pygame.Vector2(self.velocity[0], self.velocity[1]).rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child_1 = Asteroid(self.position[0], self.position[1], new_radius)
            child_2 = Asteroid(self.position[0], self.position[1], new_radius)
            child_1.velocity = new_rotation_1 * 1.2
            child_2.velocity = new_rotation_2 * 1.2

        