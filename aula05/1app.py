# manipulação de arquivos 
# leitura de arquivos
with open('texto.txt', 'r', encoding = 'utf-8') as f:
    texto = f.read()
print(texto)