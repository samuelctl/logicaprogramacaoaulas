# concatenção
# quebra linha
#formatando decimais 
# alterando virgula e ponto 
# if else
# operador ternario 

#FIXME - concatenação com +

'''nome = "Samuel"
idade = 16
altura = 1.72

# saida de dados 
print("Olá, meu nome é, " + nome +", tenho " + str(idade) + " anos de idade " )

#FIXME - concatenação com ,
print("Olá, meu nome é, ", nome,", tenho", idade, "anos de idade")
 
#FIXME - concatenação com format
print('Olá, meu nome é, {} , tenho {} anos de idade'.format (nome,idade))

#FIXME - concatenação com f-string
print(f'Olá, meu nome é {nome} e tenho {idade+1} anos de idade')

#FIXME - eliminando quebra linha 
print('O sábio sabia ', end='')
print("que sabiá sabia assobiar.")'''


'''valor = 1.23456789

#LINK - exibindo o valor com duas casas depois da virgula
print(f'{valor:.3f}')

print(50*'=')
peso = input('Digite seu peso: ').replace(',','.')
peso = float(peso)
print(f'{peso:.2f}')'''

#LINK - Atividade 1 / Variaveis 
var_str = 'Samuel'
var_int = 16
var_float = 1.72
var_bool = True 
print()
print(f'Olá,meu nome é, {var_str} e tenho {var_int} anos de idade e {var_float} de altura isso é {var_bool}')
print(f'o valores das variaveis são', '\n Samuel', type(var_str), "\n 16: ", type(var_int), '\n 1.72:', type(var_float), '\n True:', type(var_bool))
print()
#LINK - Atividade 2 / Operações
num1 = 12
num2 = 7
soma = num1 + num2
print("O resultado da soma é:", soma)
resto1 = 15 %4
print("O resultado do resto é:", resto1)
expo = 3**2
print("O resultado do expoente é:", expo)

#LINK - Atividade 3 / Boas-vindas
nome_usuario = input("DIgite seu nome: ")
print("Seja Bem-Vindo: ", nome_usuario)

#LINK - Atividade 4 / Conversão
int3 = "20"
int3 = int(int3)
int4 = int(input('Digite um numero: '))
soma4 = int3 + int4
print("A soma dos valores é: ",soma4)
