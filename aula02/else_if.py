# estrutura de decisao
'''nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
idade = int(idade)
if idade >= 18:
    print(f'{nome} é maior de idade.')
    print('Você está dentro do bloco IF')
else:
    print(f'{nome} é menor de idade.')
    print('Você está dentro do bloco ELSE')
print('Você está fora da estrutura condicional if e else')'''
#FIXME - Aula de if, else e input 

'''num1 = 10 

if num1 %2 ==0: 
    print('Numero par')
else:
    print('Numero impar')

print(40*'=','BOLETIM ESCOLAR', 40*'=') #upper caixa alta; lower caixa baixa
nome_aluno = input('Digite o nome do aluno: ').upper()
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4

# >=7: aprovado
# >=5: recuperação
# reprovado 

if media >=7:
   print(f'{nome_aluno}!!!Aluno Aprovado!')
   print(f'Nota 1: {nota1} | Nota 2: {nota2}')
   print(f'Nota 3: {nota3} | Nota 4: {nota4}' )
   print(20*'=')
   print(f'Média: {media}')

elif media >=5:
   print(f'{nome_aluno}!!!Aluno de Recuperação!')
   print(f'Nota 1: {nota1} | Nota 2: {nota2}')
   print(f'Nota 3: {nota3} | Nota 4: {nota4}' )
   print(20*'=')
   print(f'Média: {media}')

else:
   print(f'{nome_aluno}!!!Aluno Reprovado!')
   print(f'Nota 1: {nota1} | Nota 2: {nota2}')
   print(f'Nota 3: {nota3} | Nota 4: {nota4}' )
   print(20*'=')
   print(f'Média: {media}')'''

'''# variaveis 
nome = 'João'
idade1 = 11
altura = 1.25

# verifica se o usuario possui os requisitos mínimos
if idade1 >= 12 and altura >= 1.2:
   print(f'A entrada de {nome} está autorizada.')
else:
   print(f'A entrad de {nome} não está autorizada.')'''

# operador ternário
nome = 'alex'
idade = 39
print(nome, 'é maior de idade.' if idade >= 18 else 'é menos de idade.')




   


