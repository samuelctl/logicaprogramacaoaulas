pares = int(input('Digite um número limite: '))

def contar():
    cont = 0 
    for numero in range(pares +1):
        if numero %2 == 0:
            cont += numero
    print('-'*20, " Resultado ", 20*'-')
    print(f'A soma dos numeros pares dentro de {pares} é {cont}!!')
contar()

