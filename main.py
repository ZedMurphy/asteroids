# this allows us to use code from
# the open-source pygame library
# throughout this file
# need to activate venv in ubuntu: source venv/bin/activate
# to run the game: python3 main.py

import pygame
import sys
from constants import *
from circleshape import *
from player import *
from shot import *
from asteroid import *
from asteroidfield import *


def main():
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))  # Call fill on the screen object
        for shape in drawable:
            shape.draw(screen)
        updateable.update(dt)
        for stone in asteroids:
            if stone.detect_collision(player):
                sys.exit("Game over!")
            for shot in shots:
                if shot.detect_collision(stone):
                    stone.split()
        pygame.display.flip()
        time = clock.tick(60)
        dt = time/1000



if __name__ == "__main__":
    main()
