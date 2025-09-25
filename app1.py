from colorama import init, Fore, Style

# Inicializa o colorama
init(autoreset=True)

contatos = []

def cabecalho(texto):
    print('\n' + Fore.CYAN + '-'*10 + f' {texto} ' + '-'*10 + Style.RESET_ALL)

def adicionar():
    cabecalho("Adicionar Contato")
    nome = input('Digite o nome: ')
    numero = input('Digite o número: ')
    contato = {"nome": nome, "numero": numero}
    contatos.append(contato)
    print(Fore.GREEN + f"\n✅ Contato {nome} adicionado com sucesso!" + Style.RESET_ALL)

def listar():
    cabecalho("Lista de Contatos")
    if not contatos:
        print(Fore.YELLOW + "Nenhum contato cadastrado." + Style.RESET_ALL)
    else:
        for i, contato in enumerate(contatos, start=1):
            print(Fore.WHITE + f"{i}. Nome: {contato['nome']}, Número: {contato['numero']}" + Style.RESET_ALL)

def buscar():
    cabecalho("Buscar Contato")
    busc = input("Digite o nome que deseja buscar: ").lower()
    encontrados = [c for c in contatos if busc in c['nome'].lower()]
    if encontrados:
        print(Fore.GREEN + "\nContatos encontrados:" + Style.RESET_ALL)
        for c in encontrados:
            print(Fore.WHITE + f"- Nome: {c['nome']}, Número: {c['numero']}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "❌ Nenhum contato encontrado!" + Style.RESET_ALL)

def excluir():
    cabecalho("Excluir Contato")
    nome_excluir = input("Digite o contato que deseja excluir: ").lower()
    for contato in contatos:
        if nome_excluir in contato['nome'].lower():
            contatos.remove(contato)
            print(Fore.GREEN + f"\n✅ Contato {contato['nome']} excluído com sucesso!" + Style.RESET_ALL)
            return
    print(Fore.RED + "❌ Contato não encontrado!" + Style.RESET_ALL)

def menu():
    while True:
        cabecalho("MENU PRINCIPAL")
        opcoes = [
            '1 - Adicionar Contato',
            '2 - Listar Contatos',
            '3 - Buscar Contatos',
            '4 - Excluir Contatos',
            '5 - Sair'
        ]
        for item in opcoes:
            print(Fore.BLUE + item + Style.RESET_ALL)
        opcao = input("\nEscolha uma opção: ")

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
                print(Fore.CYAN + "\nSaindo... Até mais! 👋" + Style.RESET_ALL)
                break
            case _:
                print(Fore.RED + "❌ Opção inválida! Tente novamente." + Style.RESET_ALL)

# Inicia a agenda
menu()