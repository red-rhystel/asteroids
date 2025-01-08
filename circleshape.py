import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def collision_check(self, CircleShape):
        p1 = self.position
        p2 = CircleShape.position
        r1 = self.radius
        r2 = CircleShape.radius
        return p1.distance_to(p2) <= r1 + r2

    def update(self, dt):
        # sub-classes must override
        pass
