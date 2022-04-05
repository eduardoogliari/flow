from os import path
from os import listdir
from os.path import isfile, join
import numpy as np
import random

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

currentPath = path.dirname(path.abspath(__file__))
folderPath = currentPath + "/flowshop/"

filepaths = []
for f in files:
    filepaths.append( folderPath + f )

result = []
for file in filepaths:

    f = open( file, "r" )
    if f:
        f.readline() # Pula cabecario
        values = f.readline().split() # Le valores da segunda linha
        jobs = int(values[0])
        machines = int(values[1])
        print(file)
        #print(tasks)
        #print(jobs)
        #print()
        f.readline() # Pula terceira linha

        lista = []

        x = 0
        while x < machines:
            line = f.readline().split()
            lista_num = []
            for num in line:
                lista_num.append(int(num))
            lista.append(lista_num)
            #lista.append(line)
            #print(line)
            x += 1
        #print(lista)
        result.append(lista)

#for x in result:
#    print(x)
#    print()

print('---------------------------------')

print(result[0][0])
print()

perm = list(range(len(result[0][0])))

print(perm)
random.shuffle(perm)
print()
print(perm)
