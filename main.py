import sys
from transicao import *
from tabelaSimbolos import *
from Lexico import *
from Sintatico import *
from tabelasPreenche import *
import os

tabelaAction = preencheTabelaAcoes()
tabelaDesvios = preencheTabelaDesvios()
tabelaQtdSimbolos = preencheTabelaAction()
tabelaErros = preencheTabelaErros()
argumentos = sys.argv
arqFonte = open("fonte.alg", encoding="utf-8")

nome, extensao = os.path.splitext("fonte.alg")
analisadorSintatico(tabelaAction,tabelaDesvios,tabelaQtdSimbolos, tabelaErros, arqFonte,)
