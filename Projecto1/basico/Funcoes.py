def minha_func():
    print("Minha primeira funcao")


def func_parametro(x, y):
    soma = x + y
    print(soma)

minha_func()
func_parametro(int(input("Numero: ")), int(input("Numero: ")))

#funcao com parametro default
def login(usuario = "bitch", senha = "whore"):
    print("Usuario: ", usuario)
    print("Senha: ", senha)

login()

#updating
login("whore", "bitch")

#funcoes com retorno
