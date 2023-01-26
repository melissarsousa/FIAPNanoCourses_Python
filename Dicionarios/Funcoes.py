def perguntar():
    resposta = input("O que deseja realizar?\n" +
                     "<I> -Para Inserir um usuário\n" +
                     "<P> -Para Pesquisar um usuário\n" +
                     "<E> -Para Excluir um usuário\n" +
                     "<L> -Para Listar os usuários: ").upper()
    return resposta


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada: ").upper()]


def pesquisar(dicionario, usuario):
    lista = dicionario.get(usuario)
    if lista != None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir(dicionario, usuario):
    if dicionario.get(usuario) != None:
        del dicionario[usuario]
        print ("Usuário excluído")


def listar(dicionario):
    for usuario in dicionario:
        print(dicionario[usuario])

