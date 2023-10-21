'''
Escreva um programa em Python para ler 15 elementos de uma lista A. Construir uma
lista B, observando a seguinte lei de formação:
Todo elemento de B deve ser o quadrado do elemento de A correspondente. Apresentar as listas A e B.
'''

listaA = []
listaB = []

for i in range(15):
    listaA.append(int(input("Digite um elemento da lista A: ")))

for i in range(15):
    listaB.append(listaA[i]**2)

print(listaA)
print(listaB)