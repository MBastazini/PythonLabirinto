import math
def calcularbaskara(a ,b, c):
    # equação
    delta = (b ** 2) - 4 * a * c

    # exceção para "a" negativo
    if a == 0:
        print("Isso não é uma equação de segundo grau")
        return False
    elif delta < 0:
        print("Não existem raízes reais")
        return False

    elif delta == 0:
        x = -b / (2 * a)
        print(x)
        return [x, x]

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("x1 = " + str(x1))
        print("x2 = " + str(x2))
        return [x1, x2]

v1 = float(input("Digite o valor de A: "))
v2 = float(input("Digite o valor de B: "))
v3 = float(input("Digite o valor de C: "))

resultado = calcularbaskara(v1, v2, v3)
if(resultado):
    print(f"Raiz quadrada de {resultado[0]} é {math.sqrt(resultado[0])}")
    print(f"Raiz quadrada de {resultado[1]} é {math.sqrt(resultado[1])}")
else:
    print("Nenhum resultado válido encontrado.")