lista_de_compras = []

def cadastrar():
    item = input("Digite o produto que deseja adicionar: ")
    lista_de_compras.append(item)
    print("Produto adicionado com sucesso!")
def ver_lista():
    print("Lista de compras atual:")

def deletar_item():
    item = input("Digite o produto que deseja deletar: ")

def atualizar_lista():
    item = input("Digite o produto que deseja atualizar: ")
    if lista_de_compras:
        if item in lista_de_compras:
            novo_item = input("Digite o novo produto: ")
            index = lista_de_compras.index(item)
            lista_de_compras[index] = novo_item
            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado na lista.")

while True:
    print("\nMenu:")
    print("1. Cadastrar produto👜")
    print("2. Ver lista de compras📄")
    print("3. Atualizar lista de compras📱")
    print("4. Deletar item da lista❌")
    print("Digite 'sair' para encerrar o programa🔙")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        ver_lista()
    elif opcao == '3':
        atualizar_lista()
    elif opcao == '4':
        deletar_item()
       
    elif opcao.lower() == 'sair':
        print("Encerrando o programa...")
    else:
        print("Opção inválida, tente novamente.")
    print("Lista de compras:", lista_de_compras)
