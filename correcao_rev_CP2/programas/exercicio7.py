'''
Elaborar um programa em Python que efetue o cálculo de uma tabuada de um número
qualquer e armazene os resultados em uma lista A para 11 elementos. Apresentar os
valores armazenados na lista.
'''

lista_tabuada = []

num_tab = int(input("Digite o número da tabuada que deseja: "))

for i in range(11):
    tabuada = num_tab * i
    lista_tabuada.append(tabuada)

print(lista_tabuada)