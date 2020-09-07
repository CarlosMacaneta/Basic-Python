class Conta():

    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def deposita(self, nr_conta, valor):
        if self.numero == nr_conta:
            self.saldo += valor
            print("Valor depositado com sucesso")
        else:
            print("Numero da conta introduzido nao existe")

    def levantar(self, nr_conta, valor):
        if self.numero == nr_conta:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                print("Saldo insuficiente.")
        else:
            print("Numero da conta introduzido nao exite")

    def verifica_saldo(self, nr_conta):
        if self.numero == nr_conta:
            print(f"Saldo: {self.saldo}")
        else:
            print("Numero de conta introduzido nao existe")

    def transferir(self, nr_conta, nr_conta2, valor):
        if self.numero == nr_conta:
            self.saldo -= valor
            for values in enumerate(self.numero):
                if values == nr_conta2:
                    self.saldo += valor
                else:
                    print("Numero de conta nao exite")
                    break
        else:
            print("Numero de conta nao existe")

