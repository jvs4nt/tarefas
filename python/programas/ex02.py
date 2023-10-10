'''
Dada uma string digitada pelo usuário,
crie um programa em Python que faça a contagem de vogais existentes nessa string.
'''

str_ex2 = input("Digite a string desejada: ")
qtde_vogais = 0
str_min = str_ex2.lower()

tam = len(str_min)

for i in range(tam):
    if (str_min[i]=="a" or str_min[i]=="e" or str_min[i]=="i" or str_min[i]=="o" or str_min[i]=="u"):
        qtde_vogais+=1

print(f"A quantidade de vogais na string é {qtde_vogais}")