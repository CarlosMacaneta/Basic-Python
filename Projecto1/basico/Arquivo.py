#Para criar arquivo
#var = open(nome do arquivo e sua extensao, modo de criacao)
#Modos existentes: w --write, a --append, r --read, rb --read binary

#criando arquivo
arquivo = open("arq1.txt", "w")

#escrevendo no arquivo
arquivo.write("Bitch")

#fechando arquivo
arquivo.close()

#lendo arquivo
#para ler um arquivo devemos abrir o arquivo e indicar o modo
#readline le apenas uma linha do arquivo
#read le todo arquivo

arquivo = open("arq1.txt", "r")
linha = arquivo.readline()

#imprimindo
print(linha)




















texto = []

#arquivo1 = open("arquivo1.txt", "w")
#arquivo2 = open("arquivo2.txt", "a")

#arquivo1.write("Carlos\n")
#arquivo1.close()

arquivo1 = open("arquivo1.txt", "a")
arquivo1.write("Carlos\n")
arquivo1.write("Macaneta\n")
#arquivo2.write("Carlos\n")
#arquivo2.write("Macaneta\n")

arquivo1.close()
#arquivo2.close()

arquivo1 = open("arquivo1.txt", "r")
#arquivo2 = open("arquivo2.txt", "r")

#linha1 = arquivo1.readline()
#linha2 = arquivo2.readline() #readline apenas le uma linha

print(arquivo1.read())
for palavras in arquivo1:
    palavras = palavras.strip()
    texto.append(palavras)

for i in range(len(texto)):
    if texto[i] is not None:
       pass
       # print(texto[i])
#print()
#print(linha1)
#print()
#print(linha2)