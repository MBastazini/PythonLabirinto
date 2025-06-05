import random
from maze import Wall
WALL_SIZE = 100  # Tamanho do bloco da parede
    
# draw walls based on the matrix
#Tamanho usando ocupando a tela inteira 
#wall_width = SCREEN_WIDTH // len(matriz[0])
#wall_height = SCREEN_HEIGHT // len(matriz)
PAREDE = '#'
CAMINHO = '.'
ENTRADA = 'E'
SAIDA = 'S'


def criaMatrizVazia(tamanho):
    return [[PAREDE for _ in range(tamanho)] for _ in range(tamanho)]

def geraLabirintoRecursivo(matriz, x, y):
    direcoes = [(0, -2), (0, 2), (-2, 0), (2, 0)]  # cima, baixo, esquerda, direita
    random.shuffle(direcoes)

    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy

        # Verifica se a célula vizinha está dentro dos limites e é uma parede
        if 1 <= nx < len(matriz) - 1 and 1 <= ny < len(matriz) - 1:
            if matriz[ny][nx] == PAREDE:
                # Remove parede entre as células
                matriz[y + dy // 2][x + dx // 2] = CAMINHO
                # Marca a nova célula como caminho
                matriz[ny][nx] = CAMINHO
                # Continua recursivamente
                geraLabirintoRecursivo(matriz, nx, ny)

def newMaze(size):
    matriz = criaMatrizVazia(size)
    # Começa de uma posição ímpar (ex.: (1,1))
    start_x, start_y = len(matriz[0]) // 2, len(matriz) // 2
    matriz[start_y][start_x] = ENTRADA
    geraLabirintoRecursivo(matriz, start_x, start_y)
    return matriz

def generateWallList(level_difficulty, SCREEN_WIDTH=600, SCREEN_HEIGHT=600):
    matriz = newMaze(23 + (
            level_difficulty * 4 * 3  # Increase maze size based on difficulty
        )) #multiplos de 4 mais 3.

    classWallList = []

    wall_width = WALL_SIZE
    wall_height = WALL_SIZE
    for y, row in enumerate(matriz):
        for x, cell in enumerate(row):
            if cell == PAREDE:
                wall = Wall(x * wall_width, y * wall_height, wall_width, wall_height)
                classWallList.append(wall)
            if cell == ENTRADA:
                # If the cell is the starting point, draw it as a wall
                wall = Wall(x * wall_width, y * wall_height, wall_width, wall_height, color="green", active=False)
                classWallList.append(wall)

    #maze is not centered, so we move the walls to center the maze
    offset_x = (SCREEN_WIDTH - (len(matriz[0]) * wall_width)) // 2
    offset_y = (SCREEN_HEIGHT - (len(matriz) * wall_height)) // 2
    for wall in classWallList:
        wall.rect.x += offset_x
        wall.rect.y += offset_y
    return classWallList

def getMazeInfo():
    return {
        "wall_size": WALL_SIZE,
    }

