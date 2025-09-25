import random
lista = ['leao','gato','foca']
def forca():
   pala = random.choice(lista)
   escondida = "-" * len(pala)
   print(escondida)
   print(pala)
forca()