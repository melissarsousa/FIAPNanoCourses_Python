import socket

resposta = "S"
while (resposta == "S"):
    url = input("Digite uma url: ")
    ip = socket.gethostbyname(url)
    print("O IP referente à url informada é: ", ip)
    resposta = input("Digite <s> para continuar: ").upper()
