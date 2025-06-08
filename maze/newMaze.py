import random
from maze import Wall
WALL_SIZE = 50
PAREDE = '#'
CAMINHO = '.'
ENTRADA = 'E'
SAIDA = 'S'

RADIUS = 1/10

EXIT_X = 0
EXIT_Y = 0

def criaMatrizVazia(tamanho):
    return [[PAREDE for _ in range(tamanho)] for _ in range(tamanho)]

def geraLabirintoRecursivo(matriz, x, y):
    direcoes = [(0, -2), (0, 2), (-2, 0), (2, 0)]  # cima, baixo, esquerda, direita
    random.shuffle(direcoes)

    count = 0
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
            else:
                count += 1
        else:
            count += 1
        
    if count == 4:
        # Marca a célula atual como saída
        matriz[y][x] = SAIDA

def newMaze(size):
    matriz = criaMatrizVazia(size)
    # Começa de uma posição ímpar (ex.: (1,1))
    start_x, start_y = len(matriz[0]) // 2, len(matriz) // 2
    matriz[start_y][start_x] = ENTRADA
    geraLabirintoRecursivo(matriz, start_x, start_y)
    return matriz

def generateWallList(level_difficulty, SCREEN_WIDTH=600, SCREEN_HEIGHT=600, debug_mode=False):
    matriz = newMaze(23 + (
            level_difficulty * 4 * 3  # Increase maze size based on difficulty
        )) #multiplos de 4 mais 3.

    classWallList = []

    radius = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 2
    wall_width = WALL_SIZE
    wall_height = WALL_SIZE

    #vê todas as saidas e seleciona uma
    all_exits = []
    for y, row in enumerate(matriz):
        for x, cell in enumerate(row):
            if cell == SAIDA:
                if (y < len(matriz)*(RADIUS) or y > len(matriz)*(1-RADIUS) or x < len(matriz[0])*(RADIUS) or x > len(matriz[0])*(1-RADIUS)):
                    all_exits.append((x, y))

    if all_exits:
        # Select a random exit
        exit_x, exit_y = random.choice(all_exits)
        EXIT_X, EXIT_Y = exit_x, exit_y

    for y, row in enumerate(matriz):
        for x, cell in enumerate(row):
            if cell == PAREDE:
                if debug_mode:
                    if (x != len(matriz)//2 and y != len(matriz)//2+1):
                        wall = Wall(x * wall_width, y * wall_height, wall_width, wall_height)
                        classWallList.append(wall)
                else:
                    wall = Wall(x * wall_width, y * wall_height, wall_width, wall_height, active=True)
                    classWallList.append(wall)
            if cell == ENTRADA:
                # If the cell is the starting point, draw it as a wall
                wall = Wall(x * wall_width, y * wall_height, wall_width, wall_height, color="green", active=False)
                classWallList.append(wall)
            if cell == SAIDA:
                if not debug_mode:
                    if x == EXIT_X and y == EXIT_Y:
                        
                        wall = Wall(x * wall_width, y * wall_height, wall_width, wall_height, color="red", active=False, type="exit")
                        classWallList.append(wall)
                #se não for saoda é caminho, não desenha nada
            if(x == len(matriz)//2 and y == len(matriz)//2+2) and debug_mode:
                wall = Wall(x * wall_width, y * wall_height, wall_width, wall_height, color="red", active=False, type="exit")
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
        "exit": (EXIT_X, EXIT_Y)
    }

