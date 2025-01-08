# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # initialize pygame modules
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # create groups to hold our objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # add class variables to put classes in groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    # create a screen object to display the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # create a clock object to manage game speed
    clock = pygame.time.Clock()
    dt = 0
    # create a player object
    player = Player(SCREEN_WIDTH / 2,
                    SCREEN_HEIGHT / 2)
    # create the asteroid field
    asteroidfield = AsteroidField()
    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update objects before they're drawn
        for obj in updatable:
            obj.update(dt)
        # check if any asteroids have collided with the player
        for obj in asteroids:
            for shot in shots:
                if shot.collision_check(obj):
                    shot.kill()
                    obj.split()
            if obj.collision_check(player):
                print("Game over!")
                sys.exit()

        # fill the screen with the color black
        screen.fill("black")
        # draw all objects in drawable
        for obj in drawable:
            obj.draw(screen)
        # refresh the screen
        pygame.display.flip()
        
        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
