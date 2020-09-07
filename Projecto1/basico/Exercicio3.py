import os.path
import random


def gerar_id():
    return "AZ" + str(random.randrange(1, 1000))


def designar_arq():
    return gerar_id() + ".txt"


def formulario(fich):
    fich.write("Id: " + gerar_id() + "\n")
    fich.write("Nome: " + input("Nome: ").capitalize() + "\n")
    fich.write("Perfil: Docente\n")
    fich.write(input("Nome usuario: ") + "\n")
    fich.write(input("Palavra-passe: ") + "\n")
    fich.close()


path = "professor.txt"


def fill_up_list():
    users = []
    with open(path) as arquivo:
        for user in arquivo:
            users.append(user.strip())
    return users


def registar_prof(registar):
    if registar:
        arq = open(path, "w")
        formulario(arq)
    else:
        if fill_up_list() is None:
            fich = open(path, "w")
            formulario(fich)
        else:
            fich = open(path, "a")
            formulario(fich)


def login(username, password):
    found = False
    for i in range(len(fill_up_list())):
        if username and password in fill_up_list():
            found = True
    if found:
        return True
    else:
        return False


def registar_est():
    codigo_est = int(input("Codigo do estudade: "))
    est = open(codigo_est+".txt","w")
    est.write("Codigo: " + str(codigo_est)+"\n")
    est.write("Nome do estudade: " + input("Nome do estudante"))
    est.write("Curso: "+ input("Curso"))
    est.close()


def pesquisar_est(codigo_est):
    est = []
    if os.path.exists(str(codigo_est) + ".txt"):
        with open(str(codigo_est) + ".txt") as arquivo:
            for estudante in arquivo:
                est.append(estudante.strip())
    return est


def actualizar_est(codigo_est):
    found = False
    for i in range(len(pesquisar_est(codigo_est))):
        if "Codigo: "+codigo_est in pesquisar_est(codigo_est):
            found = True
    if found:
        print(pesquisar_est(codigo_est)[0])
        print()


def main():
    if not os.path.exists(path):
        registar_prof(registar=True)
    elif login(input("Nome de usuario: "), input("Palavra-passe: ")):
        print("CONSEGUIU")
    else:
        print("Nome de usuario ou palavra-passe incorrecto")


main()
