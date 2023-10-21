'''
O gerente de um bar precisa fazer um levantamento do movimento no final do expediente.
Basicamente, o bar oferece um menu (tabela abaixo) onde cada item tem um código associado.
Considerando que ele tem uma relação das comandas com as quantidades consumidas por mesa,
escreva um programa em Python faça a leitura do código e da quantidade de cada item até que o
usuário digite 0 (1-continuar e 0-parar). Calcule o total para cada comanda baseado nas quantidades
de porções e cervejas consumidas e o valor total geral do dia. Para tanto, utilize a estrutura de
repetição “while”.
'''

resp = 1
total = 0

while (resp != 0):
    print("print com os códigos, produtos e valores")
    cod = int(input("Digite o código desejado: "))
    qtde = int(input("Digite a quantidade desejada: "))
    match cod:
        case 1:
            total += qtde * 35.00
        case 2:
            total += qtde * 25.00
        case 3:
            total += qtde * 40.00
        case 4:
            total += qtde * 55.00
        case 5:
            total += qtde * 18.00
        case _:
            print("Código inválido")

    resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))

print(f"O total geral do movimento do dia é {total:.2f}")