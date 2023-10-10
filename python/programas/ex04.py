'''
Faça um programa em Python que solicite a data de nascimento (dd/mm/aaaa)
 do usuário e imprima a data com o nome do mês por extenso
'''

str_data = input("Digite uma data no formato dd/mm/yyyy: ")

lista_data = str_data.split("/")

mes = lista_data[1]

match mes:
    case "01":
        mes_extenso = "janeiro"
    case "02":
        mes_extenso = "fevereiro"
    case "03":
        mes_extenso = "março"
    case "04":
        mes_extenso = "abril"
    case "05":
        mes_extenso = "maio"
    case "06":
        mes_extenso = "junho"
    case "07":
        mes_extenso = "julho"
    case "08":
        mes_extenso = "agosto"
    case "09":
        mes_extenso = "setembro"
    case "10":
        mes_extenso = "outubro"
    case "11":
        mes_extenso = "novembro"
    case "12":
        mes_extenso = "dezembro"

data_extenso = lista_data[0]+" de "+mes_extenso+" de "+lista_data[2]

print(data_extenso)