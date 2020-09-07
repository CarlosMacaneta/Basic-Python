from conta import Conta
import random


def back():
    while True:
        resp = str(input("Voltar [V] => ").upper()[0])
        if resp in "V":
            break
        else:
            print("Opcao invalida")


def main():
    contas = []
    conta = {}
    while True:

        opcao = int(input("[1] Criar conta\n[2] Listar dados\n[3] Actulizar dados\n[4] Remover conta"
                          + "\n[5] Depositar saldo\n[6] Levantar\n[7] Transferir\n[8] Sair\n>>> "))

        if opcao == 1:
            account = Conta(random.randint(1000000, 10000000), input("Nome: "), float(input("Saldo: ")))
            conta["numero"] = account.numero
            conta["titular"] = account.titular
            conta["saldo"] = account.saldo
            contas.append(conta.copy())
            print("Cliente registado com sucesso.")
        elif opcao == 2:
            for c in contas:
                for k, v in c.items():
                    print(30 * "-=")
                    print(f"{k}: {v}")
                print(30*"-=")
            back()
        elif opcao == 3:
            numero = int(input("Numero da conta: "))
            for i, val in enumerate(contas):
                if val.edit(numero):
                    print("Seu dados foram alterados com sucesso")
                    break
                else:
                    break
                    print("Cliente nao encontrado")
        elif opcao == 4:
            pass
        elif opcao == 5:
            nr_conta = int(input("Numero da conta: "))
            for i, values in enumerate(contas):
                if nr_conta == contas[i].numero:
                    valor = float(input("Valor de deposito: "))
                    values.deposita(nr_conta, valor)
                else:
                    print("O numero de conta nao exite")
                    break
            back()
        elif opcao == 7:
            nr_conta = int(input("Numero de conta: "))
            nr_conta2 = int(input("Numero de conta destino: "))
            for i, values in enumerate(contas):
                """tas.transferir(nr_conta, nr_conta2)"""
            back()
        elif opcao == 8:
            break


main()
