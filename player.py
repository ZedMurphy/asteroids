import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown -= dt

        if keys[pygame.K_a]:
            reversed_dt = 0 - dt
            self.rotate(reversed_dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            reversed_dt = 0 - dt
            self.move(reversed_dt)
        if keys[pygame.K_SPACE] and self.cooldown <= 0:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        new_shot = Shot(self.position[0],self.position[1], SHOT_RADIUS)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity += forward * PLAYER_SHOOT_SPEED
