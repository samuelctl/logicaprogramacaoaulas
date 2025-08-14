# revisao

'''nome = "samuel"
idade = 16

print(type(nome)) #ver o tipo de dados da variavel

idade = float(idade)

print(f'O meu nome é {nome} {type(nome)} tenho {idade} anos de idade')

nome_usuario = input('Digite seu nome: ') #padrao string

peso = float(input("Digite seu peso"). replace(',',"."). lower())

if peso >= 50: # verifica se e verdade
    print("Acima de 50 kilos")
else: #se nao for verdadeiro
    print("Abaixo de 50 kilos.")'''

'''Problema: crie um sistema de indice corporal(IMC) do usuario mostre na tela seu peso e se precisa emagracer ou engordar mais.Utilize a tabela do IMC para definir os valores
imc = peso / (altura * altura)

Abaixo do peso
Menos de 18,5
Peso normal
18,5 a 24,9
Sobrepeso
25 a 29,9
Obesidade grau I
30 a 34,9
Obesidade grau II
35 a 39,9
Obesidade grau III
40 ou mais'''


'''print(40*'=', 'CALCULADORA DE IMC', 40*"=")
altura = float(input('DIgite a sua altura: ').replace(',','.'))
peso = float(input("Digite o seu peso: ").replace(',','.'))

imc = peso / (altura * altura)

print()
print(f'Seu IMC é: {imc:.2f}')
if imc <= 18.5:
    print('Abaixo do normal')
elif imc <= 24.9:
    print('Normal')
elif imc <= 29.9:
    print('Sobrepeso')
elif imc <= 34.9:
    print('Obesidade grau I')
elif imc <= 34.9:
    print("Obesidade grau II")
elif imc <= 39.9:
    print('Obesidade grau III')
else:
    print('Obesidade grau III')'''
'''Problema 2: Um elevador de carga possui capacidade para 200kg. Crie um programa que receba do usuario seu peso e o peso da carga e verifica se a carga está autorizada a usar o elevador ou não.'''
#SECTION - Atividade de if,else e elif

'''print(40*'=''Problema 2',40*'=')
peso1 = float(input("Digite seu peso: ").replace(',','.'))
carga = float(input('Digite o peso da carga: ').replace(',','.'))
carga_final = carga + peso1
if carga_final >= 200:
    print('A carga não está autorizada a entrar no elevador')
else:
    print("A carga está autorizada a entrar no elevador")
print(f'A carga final é {carga_final:.2f}')
# codigo para identificar se o elevador aguenta o peso do usuario e da carga'''

#FIXME - Lacos de repeticao
'''numero = 10
while numero >= 0:
    print(numero)
    numero -= 1'''

'''cont = 0

while cont < 10:
    cont += 1
    if cont % 2 == 0:
        print(cont)
    else:
        continue

    print('Contando')'''

'''cont = 0 

while cont < 15:
    cont += 1 
    if cont % 2 == 0:
        print(cont)
    elif cont >= 7:
        break
    else:
        continue

    print('Contando')'''

'''print(40*'=', 'CALCULADORA DE IMC', 40*"=")

while True:
    altura = float(input('DIgite a sua altura: ').replace(',','.'))
    peso = float(input("Digite o seu peso: ").replace(',','.'))

    imc = peso / (altura * altura)

    print()
    print(f'Seu IMC é: {imc:.2f}')
    if imc <= 18.5:
        print('Abaixo do normal')
    elif imc <= 24.9:
        print('Normal')
    elif imc <= 29.9:
        print('Sobrepeso')
    elif imc <= 34.9:
        print('Obesidade grau I')
    elif imc <= 34.9:
        print("Obesidade grau II")
    elif imc <= 39.9:
        print('Obesidade grau III')
    else:
        print('Obesidade grau III')
    
    opcao = input('Deseja calcular novamente? S - sim | N - Nao: ').lower()

    if opcao == 's':
        continue
    elif opcao == 'n':
        print('Saindo do Sistema!')
        break
    else:
        print('Opcao invalida')
        break'''
'''print(40*'=', ' CADASTRO DO USARIO ', 40*"=")
nome = input('Digite seu nome: ').upper()
cpf = input('Digite seu cpf: ')
telefone = int(input('Digite seu telefone: '))
anonasc = int(input('Digite o seu ano de nascimento: '))
print(80*'=')
while True:
    print(40*'=', 'Sistema console 2ds', 40*"=")
    print()
    print('1 - Calculadora IMC')
    print('2 - Maioridade')
    print('3 - Calculadora')
    print('4 - Dados pessoais')
    print('5 - Feliz Natal')
    print('6 - Sair')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        while True:
            altura = float(input('DIgite a sua altura: ').replace(',','.'))
            peso = float(input("Digite o seu peso: ").replace(',','.'))

            imc = peso / (altura * altura)

            print()
            print(f'Seu IMC é: {imc:.2f}')
            if imc <= 18.5:
                print('Abaixo do normal')
            elif imc <= 24.9:
                print('Normal')
            elif imc <= 29.9:
                print('Sobrepeso')
            elif imc <= 34.9:
                print('Obesidade grau I')
            elif imc <= 34.9:
                print("Obesidade grau II")
            elif imc <= 39.9:
                print('Obesidade grau III')
            else:
                print('Obesidade grau III')
            
            opcao = input('Deseja calcular novamente? S - sim | N - Nao: ').lower()

            if opcao == 's':
                continue
            elif opcao == 'n':
                print('Saindo do Sistema!')
                break
            else:
                print('Opcao invalida')
                break
        
    elif opcao == '2':
        ano_atual = 2025
        idade = ano_atual - anonasc
        print(nome, 'é maior de idade.' if idade >= 18 else 'é menor de idade.')

    elif opcao == '3':
        print("Calculadora")
        
        
        while True:
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
                print("1 - soma")
                print("2 - Divisão")
                print("3 - Subtração")
                print("4 - Multiplicação")
                print("5 - Expoente")
                print("6 - sair")

                opcao_calculo = input('Escolha uma operação matemática: ')

                

                if opcao_calculo == '1':
                    print(f'Resultado da soma é: {num1 + num2}')
                elif opcao_calculo == '2':
                    print(f'Resultado da divisão é: {num1/num2}')
                elif opcao_calculo == "3":
                    print(f'Resultado da subtração é: {num1 - num2}')
                elif opcao_calculo == '4':
                    print(f'Resultado da multiplicação é: {num1 * num2}')
                elif opcao_calculo == '5':
                    print(f'Resultado da exponenciação é: {num1 ** num2}')
                elif opcao_calculo == '6':
                    break
                else:
                    print("Opção Inválida")



        
    elif opcao == '4':
        print(50*'-')
        print(f'Nome: {nome} | Telefone: {telefone} |')
        print(f'CPF: {cpf} | Data de nascimento {anonasc} |')
        ...
    elif opcao == '5':
        linhas = 15
        i = 1

        while i <= linhas:
            espacos = linhas - i
            estrelas = 2 * i- 1 

            print(' ' * espacos + '*' * estrelas)
            i +=1


    elif opcao == '6':
        print('Saindo do sistema!')
        break
    else:
        print('Opcao invalida!')
'''
#LINK - Fim da
nome = 'samuel'

for i in nome:
    print(i.replace(i,"*"))

    
    
    


    