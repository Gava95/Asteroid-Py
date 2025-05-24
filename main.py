# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # Initiliaze pygame package
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Clock & Delta object
    clock = pygame.time.Clock()
    dt = 0

    while True:
        pygame.Surface.fill(screen, (0,0,0)) # Render a black screen
        pygame.display.flip() # Refresh the screen

        # Wait for the user to clck on the red cross to quit the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
    # Set the FPS to a maximun threshold to avoid the overused of CPU
    max_tick = clock.tick(MAX_FPS_RATE)
    
    dt = max_tick/1000 # convert the delta from ms to s
    
if __name__ == "__main__":
    main()
