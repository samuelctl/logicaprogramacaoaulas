import os
valor = 0
lista_cadastro = []
conta = 1001
def cadastrar():
    lista_cadastro.append(input('Digite seu nome: '))
    lista_cadastro.append(input('Digite sua idade: '))
    lista_cadastro.append(input('Digite seu cpf: '))
    print('-'*20,'Conta Criada com Sucesso!!', 20*'-')
    return

def exibir_dados():
    print('-'*20, f'Seja Bem-Vindo Ao Banco Secoob!','-'*20)
    print(f"nome: {lista_cadastro[0]}")
    print(f"idade: {lista_cadastro[1]}")
    print(f"cpf: {lista_cadastro[2]}")
    print('-'*57)
    return
print('-'*57)
print()
def deposito():
    global valor
    print('-'*57)
    valor += float(input('Digite o valor do depósito: '))
    print(f'O seu saldo é: {valor}')
    print('-'*57)
    return
def saque():
    global valor
    saque1 = float(input('Digite o valor que deseja sacar: '))
    if valor < saque1:
        print('Você não tem saldo suficiente!')
    else:
        print('Saque bem-sucedido!')
    valor = valor - saque1
    print(f'O seu saldo é: {valor}')
    print('-'*57)
    return



def encerrar():
    global valor
    del(lista_cadastro)
    print(f'A conta | {lista_cadastro} |\nFoi deletada!')
    print('-'*57)
    valor = 0

def menu():
    p = [['1 - Criar conta'],
        ['2 - Exibir dados da conta'], 
            ['3 - Depositar'], 
            ['4 - Sacar'], 
            ['5 - Sair'],
            ['6 - Encerrar conta']]
    for i in p:
        print(i)
    opcao = input('Digite a opção desejada: ')
    match opcao:
        case '1':
            cadastrar()
        case '2':
            exibir_dados()
        case'3':
            deposito()
        case '4':
            saque()
        case '5':
            sair()
        case '6':
            encerrar()
def sair():
    print('-'*20, "Saindo do sistema...",20*'-')
    exit()
    
while True:
    menu()
    
    


    

