numero = int(input("qual número da tabuada?: "))
numero_inicio = int(input("qual número começa?: "))
numero_fim = int(input("qual número final?: "))

while numero_inicio <= numero_fim:
   print(f"{numero_inicio} x {numero} = {numero_inicio * numero}")
   numero_inicio += 1
