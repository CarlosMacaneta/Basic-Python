funcionario = {}
funcionarios = []

funcionario["nome"] = input("Nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
funcionario["idade"] = 2020 - ano_nascimento
funcionario["ctps"] = int(input("Carteira de trabalho (0 nao tem): "))
if funcionario["ctps"] > 0:
    funcionario["contratacao"] = int(input("Ano de contratacao: "))
    funcionario["salario"] = float(input("Salario: "))
    funcionario["aposentadoria"] = (funcionario["contratacao"] + 35) - ano_nascimento
    for k, v in funcionario.items():
        print(f"{k}: {v}")
else:
    for k, v in funcionario.items():
        print(f"{k}: {v}")