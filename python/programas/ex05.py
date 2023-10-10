# versão da data por extenso mais compacta

meses = ("janeiro", "fevereiro", "março", "abril", "maio," "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

str_data = input("Digite uma data no formato dd/mm/yyyy: ")

lista_data = str_data.split("/")

data_extenso = lista_data[0]+" de "+meses[int(lista_data[1])-1]+" de "+lista_data[2]

print(data_extenso)