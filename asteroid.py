import pygame
from circleshape import CircleShape

# Asteroid Class that inherits from CircleShape Class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Override method draw from CircleShape Class
    def draw(self, screen):
        # draw a white triangle on the screen
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # Method to update the asteroider movements
    def update(self, dt):
        self.position += self.velocity * dt