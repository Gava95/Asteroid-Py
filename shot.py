import pygame
from constants import *
from circleshape import CircleShape

# Shot Class that inherits from CircleShape Class
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    # Override method draw from CircleShape Class
    def draw(self, screen):
        # draw a white circle on the screen
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # Method to update the bullet movements
    def update(self, dt):
        self.position += self.velocity * dt