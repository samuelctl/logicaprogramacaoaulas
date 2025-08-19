'''programa: Adivinhação V.1.0'''
'''# importando lib

from random import randint

print('Tente adivinhar o numero! ')
num1 = int(input('Digite um numero: '))

num_secreto = randint(1,10)

if num1 == num_secreto:
    print("Parabens,voce acertou!! ")
else:
    print(f'Voce perdeu o numero correto era: {num_secreto}')'''

#LINK - Versao 2.0
import random
import os
import time

numero_secreto = random.randint(1,1000)

tentativas = 0
max = 10
acertou = False

print(30*'-', 'Bem-Vindo ao AdivinhaLogo', 30*'-')
print(f'Voce tem {max} tentativas para adivinhar o numero secreto entre 1 e 100 ')
print('Vamos comecar?')

while tentativas < max:
    try:
        # entrada do usuario
        palpite = int(input('Digite o seu palpite: '))
    
    except ValueError:
        print('Por Favor, Digite um numero valido. ')
        continue

    tentativas += 1

    # verificar palpite

    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print('Tente um numero maior!')
        time.sleep(1.5)
        os.system('cls')
    else:
        print('Tente um numero menor!')
        time.sleep(1.5)
        os.system('cls')

if acertou:
    print(f'Parabens voce ganhou! Voce acertou o {numero_secreto} em {tentativas} tentativas')
else:
    print(f'Que pena! Voce nao acertou o numero secreto:{numero_secreto}')