# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Initiliaze pygame package
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Clock
    clock = pygame.time.Clock()

    # Group updatable & drawable
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Group updatable and drawable are Player containers
    Player.containers = (updatable, drawable)

    # Group asteroids, updatable and drawable are Asteroid containers
    Asteroid.containers = (asteroids, updatable, drawable)

    # Group asteroids, updatable and drawable are Asteroid containers
    AsteroidField.containers = (updatable)

    # Object Player (player draw in the middle of the screen) 
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Object AsteroidField
    asteroidfield = AsteroidField()

    # Delta
    dt = 0

    while True:
        # Wait for the user to click on the red cross to quit the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)    # update movements of all updatable objects
        screen.fill("black")    # Render the screen black

        for obj in drawable:    # draw all drawable objects
            obj.draw(screen)
        
        pygame.display.flip()   # Refresh the screen

        # Limit the FPS to a maximun threshold to avoid the overused of CPU
        dt = clock.tick(MAX_FPS_RATE)/1000      # convert the delta from ms to s
    
if __name__ == "__main__":
    main()
