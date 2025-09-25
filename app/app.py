contatos = []

def adicionar():
    nome = input('Digite o nome: ')
    numero = input('Digite o numero: ')

    contato = {
        "nome" : nome,
        "numero": numero
    }
    contatos.append(contato)
    print(f'Contato {nome} adicionado com sucesso!')

def listar():
    if not contatos:
        print('Não há contatos salvos!')
    else: 
        print('-'*20, "Lista de contatos", 20*'-')
        for i, contato in enumerate(contatos, start=1):
            print(f'{i}. Nome: {contato['nome']}, Numero: {contato['numero']}')

def buscar():
    busc = input('Digite o nome que deseja buscar: ').lower()
    encontrados = []
    for contato in contatos:
        if busc in contato['nome'].lower():
            encontrados.append(contato)
    if encontrados:
        print('-'*20, 'Contatos encontrados', 20*'-')
        for c in encontrados:
            print(f'Nome: {c['nome']}, Número: {c['numero']}')
    else:
        print('Contato não encontrado!!')
def excluir():
    excluir = input('Digite o contato que deseja excluir: ').lower()
    excluidos = []
    for contato in contatos:
        if excluir in contato['nome'].lower():
            contatos.remove(contato)
            print(f"Contato {contato['nome']} Excluido!")
            return
    print('Contato não encotrado!')
    
def menu():
    while True:
        lista = [
            '1 - Adicionar Contato',
            '2 - Listar Contatos',
            '3 - Buscar Contatos',
            '4 - Excluir contatos',
            '5 - Sair'
            ]
        for item in  lista:
            print(item)    
        opcao = input('Digite a opção desejada: ')  
        match opcao:
            case '1':
                adicionar()
            case '2':
                listar()
            case '3':
                buscar()
            case '4':
                excluir()
            case '5':
                exit()
def contas():
    menu()
contas()


    
