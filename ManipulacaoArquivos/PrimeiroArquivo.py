with open("teste.txt", "a") as arquivo:
    arquivo.write("Bsinho e Bsinha.")
    arquivo.write("\nFamília Tikuna.")
    arquivo.write("\n")

with open("teste.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
