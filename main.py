# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

    # Group updatable, drawable, asteroids and shots
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Group asteroids, updatable and drawable are Asteroid containers
    Asteroid.containers = (asteroids, updatable, drawable)

    # Group shots, updatable and drawable are Shot containers
    Shot.containers = (shots, updatable, drawable)

    # Group updatable is Asteroid containers
    AsteroidField.containers = (updatable)

    # Object AsteroidField
    asteroidfield = AsteroidField()

    # Group updatable and drawable are Player containers
    Player.containers = (updatable, drawable)

    # Object Player (player draw in the middle of the screen) 
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Delta
    dt = 0

    while True:
        # Wait for the user to click on the red cross to quit the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)    # update movements of all updatable objects

        # Iterate over all the asteroids to check if one of them collided with player
        for asteroid in asteroids:   
            collided = asteroid.collisions(player)
            # If a collision is detected we exit the programm
            if collided == True:
                print("Game over!")
                sys.exit()
        
            # Iterate over all the shot to check if one of them collided with asteroids
            for shot in shots:
                collided = asteroid.collisions(shot)
                # If a collision is detected
                if collided == True:
                    shot.kill()         # Shot that collided with asteroid is remove
                    asteroid.split()    # Large asteroid is split into two small one / Small asteroid is remove

        screen.fill("black")    # Render the screen black

        for obj in drawable:    # draw all drawable objects
            obj.draw(screen)
        
        pygame.display.flip()   # Refresh the screen

        # Limit the FPS to a maximun threshold to avoid the overused of CPU
        dt = clock.tick(MAX_FPS_RATE)/1000      # convert the delta from ms to s
    
if __name__ == "__main__":
    main()
