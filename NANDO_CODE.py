import time
import sys

matriz = []
matrizes = []  # agrupa todas as matrizes

print("Bem-vindo ao programa de operações envolvendo matrizes")
time.sleep(3)
print("\033[H\033[J", end="")

while True:

    quantMatriz = int(input("Quantas matrizes você quer gerar? "))


    def fechar_programa():
        dec = str(input("Você deseja sair do programa? S/N")).upper()
        if dec == "S":
            print("Saindo do programa...")
            time.sleep(3)
            sys.exit()


    def criar_matriz():
        print(f"\nMatriz {i + 1}:")
        lin = int(input("Coloque o número de linhas da sua matriz: "))
        col = int(input("Coloque o número de colunas da sua matriz: "))

        matriz = []

        print("Digite os números da sua matriz:")

        for l in range(lin):  # função de adicionar valores

            linha = []

            for j in range(col):
                valor = float(input(f"Digite o valor para a posição [{l + 1}][{j + 1}]: "))
                linha.append(valor)
            matriz.append(linha)
        matrizes.append(
            matriz)  # adiciona o valor a linha, da linha para a matriz, e da matriz para o grupo de matrizes


    def mostrar_matrizes(lista):
        for indice, matriz in enumerate(lista):
            lin = len(matrizes[0])
            col = len(matrizes[0][0])
            print(f"\nMatriz {indice + 1}:")  # mostra todas as matrizes
            print(f"Dimensão: {lin} x {col}")
            for linha in matriz:
                print(linha)


    def mostrar_matriz(matriz):

        for linha in matriz:
            print(linha)


    def mesma_ordem(lista):
        linhas = len(matrizes[0])
        colunas = len(matrizes[0][0])

        for matriz in matrizes:
            if len(matriz) != linhas:
                return False
            if len(matriz[0]) != colunas:
                return False
        return True


    def adicao_matriz():
        print("Matrizes disponiveis:")
        mostrar_matrizes(matrizes)
        matriz = []
        resultado = []
        escolhidas = []
        if len(matrizes) > 2:
            if mesma_ordem(matrizes) == True:
                print("Quantas você irá querer utilizar?")
                ma = int(input())

            for l in range(ma):
                quant = int(input("Digite qual você irá querer utilizar: "))
                escolhidas.append(quant - 1)

                if len(escolhidas) <= 2:
                    linhas = len(matrizes[0])
                    colunas = len(matrizes[0][0])

                    for linha in matrizes[0]:
                        resultado.append(linha.copy())

                    for linha in matrizes[1]:
                        matriz.append(linha.copy())

                    for i in range(linhas):

                        for j in range(colunas):
                            resultado[i][j] += matriz[i][j]
                else:
                    linhas = len(matrizes[0])
                    colunas = len(matrizes[0][0])

                    for linha in matrizes[escolhidas[0]]:
                        resultado.append(linha.copy())

                    for indice in escolhidas[1:]:
                        matriz = matrizes[indice]
                        for i in range(linhas):
                            for j in range(colunas):
                                resultado[i][j] += matriz[i][j]
            else:
                print("É impossivel fazer soma com matrizes de ordens diferentes! ")
                print("Crie outras matrizes de ordem igual para poder realizar este cálculo: ")
                criar_matriz()
                return adicao_matriz()

        elif len(matrizes) == 2:
            if mesma_ordem(matrizes):
                linhas = len(matrizes[0])
                colunas = len(matrizes[0][0])

                for linha in matrizes[0]:
                    resultado.append(linha.copy())

                for linha in matrizes[1]:
                    matriz.append(linha.copy())

                for i in range(linhas):

                    for j in range(colunas):
                        resultado[i][j] += matriz[i][j]

            return resultado

        else:
            print("Crie outra matriz para realizar a soma ")
            quantMatriz = int(input("\nQuantas matrizes você irá querer criar? "))
            for i in range(quantMatriz):
                criar_matriz()
                return adicao_matriz()


    def subt_matriz():
        print("Matrizes disponiveis:")
        mostrar_matrizes(matrizes)
        matriz = []
        resultado = []
        escolhidas = []
        if len(matrizes) > 2:
            if mesma_ordem(matrizes):
                print("Quantas você irá querer utilizar?")
                ma = int(input())

            for l in range(ma):
                quant = int(input("Digite qual você irá querer utilizar: "))
                escolhidas.append(quant - 1)

            linhas = len(matrizes[0])
            colunas = len(matrizes[0][0])

            for linha in matrizes[escolhidas[0]]:
                resultado.append(linha.copy())

            for indice in escolhidas[1:]:
                matriz = matrizes[indice]

                for i in range(linhas):

                    for j in range(colunas):
                        resultado[i][j] -= matriz[i][j]
            return resultado

        elif len(matrizes) == 2:
            if mesma_ordem(matrizes):
                linhas = len(matrizes[0])
                colunas = len(matrizes[0][0])

                for linha in matrizes[0]:
                    resultado.append(linha.copy())

                for linha in matrizes[1]:
                    matriz.append(linha.copy())

                for i in range(linhas):

                    for j in range(colunas):
                        resultado[i][j] -= matriz[i][j]

            return resultado

        else:
            print("Crie outra matriz para realizar a subtração ")
            quantMatriz = int(input("\nQuantas matrizes você irá querer criar? "))
            for i in range(quantMatriz):
                criar_matriz()
                return adicao_matriz()


    def mult_int():
        print("Matrizes disponiveis: ")
        mostrar_matrizes(matrizes)

        escolhida = []
        resultado = []
        ma = int(input("Escolha a matriz: "))
        escolhida.append(ma - 1)
        linhas = len(matrizes[0])
        colunas = len(matrizes[0][0])

        for linha in matrizes[escolhida[0]]:
            resultado.append(linha.copy())

        numero = int(input("Digite o número inteiro: "))

        for i in range(linhas):
            for j in range(colunas):
                resultado[i][j] *= numero

        return resultado


    def mult_matriz():

        print("Primeira matriz:")
        a = int(input()) - 1

        print("Segunda matriz:")
        b = int(input()) - 1

        matriz1 = matrizes[a]
        matriz2 = matrizes[b]

        if len(matriz1[0]) != len(matriz2):
            print("Não é possível multiplicar.")

            return

        resultado = []

        for i in range(len(matriz1)):

            linha = []

            for j in range(len(matriz2[0])):

                soma = 0

                for k in range(len(matriz2)):
                    soma += matriz1[i][k] * matriz2[k][j]

                    linha.append(soma)

                    resultado.append(linha)

        return resultado


    for i in range(quantMatriz):
        criar_matriz()


    def matriz_transposta():

        print("Matrizes disponiveis:")
        mostrar_matrizes(matrizes)

        escolha = int(input("Escolha a matriz: ")) - 1

        matriz = matrizes[escolha]

        linhas = len(matriz)
        colunas = len(matriz[0])

        resultado = []

        print("\npasso a passo da transposição:")

        for j in range(colunas):

            nova_linha = []

            for i in range(linhas):
                print(f"posição [{i}][{j}] -> [{j}][{i}] = {matriz[i][j]}")
                nova_linha.append(matriz[i][j])

            resultado.append(nova_linha)

        print("\nmatriz transposta gerada:")

        mostrar_matriz(resultado)

        dec = input("\ndeseja adicionar a transposta à lista de matrizes? S/N ").upper()

        if dec == "S":
            matrizes.append(resultado)
            print("transposta adicionada como nova matriz.")

        return resultado


    def determinante():

        print("Matrizes disponiveis:")
        mostrar_matrizes(matrizes)

        escolha = int(input("Escolha a matriz: ")) - 1

        matriz = matrizes[escolha]

        linhas = len(matriz)
        colunas = len(matriz[0])

        if linhas != colunas:
            print("determinante só existe para matrizes quadradas.")
            return

        if linhas == 1:

            print(f"det = {matriz[0][0]}")
            return matriz[0][0]

        if linhas == 2:

            a = matriz[0][0]
            b = matriz[0][1]
            c = matriz[1][0]
            d = matriz[1][1]

            print("\npasso a passo:")
            print(f"det = ({a} * {d}) - ({b} * {c})")

            det = (a * d) - (b * c)

            print(f"det = {det}")

            return det

        if linhas == 3:

            a = matriz[0][0]
            b = matriz[0][1]
            c = matriz[0][2]

            d = matriz[1][0]
            e = matriz[1][1]
            f = matriz[1][2]

            g = matriz[2][0]
            h = matriz[2][1]
            i = matriz[2][2]

            print("\nregra de sarrus:")

            soma1 = (a * e * i)
            soma2 = (b * f * g)
            soma3 = (c * d * h)

            sub1 = (c * e * g)
            sub2 = (a * f * h)
            sub3 = (b * d * i)

            print(f"({a}*{e}*{i}) + ({b}*{f}*{g}) + ({c}*{d}*{h})")
            print(f"- ({c}*{e}*{g}) - ({a}*{f}*{h}) - ({b}*{d}*{i})")

            det = (soma1 + soma2 + soma3) - (sub1 + sub2 + sub3)

            print(f"det = {det}")

            return det

        print("o programa calcula determinantes até ordem 3x3.")


    def matriz_inversa():

        print("Matrizes disponiveis:")
        mostrar_matrizes(matrizes)

        escolha = int(input("Escolha a matriz: ")) - 1

        matriz = matrizes[escolha]

        linhas = len(matriz)
        colunas = len(matriz[0])

        if linhas != colunas:
            print("matriz inversa só existe para matrizes quadradas.")
            return None

        if linhas != 2:
            print("esta versão calcula inversa apenas para matrizes 2x2.")
            return None

        a = matriz[0][0]
        b = matriz[0][1]
        c = matriz[1][0]
        d = matriz[1][1]

        det = (a * d) - (b * c)

        print("\npasso a passo:")
        print(f"det = ({a} * {d}) - ({b} * {c})")
        print(f"det = {det}")

        if det == 0:
            print("a matriz não possui inversa.")
            return None

        resultado = []

        linha1 = [d / det, -b / det]
        linha2 = [-c / det, a / det]

        resultado.append(linha1)
        resultado.append(linha2)

        print("\nmatriz inversa:")
        mostrar_matriz(resultado)

        dec = input("\ndeseja adicionar a inversa à lista de matrizes? S/N ").upper()

        if dec == "S":
            matrizes.append(resultado)

        return resultado


    def calculo():
        print("\n === Calculadora ==="
            "\n1 - Soma"
            "\n2 - Subtração"
            "\n3 - Multiplicação por numero inteiro"
            "\n4 - Multiplicação por outra matriz"
            "\n5 - Matriz transposta"
            "\n6 - Determinante"
            "\n7 - Matriz inversa"
            "\n0 - Sair do programa")
        calc = int(input("\nEscolha uma opção: "))

        if (calc == 1):
            resultado = adicao_matriz()
            print("\nResultado da adição: ")
            mostrar_matriz(resultado)

            print("\n === Calculadora ==="
                  "\n1 - Deseja fechar o programa"
                  "\n2 - Escolher operação"
                  "\n3 - Fazer/trocar matrizes")
            exc = int(input())
            if exc == 1:
                fechar_programa()
            if exc == 2:
                return calculo()
            if exc == 3:
                criar_matriz()

        if (calc == 2):
            resultado = subt_matriz()
            print("\nResultado da subração: ")
            mostrar_matriz(resultado)

            print("\n === Calculadora ==="
                  "\n1 - Deseja fechar o programa"
                  "\n2 - Escolher operação"
                  "\n3 - Fazer/trocar matrizes")
            exc = int(input())
            if exc == 1:
                fechar_programa()
            if exc == 2:
                return calculo()
            if exc == 3:
                criar_matriz()

        if (calc == 3):
            resultado = mult_int()
            print("\nResultado da multiplicação : ")
            mostrar_matriz(resultado)

            print("\n === Calculadora ==="
                  "\n1 - Deseja fechar o programa"
                  "\n2 - Escolher operação"
                  "\n3 - Fazer/trocar matrizes")
            exc = int(input())
            if exc == 1:
                fechar_programa()
            if exc == 2:
                return calculo()
            if exc == 3:
                criar_matriz()

        if calc == 5:

            resultado = matriz_transposta()

            print("\nresultado:")
            mostrar_matriz(resultado)

            return calculo()

        if calc == 6:

            resultado = determinante()

            print(f"\ndeterminante = {resultado}")

            return calculo()

        if calc == 7:

            resultado = matriz_inversa()

            if resultado != None:

                print("\nresultado:")
                mostrar_matriz(resultado)

            return calculo()


    print("\nMatrizes Geradas: ")
    mostrar_matrizes(matrizes)
    calculo()
