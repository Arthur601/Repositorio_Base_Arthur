numero = int(input("Digite um número: "))
opção = input("Digite 's' para repetir a ação ou qualquer outra tecla para sair: ")

if  numero % 2 == 0:
    print(f"{numero} é par")
elif numero % 2 == 1:
    print(f"{numero} é ímpar")
while opção == 's':
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f"{numero} é par")
    elif numero % 2 == 1:
        print(f"{numero} é ímpar")
    opção = input("Digite 's' para repetir a ação ou qualquer outra tecla para sair: ")
