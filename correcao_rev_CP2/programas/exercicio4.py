'''
Escreva um programa em Python para ler uma lista A com 10 elementos numéricos inteiros.
Apresentar o total de elementos ímpares existentes na lista e o percentual do valor total de
números ímpares em relação à quantidade total de elementos armazenados na lista.
'''

lista_numeros = []
qtde_numeros_impares = 0

for i in range(10):
    lista_numeros.append(int(input("Digite um elemento da lista: ")))

for i in range(10):
    if (lista_numeros[i] % 2 != 0):
        qtde_numeros_impares+=1

percent_impares = (qtde_numeros_impares / 10) * 100

print(f"Quantidade de números ímpares: {qtde_numeros_impares}")
print(f"Percentual de números ímpares: {percent_impares}%")
