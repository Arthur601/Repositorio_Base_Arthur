opcao = int(input("Digite o que deseja fazer: \n1- Fazer PIX \n2- Extrato \n3- Depositar \n4- Sair "))
if opcao == 1:
    valor = input("Digite o valor do PIX: ")
    quem = input("Digite o nome de quem receberá o PIX: ")  
    print(f"PIX de R${valor} para {quem} realizado com sucesso!")
elif opcao == 2:
    print("Extrato bancário:")
elif opcao == 3:
    valor = input("Digite o valor do depósito: ")
    print(f"Depósito de R${valor} realizado com sucesso!")
elif opcao == 4:
    print("Saindo do sistema.")
else:
    print("Opção inválida. Por favor, tente novamente.")
    while True:
        opcao = int(input("Digite o que deseja fazer: \n1- Fazer PIX \n2- Extrato \n3- Depositar \n4- Sair "))
        if opcao == 1:
            valor = input("Digite o valor do PIX: ")
            quem = input("Digite o nome de quem receberá o PIX: ")  
            print(f"PIX de R${valor} para {quem} realizado com sucesso!")
            break
        elif opcao == 2:
            print("Extrato bancário:")
            break
        elif opcao == 3:
            valor = input("Digite o valor do depósito: ")
            print(f"Depósito de R${valor} realizado com sucesso!")
            break
        elif opcao == 4:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
