nome = input("qual é o nome do paciente?: ")
peso = float(input("quanto ele pesa?: "))
altura = float(input("qual a altura dele?: "))
IMC = peso/(altura*altura)

if IMC <= 18.5:
    print(f"{nome} está abaixo do peso {IMC}")
elif IMC <= 24.9:
    print(f"{nome} está com o peso normal {IMC}")
elif IMC <= 29.9:
    print(f"{nome} está acima do peso {IMC}")
elif IMC <= 34.9:
    print(f"{nome} está com obesidade grau I {IMC}")
elif IMC <= 39.9:
    print(f"{nome} está com obesidade grau II {IMC}")
else:
    print(f"{nome} está com obesidade grau III {IMC}")
