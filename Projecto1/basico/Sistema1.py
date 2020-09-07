import time

nome_prod = []
preco_prod = []

lojaAberta = True

while lojaAberta:
    encontrei = False
    print("[1] Registar produto\n[2] Listar produto\n[3] Alterar produto\n[4] Remover produto\n[5] Sair")
    print(18*"=")
    opcao = int(input(">>> "))
    if opcao == 1:
        print(10*"\n")
        nome_prod.append(input("Nome do produto: ").capitalize())
        preco_prod.append(float(input("Preco do produto: ")))
        print("\nproduto registado com sucesso")
        time.sleep(0.5)
        print(10*"\n")
    elif opcao == 2:
        print(0 * "\n")
        print("LISTA DE PRODUTOS\n"+25*"=")
        for i, nome_produ in enumerate(nome_prod):
            print("Nome do produto: "+nome_produ)
            print("Preco do produto :", preco_prod[i])
            print(25*"-")
        voltar = int(input("[1] Voltar: >>> "))
        if voltar == 1:
            time.sleep(2)
    elif opcao == 3:
        print(10 * "\n")
        nome_produto = input("Nome do produto: ").capitalize()
        for i, nome_prod_ in enumerate(nome_prod):
            if nome_produto == nome_prod:
                encontrei = True
        if encontrei:
            nome_prod[i] = input("Novo nome do produto: ")
            if nome_produto != nome_prod[i]:
                print("Alteracao efectuada com sucesso")
                time.sleep(2)
                print(10 * "\n")
            else:
                print("Nao houve alteracao do nome do produto")
                time.sleep(2)
                print(10 * "\n")
        else:
            print("Produto nao registado")
            time.sleep(2)
            print(10*"\n")
    elif opcao == 4:
        print(10 * "\n")
        nome_produto = input("Nome do produto: ").capitalize()
        for nome_prod_ in nome_prod:
            if nome_produto == nome_prod_:
                encontrei = True
        if encontrei:
            nome_prod.remove(nome_prod_)
            print("O produto: "+nome_prod_+" foi removido com sucesso")
            time.sleep(2)
            print(10*"\n")
        else:
            print("Produto nao registado")
            time.sleep(2)
            print(10*"\n")
    elif opcao == 5:
        lojaAberta = False
    else:
        print("Opcao invalida tente novamente")
        time.sleep(2)
        print(10 * "\n")