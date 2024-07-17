import sys
from tabelaTransicao import *
from tabelaSimbolos import *
from analisadorLexico import *
from analisadorSintatico import *
from preencheTabelas import *
from analisadorSemantico import *
import os

# Preenche as tabelas utilizadas pelo Analisador Sintático
tabelaAcoes = preencheTabelaAcoes()
tabelaDesvios = preencheTabelaDesvios()
tabelaQtdSimbolos = preencheTabelaQtdSimbolos()
tabelaErros = preencheTabelaErros()
argumentos = sys.argv
arqFonte = open("fonte.alg", encoding="utf-8")

nome, extensao = os.path.splitext("fonte.alg")

# Chama o Analisador Sintático
analisadorSintatico(tabelaAcoes,tabelaDesvios,tabelaQtdSimbolos, tabelaErros, arqFonte, nome)

arqFonte.close()
