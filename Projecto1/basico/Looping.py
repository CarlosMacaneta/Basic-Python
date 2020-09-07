print("Tabuada")
print("\nMultiplicacao")

numero =  int(input("Numero: "))

tabuada = 1

while tabuada < 13:
    resultado = tabuada * numero
    print(numero, "*", tabuada, "=", resultado)
    tabuada += 1
else:
    print("Fim")


print("\nAdicao")

for i in range(1, 13):
    resultado = i + numero
    tabuada = i
    print(numero, "+", i, "=", resultado)
    tabuada += 1