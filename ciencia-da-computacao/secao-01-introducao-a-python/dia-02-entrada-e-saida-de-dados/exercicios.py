import random

# ======================================================
# FUNCAO NOME VERTICAL

def nome_vertical(nome):
    lista_letras = list(nome)
    print(nome)
    for letra in nome:
        lista_letras.pop(-1)
        print(''.join(lista_letras))

# nome_vertical('gabriel')

# ======================================================
# FUNCAO DESCOBRIR PALAVRA

def ler_palavras(file):
    return [palavra.strip() for palavra in file]

def descobrir_nome():
    tentativas = 0
    file = open('lista_de_palavras.txt')
    lista_de_palavras = ler_palavras(file)
    palavra_selecionada = random.choice(lista_de_palavras)
    palavra_embaralhada = "".join(random.sample(palavra_selecionada, len(palavra_selecionada)))
    while tentativas < 3:
        print(f'\nVocê tem {3 - tentativas} tentativas')
        print(palavra_embaralhada)
        palpite = input('Digite o nome correto da palavra:')
        if palpite == palavra_selecionada:
            print('VOCE ACERTOU')
            break
        else:
            tentativas += 1
    if tentativas == 3:
        print(f'\nSuas tentativas acabaram :( \n\nA palavra correta era {palavra_selecionada}\n')

    file.close()
    

# descobrir_nome()




