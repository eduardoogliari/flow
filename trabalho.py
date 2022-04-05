import sys
import time
import numpy as np
from os import path
from os import listdir
from os.path import isfile, join

files = [
        'tai20_5.txt'
    ,   'tai20_10.txt'
    ,   'tai20_20.txt'
    ,   'tai50_5.txt'
    ,   'tai50_10.txt'
    ,   'tai50_20.txt'
    ,   'tai100_5.txt'
    ,   'tai100_10.txt'
    ,   'tai100_20.txt'
    ,   'tai200_10.txt'
]

# > Função que calcula a aptidao de uma solução dada uma instância para o problema flow shop sequencing
# > A aptidão desse problema é o makespan, que deve ser minimizado
# > 'instancia' deve ser uma lista de listas m X n, onde m é o número de máquinas e n o número de tarefas,
#       com inteiros identificando os tempos de cada tarefa em cada máquina
# > 'solucao' deve ser uma lista de inteiros identificando as tarefas (de 1 até n onde n é o número de tarefas da instância)
def makespan(instancia, solucao):
    nM = len(instancia)
    tempo = [0] * nM
    tarefa = [0] * len(solucao)
    for t in solucao:
        if tarefa[t-1] == 1:
            return "SOLUÇÃO INVÁLIDA: tarefa repetida!"
        else:
            tarefa[t-1] = 1
        for m in range (nM):
            if tempo[m] < tempo[m-1] and m!=0:
                tempo[m] = tempo[m-1]
            tempo[m] += instancia[m][t-1]
    return tempo[nM-1]

def pegarListaArquivos():
    currentPath = path.dirname(path.abspath(__file__))
    folderPath = currentPath + "/flowshop/"
    filepaths = []
    for f in files:
        filepaths.append( folderPath + f )
    return filepaths

#ler a primeira instância de cada um dos dez arquivos, armazenar em uma lista e retornar essa lista
def lerInstancias(listaArquivos):
    result = []

    for filepath in listaArquivos:
        f = open( filepath, "r" )
        if f:
            f.readline() # Pula cabecario
            values = f.readline().split() # Le valores da segunda linha
            jobs = int(values[0])
            machines = int(values[1])
            print(filepath)

            f.readline() # Pula terceira linha

            lista = []

            x = 0
            while x < machines:
                line = f.readline().split()
                lista_num = []
                for num in line:
                    lista_num.append(int(num))
                lista.append(lista_num)
                x += 1
            result.append(lista)
    return result


# criar uma lista de soluções aleatórias (podem definir outro critério se desejarem) com o tamanho repassado
def criarPopulacaoInicial(instancia, tamanho):
    # np.random.uniform(,)
    pass

# usar a função makespan para avalaiar a aptidão de cada elemento da população
def avaliarPop(populacao):
    pass

# retorna a melhor solucao dentre a populacao atual
def retornaMelhorSolucao(populacao, aptidaoPop):
    pass

# função deve retornar quais elementos serão recombinados e com quem (pode fazer uso da aptidao ou não para o critério de seleção)
def selecionarPop(populacao, aptidaoPop):
    pass

# função deve usar o operador de recombinacao (definido pelo grupo_ para gerar novas soluções filhas
def recombinacao(populacaoSelecionada):
    pass

# função deve usar o operador de mutacao (definido pelo grupo) para modificar as soluções filhas (não precisa ser todas)
def mutacao(novasSolucoes):
    pass

# função deve criar uma nova população com as soluções novas (eliminando as antigas ou usando outro critério de seleção desejado)
def selecionarNovaGeracao(populacaoAtual, novasSolucoes):
    pass

# computar o lower bound, upper bound, valores médios e desvios (tanto para aptidão quanto para o tempo de execução) para cada instância
# salvar em formato de tabela (pode ser um CSV) em um arquivo
def salvarRelatorio(relatorio):
    pass


listaArquivos = pegarListaArquivos()
print(listaArquivos)

listaInstancias = lerInstancias(listaArquivos)
d = {}
#relatorio = [dict() for instancia in range(listaIntancias)]

# Pega a lista de listas e insere em um dicionario 'd'
index = 0
for i in listaInstancias:
    #print(i)
    #print()
    d[index] = i
    index += 1


for instancia in range (listaInstancias):
    tamanhoPop = len(instancia)
    tempoMaximo = 100
    melhoresSolucoes = relatorio[instancia]

    #Para cada instância executar todo o algoritmo 10 vezes
    for it in range (10):
        melhorSolucao = {'solucao':[], 'aptidao':sys.maxint, 'tempoFinal':0}
        tempoInicial = time.time()
        populacao = criarPopulacaoInicial(instancia, tamanhoPop)

        while True:
            if tempoMaximo <= time.time() - tempoInicial:
                break
            if criterioParada2 == True:
                break

            aptidaoPop = avaliarPop(populacao)
            melhorSolucaoAtual = retornaMelhorSolucao(populacao, aptidaoPop)

            if melhorSolucao['aptidao'] > melhorSolucaoAtual['aptidao']:
                melhorSolucao = melhorSolucaoAtual

            populacaoSelecionada = selecionarPop(populacao, aptidaoPop)
            novasSolucoes = recombinacao(populacaoSelecionada)
            novasSolucoes = mutacao(novasSolucoes)
            populacao = selecionarNovaGeracao(populacao, novasSolucoes)

        melhorSolucao['tempoFinal'] = time.time() - tempoInicial
        print(melhorSolucao)
        melhoresSolucoes = melhoresSolucoes | melhorSolucao

    relatorio[instancia] = melhoresSolucoes

salvarRelatorio(relatorio)

