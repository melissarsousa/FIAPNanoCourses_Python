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
    salvar(dicionario)


def pesquisar(dicionario, usuario):
    lista = dicionario.get(usuario)
    if lista is not None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])


def excluir(dicionario, usuario):
    if dicionario.get(usuario) is not None:
        del dicionario[usuario]
        print("Usuário excluído")


def listar(dicionario):
    for usuario, dados in dicionario.items():
        print("Login: ", usuario)
        print("Dados:", dados)


def salvar(dicionario):
    with open("Banco_de_Dados.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))
