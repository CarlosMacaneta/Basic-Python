produtos = []
janela = True
while janela == True:
    escolha = input("1-Registar Produto\n2-Listar Produtos\n3-Alterar dados de produto\n4-Remover Produtos\n5-Sair\n")
    if escolha == "1":
        produtos.append(input("Nome: "))
    elif escolha == "2":
        if produtos is not None:
            print(produtos)
        else: print("Lista Vazia")
    elif escolha == "3":
        prod = input("Insira o nome do produto que deseja alteral\n")
        found = False
        position = 0
        if produtos is not None:
            for i in range(len(produtos)):
                if prod == produtos[i]:
                    found = True
                    position = i
            if found == True:
                novo = input("Novo nome: ")
                produtos.remove(prod)
                produtos.insert(position, novo)
                print("Poduto Alterado")
            else: print("Nome nao encontrado")
        else: print("Lista Vazia")
    elif escolha == "4":
        encontra = False
        prod = input("Insira o nome do produto que deseja Remover\n")
        for i in range(len(produtos)):
            if prod in produtos:
                encontra = True
        if encontra == True:
            produtos.remove(prod)
            print("Poduto Removido")
        else: print("Poduto nao encontrado")
    elif escolha == "5":
        janela = False
    else: print("Opcao Invalida")



