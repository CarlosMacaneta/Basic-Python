disciplina = []
notas = []
pesos = []
count = 0
media = 0.0

n = int(input("Numero de testes: "))
for i in range(n):
    notas.append(float(input("Teste: ")))
    pesos.append(float(input("Peso do teste: ")))

    if 0 > notas[i] > 20:
        print("O teste nao pode ter uma nota inferior a 0 e superior a 20.")
    elif 0 > pesos[i] > 1:
        print("O peso nao pode ser superior a 1 e inderior a 0.")
    elif notas[i] < 10:
        count += 1
    else:
        media += (notas[i] * pesos[i])
print("\n")

for i, nota in enumerate(notas):
    print("Teste", (i+1), ":", nota)
    print("Peso", (i+1), ":", pesos[i])
    print(20*"-")
if media < 10:
    print("Excluido, Media: %.2f" %media)
elif 10 <= media < 14:
    print("Admitido, Media: %.2f" %media)
elif count >= 1:
    print("Admitido, Media: %.2f" %media)
elif 14 <= media <= 20:
    print("Dispensado, Media: %.2f" %media)
print()