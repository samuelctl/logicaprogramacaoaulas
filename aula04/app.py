#REVIEW - Aula 04

# importando biblbioteca
'''import os 
from time import sleep

cont = input('Digite um numero inteiro: ')

try:
    cont_int = int(cont)
    while cont_int >= 0:
        os.system('cls')
        print(f'Contagem regressiva: {cont_int}...')
        sleep(1)
        cont_int -= 1
        os.system('cls')
except:
    print('Digite um numero valido. ')

print('Fim da contagem!')'''
'''#SECTION - importando bibliotecas (lib)
import random

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')
nome5 = input('Digite o quinto nome: ')

lista_nomes = [nome1, nome2, nome3, nome4, nome5]

escolhido = random.choice(lista_nomes)
print(escolhido)'''


'''#SECTION - importando lib
import random
import os
import time

lista_nomes = []
lista_sorteados = []

while True:
    nome = input('Digite o nome para o sorteio: ')
    if nome:
        lista_nomes.append(nome)
    else:
        break

while True:
    if lista_nomes:
        os.system('cls')
        escolhido = random.choice(lista_nomes)
        lista_sorteados.append(escolhido)
        # excluí o sorteado da lista original
        
        pop - função, remove pelo indice
            pop() - remover o ultimo indice
            pop(0) - remove o indice 0
        del - instrução, remover item pelo indice, mais de um item
            del[3] - busca o indice 3 e remove ele
            del[2:10] - vai de 2 à 10
        
        
        if escolhido in lista_nomes:
            lista_nomes.remove(escolhido)
            print('Nome excluido')

        print(f'O escolhido foi: {escolhido} ')

    opcao = input("Deseja sortear outro nome? S -Sim \n| N - Não\n: ").lower()
    os.system('cls')

    if opcao != 's':
            break
    else:
        print('Não há nomes para serem sorteados! ')
print('Programa finalizados! ')
print(f'Os sorteados foram {lista_sorteados} ')'''


'''#SECTION - importando biblioteca (lib)

import random

lista = []

sair = False

while sair == False:
    nome_candidato = input('Digite os nomes para o sorteio ou enter para sair: ')
    if nome_candidato != "":
        # append - adiciona o valor da variavel dentro da lista
        lista.append(nome_candidato)
    else: 
        sair = True
escolhido = random.choice(lista)

print('Escolhido foi: ', escolhido)'''


'''programa: Adivinhação V.1.0'''
'''# importando lib

from random import randint

print('Tente adivinhar o numero! ')
num1 = int(input('Digite um numero: '))

num_secreto = randint(1,10)

if num1 == num_secreto:
    print("Parabens,voce acertou!! ")
else:
    print(f'Voce perdeu o numero correto era: {num_secreto}')

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
    print(f'Que pena! Voce nao acertou o numero secreto:{numero_secreto}')'''

#REVIEW - Join - Junta as coisas da lista
# split - separa as coisas da lista
# sort - ordem alfabetica ou numerica
meses_string = 'Janeiro Fevereiro Marco Abril Maio' 
meses_lista = meses_string.split(' ')
print(meses_lista)