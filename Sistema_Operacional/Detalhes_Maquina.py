import platform
import getpass
from datetime import datetime

print("Distribuição do Sistema Operacional.: ", platform.platform())
print("Nome do Sistema Operacional.........: ", platform.system())
print("Versão do Sistema Operacional.......: ", platform.release())
print("Arquitetura.........................: ", platform.architecture())
print("Nome do Computador..................: ", platform.node())
print("Tipo de Máquina.....................: ", platform.machine())
print("Processador.........................: ", platform.processor())
print("Versão do Python....................: ", platform.python_version())

print(datetime.now())
print(datetime.now().hour)

usuario = print(getpass.getuser())
senha = print(getpass.getpass("Digite sua senha:..."))

if usuario == 'usertricaster' and senha == 'hello_python':
    print('Bem-vinda Adele')
else:
    print('Você não tem acesso')
