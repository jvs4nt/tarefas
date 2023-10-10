strData = input("digite uma data no formato dd/mm/yyyy: ")

listaData = strData.split("/")

mes = listaData[1]

match mes:
    case "01":
        mesExtenso = "janeiro"
    case "02":
        mesExtenso = "fevereiro"
    case "03":
        mesExtenso = "marco"
    case "04":
        mesExtenso = "abril"
    case "05":
        mesExtenso = "maio"
    case "06":
        mesExtenso = "junho"
    case "07":
        mesExtenso = "julho"
    case "08":
        mesExtenso = "agosto"
    case "09":
        mesExtenso = "setembro"
    case "10":
        mesExtenso = "outubro"
    case "11":
        mesExtenso = "novembro"
    case "12":
        mesExtenso = "dezembro"

dataExtenso = listaData[0] + " de " + mesExtenso + " de " + listaData[2]

print(f"Data: {dataExtenso}")