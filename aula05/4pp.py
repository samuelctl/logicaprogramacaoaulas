import os

while True:
    try: 
        novo_texto = input('Digite o texto: \n')
        novo_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip().lower()

        with open(f'{novo_arquivo}.txt', 'w', encoding='utf-8') as f:
            f.write(novo_texto)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{novo_arquivo}.txt gravado com sucesso. ')

        novo_texto2 = input('Digite um novo texto: \n')

        with open(f'{novo_arquivo}.txt', 'a', encoding='utf-8')as f:
            f.write(f'\n{novo_texto2}')
        print('Gravado com sucesso. ')

        # ler os dados atualizados
        with open(f'{novo_arquivo}.txt', 'r', encoding='utf-8') as f:
           texto_final = f.read()
        print(f'Texto final: {texto_final}')
        
        while True:
            prosseguir = input('Deseja abrir outro arquivo? (s/n)')
            if prosseguir == 's' or prosseguir == 'n':
                break
            else:
                print('Opção invalida! ')
                continue 
        match prosseguir:
            case 's':
                continue
            case 'n':
                break
    except Exception as e:
        print(novo_arquivo)
        