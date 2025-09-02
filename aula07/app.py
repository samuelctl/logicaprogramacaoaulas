#NOTE - Cadastro
import os 
def usuario(nome):
    return f'Olá {nome} oque deseja?'
nome, cadastro, saldo = input('Digite o seu nome: '), input('Digite a sua idade: '), 0.00
print('-'*20, f'Seja Bem-Vindo {nome} Ao Banco Secoob!','-'*20)
print('Cadastro concluído!')
while True:
    print(usuario(nome))
    p = [['1 - Exibir dados da conta'], 
            ['2 - Depositar'], 
            ['3 - Sacar'], 
            ['4 - Sair'],
            ['5 - Encerrar conta']]
    for i in p:
        print(i)

    opcao = input('Digite a opção escolhida: ')
    match opcao:
        case '1':
            print(f'Nome:{nome}\nIdade:{cadastro}\nSaldo:{saldo}')



