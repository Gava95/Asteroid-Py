import pygame
import random
from constants import *
from circleshape import CircleShape

# Asteroid Class that inherits from CircleShape Class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Override method draw from CircleShape Class
    def draw(self, screen):
        # draw a white circle on the screen
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # Method to update the asteroid movements
    def update(self, dt):
        self.position += self.velocity * dt

    # Method to split the asteroid
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # randomize the angle of the split between 20 and 50 degres
        angle = random.uniform(20, 50)

        # Vector for new asteroids
        vector_asteroid_1 = self.velocity.rotate(angle)
        vector_asteroid_2 = self.velocity.rotate(-angle)

        new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS

        # 2 Asteroids Object with new radius, independant trajectory vector and a velocity boost
        asteroid = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        asteroid.velocity = vector_asteroid_1 * 1.2

        asteroid = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        asteroid.velocity = vector_asteroid_2 * 1.2