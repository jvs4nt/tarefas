'''
Um palíndromo é um tipo de palavra ou frase que tem a propriedade de ser lida tanto da
direita para a esquerda quanto da esquerda para a direita. Como exemplo, temos a palavra “asa”.
Baseado nesse conceito, escreva um programa em Python que, dada uma palavra,
 verifique se ele é um palíndromo ou não. DICA: utiliza a notação de slice.
'''

palavra = input("Digite a palavra desejada: ")

if (palavra.lower() == palavra[::-1]):
    print("A palavra é um palindromo")
else:
    print("A palavra não é um palíndromo")