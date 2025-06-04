# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

#Maze wall class
class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

#Player class
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
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)
        # Se quiser visualizar a hitbox para debug, pode desenhar assim:
        # pygame.draw.rect(surface, "red", self.hitbox, 2)

    def move(self, dx, dy):
        self.pos.x += dx
        self.pos.y += dy
        self.update_hitbox()

def criaMatrizVazia(tamanho):
    return [[1 for _ in range(tamanho)] for _ in range(tamanho)]

def geraLabirintoRecursivo(matriz, x, y):
    direcoes = [(0, -2), (0, 2), (-2, 0), (2, 0)]  # cima, baixo, esquerda, direita
    random.shuffle(direcoes)

    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy

        # Verifica se a célula vizinha está dentro dos limites e é uma parede
        if 1 <= nx < len(matriz) - 1 and 1 <= ny < len(matriz) - 1:
            if matriz[ny][nx] == 1:
                # Remove parede entre as células
                matriz[y + dy // 2][x + dx // 2] = 0
                # Marca a nova célula como caminho
                matriz[ny][nx] = 0
                # Continua recursivamente
                geraLabirintoRecursivo(matriz, nx, ny)

def geraLabirinto(tamanho):
    matriz = criaMatrizVazia(tamanho)
    # Começa de uma posição ímpar (ex.: (1,1))
    start_x, start_y = 1, 1
    matriz[start_y][start_x] = 0
    geraLabirintoRecursivo(matriz, start_x, start_y)
    return matriz

matriz = geraLabirinto(21)

mazeHitbox = []
# draw walls based on the matrix
wall_width = SCREEN_WIDTH // len(matriz[0])
wall_height = SCREEN_HEIGHT // len(matriz)
for y, row in enumerate(matriz):
    for x, cell in enumerate(row):
        if cell == 1:
            wall = Wall(x * wall_width, y * wall_height, wall_width, wall_height)
            mazeHitbox.append(wall.rect)

# Initialize player
player = Player(10+SCREEN_WIDTH // len(matriz[0]),10 + SCREEN_HEIGHT // len(matriz), 10)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # draw maze walls

    speed = 300 * dt

    keys = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if keys[pygame.K_w]:
        dy = -speed
    if keys[pygame.K_s]:
        dy = speed      
    if keys[pygame.K_a]:
        dx = -speed
    if keys[pygame.K_d]:
        dx = speed

    
    #Check for collisions with walls
    is_colliding = False
    playerPosHitbox = player.hitbox.copy()
    playerPosHitbox = playerPosHitbox.move(dx, dy)
    if playerPosHitbox.collidelist(mazeHitbox) != -1:
        is_colliding = True

    if not is_colliding:
        # Move the player if no collision
        player.move(dx, dy)
    #Draw the maze walls
    for wall in mazeHitbox:
        pygame.draw.rect(screen, is_colliding and "red" or "black", wall)
    keys = pygame.key.get_pressed()

    # draw the player as a circle
    player.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()