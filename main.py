# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    # initialize pygame modules
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # create groups to hold our objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # add a class variable to put Player classes in groups
    Player.containers = (updatable, drawable)
    # create a screen object to display the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # create a clock object to manage game speed
    clock = pygame.time.Clock()
    dt = 0
    # create a player object
    player = Player(SCREEN_WIDTH / 2,
                    SCREEN_HEIGHT / 2)
    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill the screen with the color black
        screen.fill("black")
        # update/draw all objects in updatable/drawable
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        # refresh the screen
        pygame.display.flip()
        
        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
