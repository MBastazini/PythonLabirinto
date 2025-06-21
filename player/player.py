import pygame
import time

class Player:
    def __init__(self, x, y, radius):
        self.pos = pygame.Vector2(x, y)
        self.radius = radius
        self.base_color = "blue"
        self.color = self.base_color
        self.hitbox = pygame.Rect(self.pos.x - radius, self.pos.y - radius, radius * 2, radius * 2)
        self.points = 0
        self.color_timer = None  # Armazena o tempo em que a cor deve voltar ao normal

    def update_hitbox(self):
        self.hitbox.topleft = (self.pos.x - self.radius, self.pos.y - self.radius)

    def draw(self, surface, debug=False):
        # Verifica se o tempo de "efeito colorido" acabou
        if self.color_timer and pygame.time.get_ticks() >= self.color_timer:
            self.color = self.base_color
            self.color_timer = None

        pygame.draw.circle(surface, self.color, self.pos, self.radius)
        if debug:
            pygame.draw.rect(surface, "red", self.hitbox, 2)

    def move(self, dx, dy):
        self.pos.x += dx
        self.pos.y += dy
        self.update_hitbox()

    def bonusSquare(self):
        self.points += 10
        self.color = "yellow"
        self.color_timer = pygame.time.get_ticks() + 500  # 0,5 segundo no futuro (1000 milissegundos)
