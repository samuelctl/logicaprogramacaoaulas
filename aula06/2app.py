#SECTION - Atividade
#REVIEW - Questão 1 - Divisão

'''num = float(input('Digite um num: '))
num2 = float(input('Digite outro num: '))
while True:
    num3 = num/num2
    print(f'O resultado é: {num3:.2f}')
    break
 
#REVIEW - Questão 2 - Conversão de temperatura F -> C
# fh = float(input('Digite a temperatura em Fahrenheit: '))
while True:
    c = (fh-32)/1.8
    print(f'A temperatura em Celsius é: {c}')
    break
#REVIEW - Questão 3 - Conversão de dolar para reais
dolar = float(input('Digite a quantia de dolares: '))
while True: 
    reais = dolar*5.41
    print(f'O valor de dolar em reais é: {reais:.2f} ')
    break

#REVIEW - Questão 4 - Média aritmetica
num1 = float(input('Digite um número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro: '))
while True:
    ari = (num1 + num2 + num3)/3
    print(f'O resultado da media aritmetica é: {ari}')
    break

#REVIEW - Questão 5 - Dados 
nome = input("Digite seu nome: ").title()
print(type (nome))

#REVIEW - Questão 6 - Lista e dobro
lista1 = []
lista2 = []
while True:
    while not len(lista1) == 10:
        lista = int(input('Digite um numeros: '))
        lista1.append(lista)
    for i in lista1:
        lista2.append(i *2)
    print(lista2)
    break'''

#REVIEW - Questao 7 - verfifcar numero
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite o segundo numero: '))
while True: 
    if numero1 >= numero2:
        print(f'O primeiro {numero1}, número é maior que o segundo número {numero2}!')
    else:
        print(f"O segundo número {numero2}, é maior que o primeiro número {numero1}")
        break

'''#REVIEW - Questão 8 - Cadastro
nome = input('Digite seu primeiro nome: ')
sob = input('Digite seu sobrenome: ')
nome2 = input('Digite o primeiro nome da segunda pessoa: ')
sob2 = input('Digite o novo sobrenome: ')
print(f"Olá {nome} {sob2} e {nome2 + sob}!!")'''