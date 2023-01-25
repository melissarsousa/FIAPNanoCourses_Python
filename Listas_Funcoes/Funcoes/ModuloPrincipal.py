from Listas_Funcoes.Funcoes.Funcoes_Modularizacao import *

minhaLista = []

print("Preenchendo")
preencherinventario(minhaLista)

print("Exibindo")
exibirinventario(minhaLista)

print("Pesquisando")
localizarpornome(minhaLista)

print("Alterando")
depreciarpornome(minhaLista, 20)

print("Excluindo")
print(excluirporserial(minhaLista))
exibirinventario(minhaLista)

print("Resumindo")
resumirvalores(minhaLista)
