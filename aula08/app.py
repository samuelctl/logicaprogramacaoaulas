import random
import string

def gerar_senha(comprimento = 12, incluir_maiusculo = True, incluir_minusculo = True,
                incluir_numero = True, inculir_carac = True):
    caracter = ''
    if incluir_maiusculo:
        caracter += string.ascii_uppercase
    
    if incluir_minusculo:
        caracter += string.ascii_lowercase
    
    if incluir_numero:
        caracter += string.digits
    if inculir_carac:
        caracter += string.punctuation
    
    if not caracter:
        return ValueError('Deve ter pelo menos um tipo de caractere')
    
    senha = ''.join(random.choice(caracter) for _ in range(comprimento))
    print(f"Senha: {senha}")
    return senha


def main():
    print("Gerador de senhas fortes")
    comprimento = int(input('Digite o comprimento da senha (padrão é 12): ') or 12)
    incluir_maiusculo = input('Incluir maiúscula: (s/n, padrão = sim): ').lower() != "n"
    incluir_minuscula = input('Incluir minúscula: (s/n, padrão = sim): ').lower() != "n"
    incluir_numero = input('Incluir número: (s/n, padrão = sim): ').lower() != "n"
    incluir_caracter_es = input('Incluir carcter especial: (s/n, padrão = sim): ').lower() != "n"

    senha = gerar_senha(comprimento, incluir_maiusculo, incluir_minuscula, incluir_numero, incluir_caracter_es)

    print(f'A senha  gerada foi: {senha}')

    with open ('aula08/senhas.txt', 'a', encoding='utf-8') as s:
        s.write(f'\n{senha}')

if __name__ == '__main__':
    main()
