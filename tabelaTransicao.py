import string

# Constantes para a identificação numérica dos estados
estadoInicial = 0
estadoNum = 1
estadoNumPonto = 2
estadoNumPontoFinal = 3
estadoNumExpoente1 = 4
estadoNumExpoente2 = 5
estadoNumExpoenteFinal = 6
estadoLiteral = 7
estadoLiteralFinal = 8
estadoId = 9
estadoComentario = 10
estadoComentarioFinal = 11
estadoOPM = 12
estadoOPRMenor = 13
estadoRCB = 14
estadoOPRMenorIgualDiferente = 15
estadoOPRMaior = 16
estadoOPRMaiorIgual = 17
estadoOPRIgual = 18
estadoABP = 19
estadoFCP = 20
estadoPTV = 21
estadoVIR = 22

# Função que preenche a tabela de transição do autômato
def preenche_tabela_dfa(Tabela_Transicao):

    # Estado 0 - estadoInicial:
    linha = {}
    linha.update({"final": False})
    for c in string.ascii_letters:
        linha.update({c:estadoId})
    for c in range(0,10):
        linha.update({str(c):estadoNum})
    linha.update({"\n":estadoInicial, " ": estadoInicial, "\t": estadoInicial})
    linha.update({"\"": estadoLiteral})
    linha.update({"{":estadoComentario})
    linha.update({"<":estadoOPRMenor , ">":estadoOPRMaior , "=":estadoOPRIgual})
    linha.update({"+": estadoOPM, "-": estadoOPM, "*": estadoOPM, "/": estadoOPM})
    linha.update({"(": estadoABP, ")": estadoFCP, ";": estadoPTV, ",": estadoVIR})
    Tabela_Transicao.append(linha)

    # Estado 1 - estadoNum:
    linha = {}
    linha.update({"final": True})
    for c in range(0, 10):
        linha.update({str(c): estadoNum})
    linha.update({".": estadoNumPonto, "E": estadoNumExpoente1, "e": estadoNumExpoente1})
    Tabela_Transicao.append(linha)

    # Estado 2 - estadoNumPonto:
    linha = {}
    linha.update({"final": False})
    for c in range(0, 10):
        linha.update({str(c): estadoNumPontoFinal})
    Tabela_Transicao.append(linha)

    # Estado 3 - estadoNumPontoFinal:
    linha = {}
    linha.update({"final": True})
    for c in range(0, 10):
        linha.update({str(c): estadoNumPontoFinal})
    linha.update({"E": estadoNumExpoente1, "e": estadoNumExpoente1})
    Tabela_Transicao.append(linha)

    # Estado 4 - estadoNumExpoente1:
    linha = {}
    linha.update({"final": False})
    for c in range(0, 10):
        linha.update({str(c): estadoNumExpoenteFinal})
    linha.update({"+": estadoNumExpoente2, "-": estadoNumExpoente2})
    Tabela_Transicao.append(linha)

    # Estado 5 - estadoNumExpoente2:
    linha = {}
    linha.update({"final": False})
    for c in range(0, 10):
        linha.update({str(c): estadoNumExpoenteFinal})
    Tabela_Transicao.append(linha)

    # Estado 6 - estadoNumExpoenteFinal:
    linha = {}
    linha.update({"final": True})
    for c in range(0, 10):
        linha.update({str(c): estadoNumExpoenteFinal})
    Tabela_Transicao.append(linha)

    # Estado 7 - estadoLiteral
    linha = {}
    linha.update({"final": False})
    for c in string.printable:
        if c != "\"":
            linha.update({c:estadoLiteral})
    linha.update({"\"": estadoLiteralFinal})
    Tabela_Transicao.append(linha)

    # Estado 8 - estadoLiteralFinal
    linha = {}
    linha.update({"final": True})
    Tabela_Transicao.append(linha)

    # Estado 9 - estadoId
    linha = {}
    linha.update({"final": True})
    for c in range(0, 10):
        linha.update({str(c): estadoId})
    for c in string.ascii_letters:
        linha.update({c:estadoId})
    linha.update({"_": estadoId})
    Tabela_Transicao.append(linha)

    # Estado 10 - estadoComentario
    linha = {}
    linha.update({"final": False})
    for c in string.printable:
        linha.update({c:estadoComentario})
    linha.update({"\n": estadoComentario})
    linha.update({"\t": estadoComentario})
    linha.update({"}": estadoComentarioFinal})
    Tabela_Transicao.append(linha)

    # Estado 11 - estadoComentarioFinal
    linha = {}
    linha.update({"final": True})
    Tabela_Transicao.append(linha)

    # Estado 12 - estadoOPM
    linha = {}
    linha.update({"final": True})
    Tabela_Transicao.append(linha)

    # Estado 13 - estadoOPRMenor
    linha = {}
    linha.update({"final": True})
    linha.update({"-": estadoRCB})
    linha.update({">": estadoOPRMenorIgualDiferente, "=": estadoOPRMenorIgualDiferente})
    Tabela_Transicao.append(linha)

    # Estado 14 - estadoRCB
    linha = {}
    linha.update({"final": True})
    Tabela_Transicao.append(linha)

    # Estado 15 - estadoOPRMenorIgualDiferente
    linha = {}
    linha.update({"final": True})
    Tabela_Transicao.append(linha)

    # Estado 16 - estadoOPRMaior
    linha = {}
    linha.update({"final": True})
    linha.update({"=": estadoOPRMaiorIgual})
    Tabela_Transicao.append(linha)

    # Estado 17 - estadoOPRMaiorIgual
    linha = {}
    linha.update({"final": True})
    Tabela_Transicao.append(linha)

    # Estado 18 - estadoOPRIgual
    linha = {}
    linha.update({"final": True})
    Tabela_Transicao.append(linha)

    # Estado 19 - estadoABP
    linha = {}
    linha.update({"final": True})
    Tabela_Transicao.append(linha)

    # Estado 20 - estadoFCP
    linha = {}
    linha.update({"final": True})
    Tabela_Transicao.append(linha)

    # Estado 21 - estadoPTV
    linha = {}
    linha.update({"final": True})
    Tabela_Transicao.append(linha)

    # Estado 22 - estadoVIR
    linha = {}
    linha.update({"final": True})
    Tabela_Transicao.append(linha)

# Aqui algumas funções para teste

#Teste = []
#preenche_tabela_dfa(Teste)

##Imprime toda a tabela de transições
#i = 0
#for k in Teste:
#    print("Estado:" + str(i) + " " + str(Teste[i]) + "\n")
#   i+=1