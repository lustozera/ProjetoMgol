# Cores para formatar saída do print(impressao do simbolo adicionado na tabela)
GREEN = '\033[92m'
RESET = '\033[0m'

# Preenche a tabela com as palavras reservadas
def preenchePalavrasReservadas():
    tabelaSimbolos = {}
    listaPalavrasReservadas = ['inicio', 'varinicio', 'varfim', 'escreva', 'leia', 'se', 
    'entao', 'fimse', 'repita', 'fimrepita', 'fim', 'inteiro', 'lit', 'real', 'faca', 'enquanto',
    'fimenquanto']
    for palavra in listaPalavrasReservadas:
        tabelaSimbolos[palavra] = {'lexema': palavra, 'token': palavra, 'tipo': 'null'}

    return tabelaSimbolos

# Dado uma tupla com lexema, token e tipo e a tabela de simbolos, procura se existe
# o token, adicionando caso não encontre
def procuraToken(tupla, tabelaSimbolos):
    if not (tupla['lexema'] in tabelaSimbolos):
        tabelaSimbolos[tupla['lexema']] = tupla
        #print(GREEN + "Adicionado na tabela de símbolos: " + RESET + tupla['lexema'])
        
    return tabelaSimbolos[tupla['lexema']]

