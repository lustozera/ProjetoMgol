from Lexico import *
from tabelaSimbolos import *
from transicao import *

def analisadorSintatico(tabelaAction, tabelaDesvios, tabelaGoto, tabelaErros, arquivo):
    TabelaTransicao = []
    tabelaDFA(TabelaTransicao)
    TabelaSimbolos = preenchePalavrasReservadas()
    pilha = []
    pilha.append(0)
    while True:
        b = analisadorLexico(arquivo, TabelaTransicao, TabelaSimbolos)
        a = b["token"]
        if a != "Comentário" and a != "ERRO":
            break
    flagSimbolo = False  
    aAntigo = a
    flagErro = False 
    celula = ""
    while(1):
        s = pilha[len(pilha) - 1]
        if tabelaAction[int(s)].get(a):
            celula = tabelaAction[int(s)].get(a)
            operacao = celula[0]
            t = celula.translate({ord('S'): None, ord('R'): None})
        else:
            t = 0
        if t and operacao == "S":
            pilha.append(t)
            while True:
                if flagSimbolo: 
                    a = aAntigo
                    flagSimbolo = False
                else:
                    b = analisadorLexico(arquivo, TabelaTransicao, TabelaSimbolos)
                    a = b["token"]
                if a != "Comentário" and a != "ERRO":
                    break
        elif t and operacao == "R":
            x = tabelaGoto[int(t) - 1].get("TamanhoBeta")
            A = tabelaGoto[int(t) - 1].get("A")
            B = tabelaGoto[int(t) - 1].get("Beta")

            if x:
                for i in range(0, int(x)):
                    pilha.pop()
            t = pilha[len(pilha) - 1]
            if tabelaDesvios[int(t)].get(A):
                valor = tabelaDesvios[int(t)].get(A)
                pilha.append(valor)
            print("Regra: " + A +" -> " + B)
        elif celula == "aceita":
            print()
            print("___________________________________________________________________")
            if flagErro:
                print("Fim da análise Sintática: foram encontrados erros. Falha!")
                print("___________________________________________________________________")                
            else:
                print("Fim da análise Sintática: Aceitou!")
                print("___________________________________________________________________")                
            return
        else:
            flagErro = True
            simbolosFaltando = {}
            listaParaImprimir = ""
            for k,v in tabelaAction[int(s)].items():
                if v != '' and k!='Estado':
                    simbolosFaltando.update({k : v})
                    nomeToken = traduzToken(k)
                    listaParaImprimir = listaParaImprimir + " " + str(nomeToken)
            print("\nErro Sintático. " + "Linha: " + b.get("linha") +" Coluna: " + b.get("coluna") +" Está faltando:"+ listaParaImprimir)
            if len(simbolosFaltando) == 1:
                print("\tTratamento de erro. Inserindo símbolo ausente...")
                chave = [key for key in simbolosFaltando.keys()]
                aAntigo = a
                a = chave[0]
                flagSimbolo = True 
                print("\t" + a + " inserido para prosseguir a análise.")
                print("\tFim de tratamento de erro\n")
            else:
                print("\t\tIniciando tratamento de erro.  À procura de um token sincronizante...")
                listaFollow = tabelaErros[int(s)].get('Follow')
                aux = 1
                while (aux):
                    while True:
                        a = analisadorLexico(arquivo, TabelaTransicao, TabelaSimbolos)["token"]
                        if a == "$":
                            print("\t\tArquivo finalizado. Não foi possível concluir a recuperação...")
                            print("\t\tFim de tratamento de erro\n")
                            print("\n___________________________________________________________________")
                            print("Fim da análise Sintática: foram encontrados erros. Falha!")
                            print("___________________________________________________________________")
                            return
                        elif a != "Comentário" and a != "ERRO":
                            break
                    for token in listaFollow:
                        if token == a:
                            aux = 0
                            break
                print("\t\tEncontrado token sincronizante: " + a)
                x = tabelaErros[int(s)].get('Quantidades')
                if x:
                    for i in range(0, int(x)):
                        pilha.pop()
                print("\t\tRetomando análise sintática\n")