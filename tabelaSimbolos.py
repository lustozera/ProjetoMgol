GREEN = '\033[92m'
RESET = '\033[0m'

def preenchePalavrasReservadas():
    tabelaSimbolos = {}
    listaPalavrasReservadas = ['inicio', 'varinicio', 'varfim', 'escreva', 'leia', 'se', 
    'entao', 'fimse', 'repita', 'fimrepita', 'fim', 'inteiro', 'lit', 'real']
    for palavra in listaPalavrasReservadas:
        tabelaSimbolos[palavra] = {'lexema': palavra, 'token': palavra, 'tipo': 'null'}
    return tabelaSimbolos

def procuraToken(tupla, tabelaSimbolos):
    if not (tupla['lexema'] in tabelaSimbolos):
        tabelaSimbolos[tupla['lexema']] = tupla      
    return tabelaSimbolos[tupla['lexema']]

