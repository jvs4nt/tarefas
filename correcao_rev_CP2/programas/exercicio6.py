'''
Escreva um programa em Python para ler duas listas A e B com 10 elementos cada.
Construir uma lista C, sendo esta a junção das 2 outras listas. Desta forma C
deve ter o dobro de elementos em relação às listas A e B, ou seja, a lista C
deverá possuir 20 elementos. Apresentar a lista C.
'''

listaA = []
listaB = []
listaC = []

for i in range(10):
    listaA.append(int(input("Digite um elemento da lista A: ")))
    listaB.append(int(input("Digite um elemento da lista B: ")))

for i in range(10):
    listaC.append(listaA[i])

for i in range(10):
    listaC.append(listaB[i])

print(listaA)
print(listaB)
print(listaC)

