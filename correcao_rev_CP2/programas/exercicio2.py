'''
A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Escreva um
programa em Python para coletar dados sobre o salário e número de filhos de cada habitante e
após as leituras, escrever:

a) Média de salário da população

b) Média do número de filhos

c) Maior salário dos habitantes

d) Percentual de pessoas com salário menor que R$ 150,00

Obs.: O final das leituras dos dados se dará com a entrada de um “salário negativo”.
Utilize a estrutura de repetição “while”.
'''

soma_salarios = 0
soma_nrofilhos = 0
qtde_habit = 0
qtde_pessoas_salario_menor_150 = 0

salario = float(input("Digite o salário do habitante: "))
nro_filhos = int(input("Digite o número de filhos do habitante: "))

while (salario >= 0):
    soma_salarios+=salario
    soma_nrofilhos+=nro_filhos
    qtde_habit+=1
    if (salario < 150):
        qtde_pessoas_salario_menor_150+=1

    if (qtde_habit == 1): # considerar o salário do primeiro habit. como o maior
        maior_salario = salario
    else:
        if (salario > maior_salario):
            maior_salario = salario

    salario = float(input("Digite o salário do habitante: "))
    nro_filhos = int(input("Digite o número de filhos do habitante: "))

media_salarios = soma_salarios / qtde_habit
media_nrofilhos = soma_nrofilhos / qtde_habit
percent_menor_150 = (qtde_pessoas_salario_menor_150 / qtde_habit) * 100

print(f"Média dos salários: {media_salarios:.2f}")
print(f"Média do nro de filhos: {media_nrofilhos:.2f}")
print(f"Maior salário: {maior_salario:.2f}")
print(f"Percentual de pessoas com salário menor que R$ 150,00: {percent_menor_150}%")



