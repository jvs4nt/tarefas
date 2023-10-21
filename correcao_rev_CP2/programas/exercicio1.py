'''
Escreva um programa em Python para ler 10 valores e escrever quantos desses valores lidos
estão no intervalo [10,20] (incluindo os valores 10 e 20 no intervalo) e quantos deles estão
fora deste intervalo. Nesse caso, utilize a estrutura de repetição “for”.
'''

qtde_dentro_int = 0
qtde_fora_int = 0

for cont in range(10):
    num = int(input("Digite um número: "))
    if (num >= 10 and num <= 20):
        qtde_dentro_int+=1
    else:
        qtde_fora_int+=1

print(f"Quantidade de números no intervalo [10,20]: {qtde_dentro_int}")
print(f"Quantidade de números fora do intervalo [10,20]: {qtde_fora_int}")
