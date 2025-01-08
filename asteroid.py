import pygame
import random
from constants import *
from circleshape import CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # spawn two new asteroids
        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)

        new_ast_1 = Asteroid(self.position.x, self.position.y,
                             self.radius - ASTEROID_MIN_RADIUS)
        new_ast_2 = Asteroid(self.position.x, self.position.y,
                             self.radius - ASTEROID_MIN_RADIUS)

        new_ast_1.velocity = vector1 * 1.2
        new_ast_1.velocity.rotate(random_angle)
        new_ast_2.velocity = vector2 * 1.2
        new_ast_2.velocity.rotate(-random_angle)

