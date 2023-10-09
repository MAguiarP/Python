tupla1 = tuple(range(10))
print(tupla1)

tupla2 = ('Teste Python', 'Teste interativo') 
testePython, tipoInterativo = tupla2
print(testePython, tipoInterativo)

print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))
print(len(tupla1))

for indice, valor in enumerate(tupla1):
    print(indice, valor)


    