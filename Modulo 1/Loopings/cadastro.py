nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
opcao = int(input(f"Nome: {nome}, Email: {email} estão corretos?:  \n1- sim \n2- não"))

if opcao == 1:
    print("Dados salvos com sucesso!")
    arquivo = open("game.txt", "a")
    arquivo.write(nome + " | " + email + "\n")
    arquivo.close()
else:
    opcaob = int(input("deseja tentar novamente?: \n1- sim \n2- não"))
    if opcaob == 1:
        while True:
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            opcao = int(input(f"Nome: {nome}, Email: {email} estão corretos?:  \n1- sim \n2- não"))
    else:
        print("Dados não salvos.")
        print("Obrigado por usar nosso sistema!")
        exit()
