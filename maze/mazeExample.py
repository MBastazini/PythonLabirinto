import pygame
import random

# pygame setup
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Cores
BACKGROUND_COLOR = "white"
WALL_COLOR = "black"
PLAYER_COLOR = "blue"

# Maze wall class
class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

# Player class
class Player:
    def __init__(self, x, y, radius):
        self.pos = pygame.Vector2(x, y)
        self.radius = radius
        self.color = PLAYER_COLOR
        self.hitbox = pygame.Rect(self.pos.x - radius, self.pos.y - radius, radius * 2, radius * 2)

    def update_hitbox(self):
        self.hitbox.topleft = (self.pos.x - self.radius, self.pos.y - self.radius)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

    def move_to_cell(self, cell_x, cell_y, cell_width, cell_height):
        self.pos.x = cell_x * cell_width + cell_width // 2
        self.pos.y = cell_y * cell_height + cell_height // 2
        self.update_hitbox()

# Função para criar matriz vazia
def criaMatrizVazia(tamanho):
    return [[1 for _ in range(tamanho)] for _ in range(tamanho)]

# Função para desenhar o labirinto
def desenhe_labirinto(matriz, cell_width, cell_height):
    for y, row in enumerate(matriz):
        for x, cell in enumerate(row):
            if cell == 1:
                rect = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)
                pygame.draw.rect(screen, WALL_COLOR, rect)
            if cell == 2:
                # Desenha a saída do labirinto
                rect = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)
                pygame.draw.rect(screen, "green", rect)
            if cell == 3:
                # Desenha o caminho da saída
                rect = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)
                pygame.draw.rect(screen, "yellow", rect)

# Função para desenhar o player
def desenhe_player(player):
    player.draw(screen)

# Função recursiva que gera o labirinto e move o player
def geraLabirintoRecursivoVisual(matriz, x, y, player, cell_width, cell_height):
    direcoes = [(0, -2), (0, 2), (-2, 0), (2, 0)]  # cima, baixo, esquerda, direita
    random.shuffle(direcoes)
    count = 0
    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy

        # Move o player sempre que escolhe uma direção
        player.move_to_cell(nx, ny, cell_width, cell_height)

        # Desenha tudo
        screen.fill(BACKGROUND_COLOR)
        desenhe_labirinto(matriz, cell_width, cell_height)
        desenhe_player(player)
        pygame.display.flip()
        #pygame.time.delay(10)  # espera de 100ms para visualizar

        if 1 <= nx < len(matriz) - 1 and 1 <= ny < len(matriz) - 1:
            if matriz[ny][nx] == 1:
                matriz[y + dy // 2][x + dx // 2] = 0
                matriz[ny][nx] = 0
                geraLabirintoRecursivoVisual(matriz, nx, ny, player, cell_width, cell_height)
            else:
                count += 1
        else:
            count += 1
    if (count == 4):
        matriz[y][x] = 3
# Inicialização
tamanho = 51
matriz = criaMatrizVazia(tamanho)
start_x, start_y = 26, 26  # Começa no centro da matriz
matriz[start_y][start_x] = 2

cell_width = SCREEN_WIDTH // tamanho
cell_height = SCREEN_HEIGHT // tamanho

player = Player(start_x * cell_width + cell_width // 2, start_y * cell_height + cell_height // 2, cell_width // 3)

# Geração visual do labirinto
geraLabirintoRecursivoVisual(matriz, start_x, start_y, player, cell_width, cell_height)

# Loop principal para manter a janela aberta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    desenhe_labirinto(matriz, cell_width, cell_height)
    desenhe_player(player)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
