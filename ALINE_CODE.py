import time

MENU = 0
matrizes = []

print("Bem-vindo ao programa de operações envolvendo matrizes")
time.sleep(3)

print("\033[H\033[J", end="")

quantMatriz = int(input("Quantas matrizes você quer gerar? "))

for i in range(quantMatriz):

    print(f"\nMatriz {i + 1}:")

    lin_m = int(input("Coloque o número de linhas da sua matriz: "))
    col_n = int(input("Coloque o número de colunas da sua matriz: "))

    matriz = []

    print("Digite os números da sua matriz:")

    for linha_atual in range(lin_m):

        linha = []

        for j in range(col_n):

            valor = int(input(f"Digite o valor para a posição [{linha_atual+1}][{j+1}]: "))
            linha.append(valor)

        matriz.append(linha)

    matrizes.append(matriz)

print("\nMatrizes Geradas:")

for indice, matriz in enumerate(matrizes):

    print(f"\nMatriz {indice + 1}:")

    for linha in matriz:
        print(linha)

calc = int(input(
"\n=== Calculadora ==="
"\n1 - Soma"
"\n2 - Subtração"
"\n3 - Multiplicação por outra matriz"
"\n4 - Multiplicação por número inteiro"
"\n0 - Sair do programa\n"
))

if(calc == 1):

    m1 = int(input("Escolha a primeira matriz: ")) - 1
    m2 = int(input("Escolha a segunda matriz: ")) - 1

    if len(matrizes[m1]) == len(matrizes[m2]) and len(matrizes[m1][0]) == len(matrizes[m2][0]):

        resultado = []

        for i in range(len(matrizes[m1])):

            linha = []

            for j in range(len(matrizes[m1][0])):
                linha.append(matrizes[m1][i][j] + matrizes[m2][i][j])

            resultado.append(linha)

        print("\nResultado da soma:")

        for linha in resultado:
            print(linha)

    else:
        print("As matrizes devem ter a mesma ordem.")

elif(calc == 2):

    m1 = int(input("Escolha a primeira matriz: ")) - 1
    m2 = int(input("Escolha a segunda matriz: ")) - 1

    if len(matrizes[m1]) == len(matrizes[m2]) and len(matrizes[m1][0]) == len(matrizes[m2][0]):

        resultado = []

        for i in range(len(matrizes[m1])):

            linha = []

            for j in range(len(matrizes[m1][0])):
                linha.append(matrizes[m1][i][j] - matrizes[m2][i][j])

            resultado.append(linha)

        print("\nResultado da subtração:")

        for linha in resultado:
            print(linha)

    else:
        print("As matrizes devem ter a mesma ordem.")

elif(calc == 3):

    m1 = int(input("Escolha a primeira matriz: ")) - 1
    m2 = int(input("Escolha a segunda matriz: ")) - 1

    if len(matrizes[m1][0]) == len(matrizes[m2]):

        resultado = []

        for i in range(len(matrizes[m1])):

            linha = []

            for j in range(len(matrizes[m2][0])):

                soma = 0

                for k in range(len(matrizes[m2])):
                    soma += matrizes[m1][i][k] * matrizes[m2][k][j]

                linha.append(soma)

            resultado.append(linha)

        print("\nResultado da multiplicação:")

        for linha in resultado:
            print(linha)

    else:
        print("Número de colunas da primeira matriz deve ser igual ao número de linhas da segunda.")

elif(calc == 4):

    m = int(input("Escolha a matriz: ")) - 1
    numero = int(input("Digite o número inteiro: "))

    resultado = []

    for i in range(len(matrizes[m])):

        linha = []

        for j in range(len(matrizes[m][0])):
            linha.append(matrizes[m][i][j] * numero)

        resultado.append(linha)

    print("\nResultado da multiplicação por inteiro:")

    for linha in resultado:
        print(linha)

elif(calc == 0):

    print("Programa encerrado.")

else:

    print("Opção inválida.") 
