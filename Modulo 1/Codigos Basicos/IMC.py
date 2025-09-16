nome = str(input("qual o nome do paciente?:" ))
peso = float(input("qual o peso do paciente?:" ))
altura = float(input("qual a altura do paciente?: "))
IMC = peso / (altura * altura)

if IMC <= 18.5:
    print(f" {nome} Está Abaixo do Peso {IMC}")
elif IMC <= 24.9:
    print(f" {nome} Está com Peso Normal {IMC}")
elif IMC <= 29.9:
    print(f" {nome} Está com Sobrepeso {IMC}")
elif IMC <= 34.9:
    print(f" {nome} Está com Obesidade Grai I {IMC}")
elif IMC <= 39.9:
    print(f" {nome} Está com Obesidade Grau II {IMC}")
else:
     print(f" {nome} Está com Obesidade Grau III {IMC}")
