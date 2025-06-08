import pygame

class Wall:
    def __init__(self, x, y, width, height, color="black", active=True, type="wall"):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.active = active  # If the wall is active or not, used for collision detection
        self.type = type