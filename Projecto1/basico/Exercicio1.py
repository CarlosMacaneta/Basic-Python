numeros = [12,	-2,	4,	8, 29, 45,	78,	36,	-17, 2,	12,	8,	3,	3,	-52]

print("Maior numero:", max(numeros))
print("Menor numero:", min(numeros))
print("Pares:", (numeros[0:4:2] + numeros[3:4] + numeros[6:8:1] + numeros[9:12:1]))
print("Numeros de ocorrendcias do primeiro elemento:", numeros.count(12))
print("Media dos elementos: %.2f" % (sum(numeros)/len(numeros)))
print("Soma de valores negativos:", sum((numeros[1:2:1] + numeros[8:9:1] + numeros[14::])))