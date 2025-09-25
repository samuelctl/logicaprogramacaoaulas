import json
with open("testejson/app.json", "r", encoding="utf-8") as f:
    dados = dict(json.load(f))

def salvar():
    global dados
    with open("testejson/app.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


def adicionar():
    global dados
    livro = {
    "nome" : input("Digite o nome do livro que deseja adicionar: ").strip().title(),
    "autor" : input("Digite o autor do livro : ").strip().title(),
    "genero": input("Digite o gênero do livro: ").strip().title()
    }
    dados["livros"].append(livro)
    with open("testejson/app.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    salvar()
    print("Livro salvo com sucesso na biblioteca!!")
    print("-"*20, "BIBLIOTECA", 20* "-")


def remover():
    global dados
    for livro in dados["livros"]:
        print(f"- {livro['nome']} ({livro['autor']} / {livro['genero']})")
    sair = input("Digite o nome do livro que deseja remover: ").strip().title()
    encontrado = False
    for livro in dados["livros"]:
        if livro["nome"] == sair:
            dados["livros"].remove(livro)
            encontrado = True
            print("Removido com sucesso!!!")
            break
    if not encontrado:
        print("Livro não encontrado!!")
    salvar()


def atualizar():
    global dados
    with open("testejson/app.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    for livro in dados["livros"]:
        print(f"- {livro['nome']} ({livro['autor']} / {livro['genero']})")
    novo = input("Digite o livro que deseja atualizar: ").strip().title()
    encontrado = False
    for livro in dados["livros"]:
        if livro["nome"] == novo:
            print("Atualizando...")
            novo_nome = input(f"Novo nome(atual: {livro['nome']}): ").strip().title()
            novo_autor = input(f"Novo autor(atual: {livro['autor']}): ").strip().title()
            novo_genero = input(f"Novo genero(atual: {livro['genero']}): ").strip().title()
            if novo_nome:
                livro["nome"] = novo_nome
            if novo_autor:
                livro["autor"] = novo_autor
            if novo_genero:
                livro["genero"] = novo_genero
            encontrado = True
            print(f"Livro '{novo}' atualizado com sucesso")
            break
    if not encontrado:
        print("Livro não encontrado!!")
    salvar()


def listar():
    global dados
    for livro in dados["livros"]:
        print(f"- {livro['nome']} ({livro['autor']} / {livro['genero']})")
    


def menu():
    print(" 1 - Adicionar Livro")
    print("2 - Listar")
    print("3 - Remover Livro")
    print("4 - Atualizar livro")
    print("5 - Sair")
    opcao = input("Digite a opção desejada: ")
    match opcao:
        case "1":
            adicionar()
        case "2":
            listar()
        case "3":
            remover()
        case "4":
            atualizar()
        case "5":
            exit()
while True:
    menu()

    

