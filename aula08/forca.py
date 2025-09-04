import random
import os
def animal():
    animal = ["leão", "tigre", "elefante", "girafa", "zebra", "cavalo", "macaco", "urso", "lobo", "raposa",
"cachorro", "gato", "coelho", "panda", "cervo", "hipopótamo", "rinoceronte", "antílope", "búfalo", "camelo",
"canguru", "tamanduá", "pinguim", "águia", "falcão", "coruja", "papagaio", "arara", "jacaré", "crocodilo",
"cobra", "tartaruga", "tatu", "porco-espinho", "ouriço", "golfinho", "baleia", "tubarão", "foca", "leão-marinho",
"texugo", "doninha", "guaxinim", "suricato", "lhama", "alpaca", "galo", "galinha", "pato", "cisne"]
    return random.choice(animal)

def comida():
    comida = ["pizza", "hambúrguer", "sushi", "lasanha", "macarrão", "feijoada", "churrasco", "taco", "burrito", "curry",
"arroz", "feijão", "salada", "frango assado", "bife", "nhoque", "esfiha", "kibe", "pastel", "coxinha",
"empada", "pão de queijo", "torta de frango", "risoto", "moqueca", "acarajé", "bacalhau", "panqueca", "omelete", "quibe cru",
"estrogonofe", "sopa", "caldo verde", "canja", "lasanha de berinjela", "yakisoba", "temaki", "ramen", "gnocchi", "carbonara",
"picanha", "costela", "linguiça", "farofa", "polenta", "cuscuz", "tabule", "salpicão", "bolonhesa", "fricassê"]
    return random.choice(comida)

def cep():
    print('Cidade, Estado e Países!')
    cep = ["Brasil", "Estados Unidos", "Canadá", "Japão", "França", "Alemanha", "Itália", "China", "Índia", "Austrália",
"São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Fortaleza", "Salvador", "Recife", "Porto Alegre", "Manaus", "Brasília",
"Califórnia", "Texas", "Nova York", "Flórida", "Illinois", "Alasca", "Nevada", "Arizona", "Geórgia", "Ohio",
"Paris", "Londres", "Berlim", "Roma", "Tóquio", "Pequim", "Seul", "Moscou", "Cidade do México", "Buenos Aires",
"Argentina", "Chile", "Colômbia", "Peru", "Egito", "África do Sul", "Rússia", "Noruega", "Suécia", "Espanha"]
    return random.choice(cep)

def menu():
    p = [['1 - Animal'],
        ['2 - Comida'], 
            ['3 - Cep'], 
            ['4 - Sair']]
    for i in p:
        print(i)
    opcao = input('Digite a opção desejada: ')
    match opcao:
        case '1':
          return  animal()
        case '2':
           return comida()
        case'3':
            return cep()
        case '4':
            exit()
    
def jogar_forca():
    palavra = menu()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    while True:
        palavra_escondida = ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_escondida += letra
            else:
                palavra_escondida += '_'
        print('Palavra:', palavra_escondida)
        print('Letras erradas:', letras_erradas)
        print('Tentativas restantes:', tentativas)

        if palavra_escondida == palavra:
            print('Parabéns! Você ganhou!!!')
            while True:
                input_user = input("Deseja jogar denovo?(s/n): ").strip().upper()
                if input_user == 'S':
                    jogar_forca()
                elif input_user == 'N':
                    print('Saindo')
                    exit()
                else:
                    print('Opção inválida!')


        elif tentativas == 0:
            print('Você perdeu! A palavra era:', palavra)
            while True:
                input_user = input("Deseja jogar denovo?(s/n): ").strip().upper()
                if input_user == 'S':
                    jogar_forca()
                elif input_user == 'N':
                    print('Saindo')
                    exit()
                else:
                    print('Opção inválida!')
            
        letra_usuario = input('Digite uma letra: ').lower()

        if letra_usuario in palavra:
            print('Letra correta!')
            letras_corretas.append(letra_usuario)
        else:
            print('Letra errada!')
            letras_erradas.append(letra_usuario)
            tentativas -= 1
        

if __name__ == '__main__':
    os.system('cls')
    print('-'*20, 'Bem vindo ao jogo da forca', 20*'-')
    print('Escolha uma opção de jogo\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
    jogar_forca()
