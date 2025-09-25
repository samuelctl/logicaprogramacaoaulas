import random

# Criar tabuleiro 5x5
tabuleiro = [["~" for _ in range(5)] for _ in range(5)]

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tab):
    print("  0 1 2 3 4")
    for i, linha in enumerate(tab):
        print(f"{i} {' '.join(linha)}")

# Posicionar 3 navios aleatoriamente
navios = []
while len(navios) < 3:
    pos = (random.randint(0, 4), random.randint(0, 4))
    if pos not in navios:
        navios.append(pos)

# Contador de tentativas
tentativas = 0

# Função para verificar se o jogador acertou
def verificar_tiro(linha, coluna):
    global tentativas
    tentativas += 1
    if (linha, coluna) in navios:
        tabuleiro[linha][coluna] = "O"
        print("Acertou!")
        navios.remove((linha, coluna))
    else:
        tabuleiro[linha][coluna] = "X"
        print("Água!")

# Loop principal do jogo
while len(navios) > 0:
    imprimir_tabuleiro(tabuleiro)
    try:
        l = int(input("Escolha a linha (0-4): "))
        c = int(input("Escolha a coluna (0-4): "))
        if 0 <= l <= 4 and 0 <= c <= 4:
            verificar_tiro(l, c)
        else:
            print("Digite valores entre 0 e 4!")
    except ValueError:
        print("Digite números válidos!")

print(f"Parabéns! Você afundou todos os navios em {tentativas} tentativas!")