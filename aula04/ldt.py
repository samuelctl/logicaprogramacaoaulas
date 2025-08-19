 #LINK - Coleção - lista, dicionário e tupla
#SECTION - lista
'''nomes_lista = ['Fulano','Cicrano','Beltrano','Maria','Joao']
#busca o nome desejado
nome = input('Informe o nome que deseja encontrar: ')
if nome in nomes_lista:
    print(nome)
else:
    print(f'{nome} não encontrado. ')
#ordenar a lista
nomes_lista.sort()

#percorrendo a lista com contador
for i in range(len(nomes_lista)):
    print(f'{i+1}º nome da lista: {nomes_lista[i]}')

#ANCHOR - procura pelo índice através do valor
indice = nomes_lista.index(nome)

# retorna resultado 
try:
    print(f'{nome} encontrado no índice {indice}. ')
except:
    print(f'{nome} nao encontrado. ')


#ANCHOR - count

quantidade = nomes_lista.count(nome)

try:
    print(f'{nome} foi encontrado na lista {quantidade} vezes. ')
except:
    print(f'{nome} nao encontrado. ')

#LINK - alterano dados de uma lista
print(nomes_lista)

nomes_lista[0] = 'Alex'

for nome in nomes_lista:
    print(nome)'''
'''#REVIEW - Mudar o nome da lista
nomes_lista = ['fulano','cicrano','beltrano','joana']
nome_alterar = input('Informe o nome que deseja alterar: ')
nomes_lista[nomes_lista.index(nome_alterar)] = input('Informe o novo nome: ')

for nome in nomes_lista: 
    print(nome)'''

numero = int(input('Digite o número: '))
for i in range(1,11):
    resultado = numero * i
    print(f'{i} X {numero} = {resultado}')