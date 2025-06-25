try:
    with open('teste.txt', 'r') as f:
        lines = f.readlines()
        numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        new_lines = []
        for line in lines:
            n = len(line)
            new_line = ""
            for i in range(n):
                if line[n-1-i] not in numeros:
                    new_line += line[n-1-i]
            new_lines.append(new_line)
        with open('teste.txt', 'w') as f:
            f.writelines(new_lines)

except FileNotFoundError:
    print("Arquivo teste.txt não encontrado.")

