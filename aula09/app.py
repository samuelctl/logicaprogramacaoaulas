import os
import json
from time import sleep as delay

lista = []

with open("aula09/biblioteca.json", "r", encoding="utf-8") as f:
                   livro = dict(json.load(f))

def clear(): delay(1); return print('\033[H\033[J')

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

while True:
       print(40*'*','BEM VINDO A BIBLIOTECA', 40*'*')
       print('1 - Cadastrar novo livro.')
       print('2 - listar livros da biblioteca.')
       print('3 - atualizar algum livro da biblioteca.')
       print('4 - excluir livro da biblioteca.')
       print('5 - sair do sistema.')
       opcao = input('Informe a opção desejada: ')
       limpar()
       match opcao:
           case '1':
               livro['nome'].append(input('Informe o nome do livro: ').strip().title())
               livro['idade_indicativa'].append(input('Informe a idade indicativa do livro: '))
               livro['genero'].append(input('Digite o genero do livro: ').strip().lower())
               
               limpar()

               print('livro cadastradado com sucesso! ')

               

               with open("aula09/biblioteca.json", "w", encoding="utf-8") as f:
                   json.dump(livro, f, ensure_ascii=False, indent=4)

               continue
           case "2":
                if livro:
                    print(f"nome: {livro["nome"]}")
                    print(f"idade: {livro["idade_indicativa"]}")
                    print(f"genero: {livro["genero"]}")
                else:
                       print('nenhum livro encontrado na biblioteca!')
           case '3':
                nome = input('Informe o nome do livro que deseja atualizar: ').strip().lower()
                with open("aula09/biblioteca.json", 'r', encoding='utf-8') as f:
                    cadastro = json.load(f)
                print('Dados atuais:', cadastro)
                idade_indicativa = input('Nova idade idade indicativa (permaneça em branco para nao fazer alteraçoes): ').strip()
                genero = input('Novo genero (permaneça em branco para nao fazer alteraçoes): ').strip()
                if genero:
                    cadastro['genero'] = ['genero']
                if idade_indicativa:
                    cadastro['idade_indicativa'] = ['idade_indicativa']
                    with open('aula09/biblioteca.json', 'w', encoding='utf-8') as f:
                        json.dump(cadastro, f, ensure_ascii=False, indent=4)
                    limpar()
                    print('Livro atualizado com sucesso!')

                else:
                    print('Livro não encontrado!')
                continue
           case '4':
                   print(f"nome: {livro["nome"]}")
                   print(f"idade: {livro["idade_indicativa"]}")
                   print(f"genero: {livro["genero"]}")
                   
           case "5":
                   exit()
                        