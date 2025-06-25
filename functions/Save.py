import json


#####
#####   Função apenas para verificar se o arquivo mestre (arquivo contendo os saves) existe
#####

Caminho_arquivo = "saves/arquivoMestre.txt"

def _VerificaSave():
    try:
        with open(Caminho_arquivo, "r") as f:
            pass
    except:
        f = open(Caminho_arquivo, "w")
        f.write("[]")
        f.close()

def _Formatacao(name, id, defaultLevels=[], campaign=[]):

    formato = "   {\n"
    formato += f"    \"name\": \"{name}\",\n"
    formato += f"    \"id\": {id},\n"
    if defaultLevels == []:
        formato += "     \"defaultLevels\": [],\n"
    else:
        formato += "     \"defaultLevels\": [\n"
        j = 0
        for elem in defaultLevels:
            if j == 0:
                pass
            else:
                formato += ",\n"
            j += 1
            formato += "         {\n" 
            formato += f"            \"difficult\": {elem["difficult"]},\n"
            formato += "            \"scores\": [\n"
            i = 0
            for scores in elem["scores"]:
                if i == 0:
                    pass
                else:
                    formato += ",\n"
                i += 1
                formato += "               {\n"
                formato += f"                  \"n\": {scores["n"]},\n"
                formato += f"                  \"points\": {scores["points"]}\n"
                formato += "               }"
                if i == len(elem["scores"]):
                    formato += "\n"
            formato += "            ]\n"
            formato += "         }"
            if j == len(defaultLevels):
                formato += "\n"
        formato += "     ],\n"
    if campaign == []:
        formato += "     \"campaign\": []\n"
    else:
        j = 0
        formato += "     \"campaign\": [\n"
        for elem in campaign:
            if j == 0:
                pass
            else:
                formato += ",\n"
            j += 1
            formato += "         {\n" 
            formato += f"            \"level\": {elem["level"]},\n"
            formato += "            \"scores\": [\n"
            i = 0
            for scores in elem["scores"]:
                if i == 0:
                    pass
                else:
                    formato += ",\n"
                i += 1
                formato += "               {\n"
                formato += f"                  \"n\": {scores["n"]},\n"
                formato += f"                  \"points\": {scores["points"]}\n"
                formato += "               }"
                if i == len(elem["scores"]):
                    formato += "\n"
            formato += "            ]\n"
            formato += "         }"
            if j == len(campaign):
                formato += "\n"
        formato += "     ]\n"
    formato += "   }"

    return formato

#####
#####   Função que converte uma string em um array json
#####

def _ConverteEmArray(string):
    data = json.loads(string)
    return data

#####
#####   Cria um arquivo de save para um novo jogador
#####

def CreateNewSave(plyrName):
    _VerificaSave()
    f = open(Caminho_arquivo, "r")
    data = _ConverteEmArray(f.read())
    f.close
    f = open(Caminho_arquivo, "r")
    content = [linha.strip("\n") for linha in f.readlines()]
    f.close
    n = 0
    for player in data:
        n = player["id"] + 1
    
    f.close
    f = open(Caminho_arquivo, "w")
    save = "[\n"

    
    for linhas in content[1:-1]:
        save += linhas + "\n"

    if data != []:
        save += ",\n"
    save += _Formatacao(plyrName, n)
    save += "\n]"
    
    f.write(save)
    f.close()

#####
#####   Função que mostra os arquivos de save existentes
#####

def SelectAllSaves():
    f = open(Caminho_arquivo, "r")
    data = _ConverteEmArray(f.read())
    return data

#####
#####   Função que mostra um save baseado no ID do save
#####

def SelectSaveFromID(plyrID):
    f = open(Caminho_arquivo, "r")
    data = _ConverteEmArray(f.read())
    for player in data:
        if player["id"] == plyrID:
            return player
        else:
            pass
    return []

def SaveScore(plyrID, modo, nivel, pontuacao):
    #modo = 1 => sandbox
    #modo = 2 => modo campanha
    #nivel pode ser a dificuldade ou o level
    #pontuacao é a potação em si (número inteiro)
    #retorna True se a alteração for bem sucedida
    #retorna False se algo der errado

    f = open(Caminho_arquivo, "r")
    oldsave = f.read()
    data = _ConverteEmArray(oldsave)
    f.close()
    j = 0

    if(modo == 1):
        if(nivel > 3 or nivel <0):
            return False

        for saves in data:
            j += 1
            if saves["id"] == plyrID:
                i = 0
                if(len(saves["defaultLevels"]) == 0):
                    saves["defaultLevels"].append({"difficult": nivel, "scores": [{"n": 1, "points": pontuacao}]})
                    break
                for defaultLevels in saves["defaultLevels"]:
                    i += 1
                    if defaultLevels["difficult"] == nivel:
                        n = defaultLevels["scores"][-1]["n"] + 1
                        defaultLevels["scores"].append({"n": n, "points": pontuacao})
                        break
                    elif (i == len(saves["defaultLevels"])):
                        saves["defaultLevels"].append({"difficult": nivel, "scores": [{"n": 1, "points": pontuacao}]})
                        break
                break
            elif(j == len(data)):
                return False
        save = "["
        i = 0
        for elem in data:
            if i == 0:
                save += "\n"
            else:
                save += "\n,\n"
            i += 1
            save += _Formatacao(elem["name"], elem["id"], elem["defaultLevels"],elem["campaign"])
            if i == len(data):
                save += "\n"
        save += "]"

        f = open(Caminho_arquivo, "w")
        f.write(save)
        f.close()
        return True

    elif(modo == 2):
        if(nivel < 0 or nivel > 30):
            return False
        
        for saves in data:
            j += 1
            if saves["id"] == plyrID:
                i = 0
                if(len(saves["campaign"]) == 0):
                    saves["campaign"].append({"level": nivel, "scores": [{"n": 1, "points": pontuacao}]})
                    break
                for campaigns in saves["campaign"]:
                    i += 1
                    if campaigns["level"] == nivel:
                        print("oi")
                        n = campaigns["scores"][-1]["n"] + 1
                        campaigns["scores"].append({"n": n, "points": pontuacao})
                        break
                    elif (i == len(saves["campaign"])):
                        saves["campaign"].append({"level": nivel, "scores": [{"n": 1, "points": pontuacao}]})
                        break
                break
            elif(j == len(data)):
                return False
        save = "["
        i = 0
        for elem in data:
            if i == 0:
                save += "\n"
            else:
                save += "\n,\n"
            i += 1
            save += _Formatacao(elem["name"], elem["id"], elem["defaultLevels"],elem["campaign"])
            if i == len(data):
                save += "\n"
        save += "]"
        
        f = open(Caminho_arquivo, "w")
        f.write(save)
        f.close()
        return True
        
    return False
        
#####
#####   Função que deleta um save
#####

def DeletSaveFromID(plyrID):
    #retorna True se tudo estiver correto
    #retorna False se algo der errado

    f = open(Caminho_arquivo, "r")
    oldsave = f.read()
    data = _ConverteEmArray(oldsave)
    f.close()

    i = 0
    while i < len(data):
        if data[i]['id'] == plyrID:
            data.pop(i)
        else:
            pass

        i += 1
    
    save = "["
    i = 0
    for elem in data:
        if i == 0:
            save += "\n"
        else:
            save += "\n,\n"
        i += 1
        save += _Formatacao(elem["name"], elem["id"], elem["defaultLevels"],elem["campaign"])
        if i == len(data):
            save += "\n"
    save += "]"
    
    if save == oldsave:
        return False

    f = open(Caminho_arquivo, "w")
    f.write(save)
    f.close()
    return True
