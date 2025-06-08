import pygame

class Player:
    def __init__(self, x, y, radius):
        self.pos = pygame.Vector2(x, y)
        self.radius = radius
        self.color = "blue"
        # Hitbox: cria um quadrado que envolve o círculo
        self.hitbox = pygame.Rect(self.pos.x - radius, self.pos.y - radius, radius * 2, radius * 2)
    
    def update_hitbox(self):
        # Atualiza a hitbox com base na posição atual
        self.hitbox.topleft = (self.pos.x - self.radius, self.pos.y - self.radius)
    
    def draw(self, surface, debug=False):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)
        # Se quiser visualizar a hitbox para debug, pode desenhar assim:
        if debug:
            pygame.draw.rect(surface, "red", self.hitbox, 2)

    def move(self, dx, dy):
        self.pos.x += dx
        self.pos.y += dy
        self.update_hitbox()