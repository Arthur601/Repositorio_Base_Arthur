emocao = int(input("qual o grau de sua emoção?: "))
sentimento = int(input("qual o grau de seu sentimento: "))

while emocao < sentimento:
   print(" i'm mr lonely ")
   emocao += 1

while emocao > sentimento:
   print(" you win !!!")
   sentimento = 1
