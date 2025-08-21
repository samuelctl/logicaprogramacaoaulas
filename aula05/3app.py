import os

while True:
    try: 
        novo_texto = input('Digite o texto: \n')
        novo_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip().lower()

        with open(f'Aula05/{novo_arquivo}.txt', 'w', encoding='utf-8') as f:
            f.write(novo_texto)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{novo_arquivo}.txt gravado com sucesso. ')

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
        print(f'')