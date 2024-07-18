import csv
csvAction = "action.csv"
csvGoto = "goto.csv"
csvGramatica = "gramatica.csv"
csvPanico = "panico.csv"

def preencheTabela(csvFile):
    tabela = []
    with open(csvFile) as fT:
        dados = csv.DictReader(fT, delimiter=',') 
        for linha in dados:
            tabela.append(linha)
    return tabela
def preencheTabelaAcoes():
    tabela = preencheTabela(csvAction)
    return tabela
def preencheTabelaDesvios():
    tabela = preencheTabela(csvGoto)
    return tabela
def preencheTabelaAction():
    tabela = preencheTabela(csvGramatica)
    return tabela
def preencheTabelaErros():
    tabela = preencheTabela(csvPanico)
    for entrada in tabela:
        if not (entrada['Follow'] == ''):
            lista = entrada['Follow'].split()
            entrada['Follow'] = lista
    return tabela
