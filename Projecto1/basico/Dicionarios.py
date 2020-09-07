pessoa = {}
pessoas = []

for i in range(2):
    pessoa["nome"] = input("Nome: ")
    pessoa["idade"] = int(input("Idade: "))
    pessoas.append(pessoa.copy())

print(10*"\n")
for p in pessoas:
    for k, v in p.items():
        print(f"{k}: {v}")

