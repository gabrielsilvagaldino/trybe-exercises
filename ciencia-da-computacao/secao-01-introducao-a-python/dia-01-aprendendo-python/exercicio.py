# ======================================================
# FUNÇÃO DE MAIOR E MENOR

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

def maior_menor(num1, num2):
    if num1 > num2:
        print(f'O numero {num1} é maior que {num2}')
    else:
        print(f'O numero {num2} é maior que {num1}')

# maior_menor(num1, num2)

# ======================================================
# FUNÇÃO DE MÉDIA ARITMÉTICA

lista = [1,2,3,4,5,6,7,8]

def media(array):
    result = 0
    for n in lista:
        result += n
    print(result / len(array))

# media(lista)

# ======================================================
# FUNÇÃO DE QUADRADO

def quadrado(num):
    if num > 1:
        line = num * '*'
        for n in range(num):
            print(line)
    else:
        print('O número precisa ser maior que 1.')

# quadrado(6)

# ======================================================
# FUNÇÃO DE MAIOR NOME

lista_de_nomes = ["Gabriel", "Apapocuva Momento Mori da Silva", "Heimerdinger"]

def maior_nome(lista):
    num = 0
    maior = ''
    for nome in lista:
        if len(nome) > num:
            num = len(nome)
            maior = nome
    print(maior)

# maior_nome(lista_de_nomes)

# ======================================================
# FUNÇÃO DE LATA DE TINTA

tamanho_parede = int(input("Digite o tamanho da sua parede em m²: "))

def calculo_da_tinta(metros):
    preco_tinta = 80
    tinta_necessaria = metros / 3
    latas = tinta_necessaria // 18
    if tinta_necessaria % 18:
        latas += 1
    print(latas, tinta_necessaria * preco_tinta)

calculo_da_tinta(tamanho_parede)