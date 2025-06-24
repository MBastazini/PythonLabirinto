import random

PAREDE = '#'
CAMINHO = '.'
ENTRADA = 'E'
FIM_DE_CAMINHO = '&'
QUADRADO_BONUS = '!'
SAIDA = 'S'


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
        matriz[y][x] = FIM_DE_CAMINHO

def newMaze(size):
    matriz = criaMatrizVazia(size)
    # Começa de uma posição ímpar (ex.: (1,1))
    start_x, start_y = len(matriz[0]) // 2, len(matriz) // 2
    matriz[start_y][start_x] = ENTRADA
    geraLabirintoRecursivo(matriz, start_x, start_y)
    return matriz


num = 17
with open("saves/fases/fase16.txt", "w") as f:
    size = 23 + (num * 4)
    maze = newMaze(size)
    for row in maze:
        f.write(''.join(row) + '\n')
