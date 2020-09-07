jogador = {}
jogadores = []
golos = []


def play():
    jogador["nome"] = input("Nome do jogador: ").upper()
    partidas = int(input("Quantas partidas %s" % jogador["nome"] + " jogou? "))

    for i in range(partidas):
        golos.append(int(input("Quantas golos na partida " + str(i + 1) + ": ")))

    jogador["golos"] = golos
    jogador["total"] = sum(golos)

    jogadores.append(jogador.copy())
    #ranking(partidas)

    resp = input("Quer continuar? [S/N] => ").upper()[0]
    if resp == "S":
        print(30*"-")
        jogador.clear()
        golos.clear()
        play()
    elif resp == "N":
        print(40*"-")
        ranking()

"""def ranking(partidas):
    print(30 * "-=")
    print(jogador)
    print(30 * "-=")

    for k, v in jogador.items():
        print(f"O campo {k} tem o valor {v}")

    print(30 * "-=")
    print("O jogador %s" % jogador["nome"] + " jogou %i" % partidas, " partidas")
    for i, v in enumerate(golos):
        print(f"\t=> Na partida %i" % (i + 1), ", fez %i" % v, "golos")

    print("Foi um total de %i" % sum(golos), " golos")"""


def ranking():
    print("cod ", end="")
    for chave in jogador.keys():
        print(f"{chave:<15}", end="")
    print()
    print(40 * "-")
    for k, v in enumerate(jogadores):
        print(f"{(k+1):>3} ", end="")
        for dado in v.values():
            print(f"{str(dado):<15}", end="")
        print()
    print(40*"-")


def main():
    play()


main()
