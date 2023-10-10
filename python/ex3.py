palavra = input("digite a palavra desejada: ")

if (palavra == palavra[::-1]):
    print("a palavra é um palindromo")
else:
    print("a palavra nao é um palindromo")