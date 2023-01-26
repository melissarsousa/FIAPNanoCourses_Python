texto = "Bergson e Bergsa"

print(texto[0:7])
print(texto[10:])
print(texto[-6:])
print(texto[::-1])

print(texto.find("B"))
print(texto[texto.find("B") + 1:].find("B"))

print(texto.split(" "))
