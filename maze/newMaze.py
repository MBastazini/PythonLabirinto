import random

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

def newMaze(size):
    matriz = criaMatrizVazia(size)
    # Começa de uma posição ímpar (ex.: (1,1))
    start_x, start_y = len(matriz[0]) // 2, len(matriz) // 2
    matriz[start_y][start_x] = 2
    geraLabirintoRecursivo(matriz, start_x, start_y)
    return matriz