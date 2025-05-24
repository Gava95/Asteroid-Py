import pygame
from constants import *
from circleshape import CircleShape

# Player Class that inherits from CircleShape Class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # method to draw a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Override method draw from CircleShape Class
    def draw(self, screen):
        # draw a white triangle on the screen
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # Method to make the player rotate on himself
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # Method to make the player move
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # Method to update the player movements when a key is press
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Press A or LEFT arrow
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt) # player rotate on himself on the left
        
        # Press D or RIGHT arrow
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt) # player rotate on himself on the right

        # Press W or UP arrow
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt) # player move up

        # Press S or DOWN arrow
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt) # player move down