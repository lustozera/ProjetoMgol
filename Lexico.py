
from transicao import *
from tabelaSimbolos import *

dadosErro = {"linha" : 1, "colAtual": 0, "colAntiga": 0 }
def verifica_tabela_dfa(caractere, estado_atual, TabelaTransicao):
    prox_estado = TabelaTransicao[estado_atual].get(caractere)
    if prox_estado != None:
        return prox_estado
    else:
        return -1

def verificaDFA(estado):
    if estado == 1 or estado == 3 or estado == 6:
        token = "Num"
    if estado == 8:
        token = "literal"
    if estado == 9:
        token = "id"
    if estado == 11:
        token = "Comentário"
    if estado == 12:
        token = "OPM"
    if estado == 13 or estado == 15 or estado == 16 or estado == 17 or estado == 18:
        token = "OPRD"
    if estado == 14:
        token = "ATR"
    if estado == 19:
        token = "AB_P"
    if estado == 20:
        token = "FC_P"
    if estado == 21:
        token = "PT_V"
    if estado == 22:
        token = "vir"
    return token

def traduzToken(token):
    tokenTraduzido = token + "("
    if token == "Num":
        return tokenTraduzido + "Número)" 
    if token == "literal":
        return tokenTraduzido + "Literal)"
    if token == "id":
        return tokenTraduzido + "Identificador)"
    if token == "Comentário":
        return tokenTraduzido + "Comentário)"
    if token == "OPM":
        return tokenTraduzido + "Operador Matemático)"
    if token == "OPRD":
        return tokenTraduzido + "Operador Relacional)"
    if token == "ATR":
        return tokenTraduzido + "Atribuição)"
    if token == "AB_P":
        return tokenTraduzido + "Abre Parêntesis - '(')"
    if token == "FC_P":
        return tokenTraduzido + "Fecha Parêntesis - ')')"
    if token == "PT_V":
        return tokenTraduzido + "Ponto e Vírgula - ;)"
    if token == "vir":
        return tokenTraduzido + "Vírgula - ,)"
    else:
        return token

def analisadorLexico(arquivo, TabelaTransicao, TabelaSimbolos):
    distanciaUltimoAceito = 1
    abreAspas = 0
    abreChaves = 0

    tupla = {"lexema": "", "token": "", "tipo": "null", "linha": "","coluna": ""}
    char = arquivo.read(1)
    dadosErro['colAtual'] += 1
    palavra = ""
    estado = 0
    if char == '\"':
        abreAspas = 1
    elif char == '{':
        abreChaves = 1
    elif char == '}':
        abreChaves = 0
    if not char:  
        return {"lexema": "EOF", "token": "$", "tipo": "null", "linha": str(dadosErro["linha"]),"coluna": str(dadosErro["colAtual"])}

    while True:
        if char == "\n":
            dadosErro["linha"] += 1
            dadosErro["colAntiga"] = dadosErro["colAtual"] 
            dadosErro["colAtual"] = 0
        estado_aux = verifica_tabela_dfa(char, estado, TabelaTransicao)
        estado = estado_aux
        if estado == -1:  
            if not char:  
                if tupla['token'] == '' and tupla['lexema'] != '':
                    if abreAspas % 2 != 0:
                        tipoErro = "Não fechou as aspas"
                    elif abreChaves == 1:
                        tipoErro = "Não fechou as chaves"
                    else:
                        tipoErro = "Caractere invalido"

                    print("Erro léxico. " + tipoErro + ": "+ palavra + " - Linha " + str(dadosErro["linha"]) + ", Coluna " + str(dadosErro["colAtual"]))
                    tupla = {"lexema": palavra, "token": "ERRO", "tipo": "null", "linha": str(dadosErro["linha"]), "coluna": str(dadosErro["colAtual"])}
                elif tupla["token"] == "id":
                    tupla = procuraToken(tupla, TabelaSimbolos)
                    tupla.update({"linha": str(dadosErro["linha"]), "coluna": str(dadosErro["colAtual"])})
                else:
                    tupla = {"lexema": "EOF", "token": "$", "tipo": "null", "linha": str(dadosErro["linha"]),"coluna": str(dadosErro["colAtual"])}
                return tupla
            if tupla['lexema'] == '':
                if abreAspas % 2 != 0:
                    tipoErro = "Não fechou as aspas"
                elif abreChaves == 1:
                    tipoErro = "Não fechou as chaves"
                else:
                    tipoErro = "Caractere invalido"
                    print("Erro léxico. " + tipoErro + ": " + char + " - Linha " + str(
                        dadosErro["linha"]) + ", Coluna " + str(dadosErro["colAtual"]))
                tupla = {"lexema": char, "token": "ERRO", "tipo": "null", "linha": str(dadosErro["linha"]),"coluna": str(dadosErro["colAtual"])}
                return tupla
            arquivo.seek(arquivo.tell() - distanciaUltimoAceito)  
            if char == '\n':
                dadosErro["linha"] -= 1
                dadosErro["colAtual"] = dadosErro["colAntiga"] - distanciaUltimoAceito
            else :
                dadosErro["colAtual"] = dadosErro["colAtual"] - distanciaUltimoAceito
            if tupla["token"] == "id":
                tupla = procuraToken(tupla, TabelaSimbolos)
                tupla.update({"linha": str(dadosErro["linha"]),"coluna": str(dadosErro["colAtual"])}) 
            return tupla
        elif TabelaTransicao[estado].get("final"):  
            palavra = palavra + char
            distanciaUltimoAceito = 1
            token = verificaDFA(estado)
            if(estado == 1):
                tupla = {"lexema": palavra, "token": token, "tipo": "int", "linha": str(dadosErro["linha"]),"coluna": str(dadosErro["colAtual"])}
            elif(estado == 3 or estado == 6):
                tupla = {"lexema": palavra, "token": token, "tipo": "real", "linha": str(dadosErro["linha"]),"coluna": str(dadosErro["colAtual"])}
            else:
                tupla = {"lexema": palavra, "token": token, "tipo": "null", "linha": str(dadosErro["linha"]),"coluna": str(dadosErro["colAtual"])}
        else:
            if (estado == 0 and char != " " and char != "\n" and char != "\t") or estado != 0:
                palavra = palavra + char
                distanciaUltimoAceito += 1
        char = arquivo.read(1)
        dadosErro['colAtual'] += 1
        if char == '\"':
            abreAspas = abreAspas + 1
        elif char == '{':
            abreChaves = 1
        elif char == '}':
            abreChaves = 0

