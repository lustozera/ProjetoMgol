import sys
from tabelaTransicao import *
from tabelaSimbolos import *
from analisadorLexico import *

#Criação e preenchimento da tabela de transições do DFA
TabelaTransicao = []
preenche_tabela_dfa(TabelaTransicao)

#Criação e preenchimento da tabela de símbolos
TabelaSimbolos = preenchePalavrasReservadas()

argumentos = sys.argv

arq = open("teste.mgol")


while(1):
    resultado = analisadorLexico(arq, TabelaTransicao, TabelaSimbolos)
    if resultado:
        if resultado.get("token") == "$":
            print(resultado)
            break
        else:
            print(resultado)

arq.close() 