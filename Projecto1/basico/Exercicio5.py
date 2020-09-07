import random
from time import sleep
from operator import itemgetter

jogador1 = random.randrange(1, 6)
jogador2 = random.randrange(1, 6)
jogador3 = random.randrange(1, 6)
jogador4 = random.randrange(1, 6)

jogadores = {"jogador1": jogador1,
             "jogador2": jogador2,
             "jogador3": jogador3,
             "jogador4": jogador4
             }
print("Valores sorteados:")
for k, v in jogadores.items():
    print(f"\tO {k} tirou {v}")
    sleep(1)

print(20*"-=")
print("Ranking dos jogadores")

resultados = {}
resultados = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(resultados):
    print(f"\t{i+1}º lugar: {v[0]} com {v[1]}")
    sleep(1)
