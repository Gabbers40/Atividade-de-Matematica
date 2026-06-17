# Trabalho de matematica do tarcisio
# grupo - Aline ramos, Angelo gerola, fernando viegas, gabriel moreira e gabriel nicolas
# 2° DS
import time
import sys

matriz = []
matrizes = []  # agrupa todas as matrizes

print("Bem-vindo ao programa de operações envolvendo matrizes")
time.sleep(3)
print("\033[H\033[J", end="")

while True:
    quantMatriz = int(input("Quantas matrizes você quer gerar? :"))

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
            print(linha)  # imprime as linhas da matriz

    def mesma_ordem(lista):  # função para ver se a matriz é de mesma ordem
        linhas = len(matrizes[0])
        colunas = len(matrizes[0][0])

        for matriz in matrizes:
            if len(matriz) != linhas:
                return False
            if len(matriz[0]) != colunas:
                return False
        return True

    def escolher_matriz(lista):
        print("Matrizes disponiveis:")
        mostrar_matrizes(lista)
        escolhidas = []

        while True:
            valor = int(input("Digite a matriz desejada: "))
            if 1 <= valor <= len(lista):
                escolhidas.append(valor - 1)
                break
            else:
                print("Matriz inexistente!")
        
        return escolhidas

    def escolher_matrizes(lista):
        print("Matrizes disponiveis: ")
        mostrar_matrizes(lista)
        escolhidas = []

        quant = int(input("Quantas você quer utilizar? "))
        for i in range(quant):
            while True:
                valor = int(input(f"Digite a {i + 1}ª Matriz: "))
                if 1 <= valor <= len(lista):
                    escolhidas.append(valor - 1)
                    break
                else:
                    print("Matriz inexistente!")

        return escolhidas

    def adicao_matriz():
        escolhidas = []
        matriz = []
        resultado = []

        if len(matrizes) > 2:  # verifica se tem mais de 2 matrizes no array
            if mesma_ordem(matrizes):
                escolhidas = escolher_matrizes(matrizes)
                linhas = len(matrizes[0])
                colunas = len(matrizes[0][0])

                for linha in matrizes[escolhidas[0]]:
                    resultado.append(linha.copy())

                for indice in escolhidas[1:]:
                    matriz = matrizes[indice]
                    for i in range(linhas):
                        for j in range(colunas):
                            resultado[i][j] += matriz[i][j]
        
                ver_passo = input("\nDeseja ver o passo a passo da adição? (S/N): ").upper()  # passo a passo da adição
                if ver_passo == "S":
                    matrizes_para_explicar = [matrizes[idx] for idx in escolhidas]
                    explicar_soma_multipla(matrizes_para_explicar)
                
                return resultado
            else:
                print("As matrizes não possuem a mesma ordem para serem somadas.")
                return None

        elif len(matrizes) == 2:
            if mesma_ordem(matrizes):
                linhas = len(matrizes[0])
                colunas = len(matrizes[0][0])

                for linha in matrizes[0]:
                    resultado.append(linha.copy())

                for i in range(linhas):
                    for j in range(colunas):
                        resultado[i][j] += matrizes[1][i][j]

                ver_passo = input("\nDeseja ver o passo a passo da soma? (S/N): ").upper()  # passo a passo da adição
                if ver_passo == "S":
                    explicar_soma(matrizes[0], matrizes[1])

                return resultado
            else:
                print("As matrizes não possuem a mesma ordem para serem somadas.")
                return None

        else:
            print("Crie outra matriz para realizar a soma ")
            quantMatriz = int(input("\nQuantas matrizes você irá querer criar? "))
            for i in range(quantMatriz):
                criar_matriz()
            return adicao_matriz()

    def explicar_soma(m1, m2):  # Função de passo a passo da adição
        print("\n--- PASSO A PASSO DA SOMA ---")
        print("Para somar matrizes, somamos os elementos que estão na mesma posição:")
        linhas = len(m1)
        colunas = len(m1[0])

        for i in range(linhas):
            for j in range(colunas):
                v1 = m1[i][j]
                v2 = m2[i][j]
                print(f"Posição [{i + 1}][{j + 1}]: {v1} + {v2} = {v1 + v2}")

    def explicar_soma_multipla(lista_matrizes):  # Função de passo a passo da adição múltipla
        print("\n--- PASSO A PASSO DA SOMA (MÚLTIPLAS MATRIZES) ---")
        print("Somamos os elementos correspondentes de todas as matrizes escolhidas:")
        linhas = len(lista_matrizes[0])
        colunas = len(lista_matrizes[0][0])

        for i in range(linhas):
            for j in range(colunas):
                valores = [m[i][j] for m in lista_matrizes]
                conta_visual = " + ".join(str(v) for v in valores)
                print(f"Posição [{i + 1}][{j + 1}]: {conta_visual} = {sum(valores)}")

    def subt_matriz():
        matriz = []
        resultado = []
        escolhidas = []

        if len(matrizes) > 2:  # verifica se tem mais de 2 matrizes no array
            if mesma_ordem(matrizes):
                escolhidas = escolher_matrizes(matrizes)
                linhas = len(matrizes[0])
                colunas = len(matrizes[0][0])

                for linha in matrizes[escolhidas[0]]:
                    resultado.append(linha.copy())

                for indice in escolhidas[1:]:
                    matriz = matrizes[indice]
                    for i in range(linhas):
                        for j in range(colunas):
                            resultado[i][j] -= matriz[i][j]

                ver_passo = input("\nDeseja ver o passo a passo da subtração? (S/N): ").upper()
                if ver_passo == "S":
                    matrizes_para_explicar = [matrizes[idx] for idx in escolhidas]
                    explicar_subt_multipla(matrizes_para_explicar)

                return resultado
            else:
                print("As matrizes não possuem a mesma ordem para serem subtraídas.")
                return None

        elif len(matrizes) == 2:
            if mesma_ordem(matrizes):
                linhas = len(matrizes[0])
                colunas = len(matrizes[0][0])

                for linha in matrizes[0]:
                    resultado.append(linha.copy())
                print("resultado após cópia:", resultado)

                for i in range(linhas):
                    for j in range(colunas):
                        resultado[i][j] -= matrizes[1][i][j]

            ver_passo = input("\nDeseja ver o passo a passo da subtração? (S/N): ").upper()
            if ver_passo == "S":
                explicar_subt(matrizes[0], matrizes[1])

            return resultado
        else:
            print("Crie outra matriz para realizar a subtração ")
            quantMatriz = int(input("\nQuantas matrizes você irá querer criar? "))
            for i in range(quantMatriz):
                criar_matriz()
            return subt_matriz()

    def explicar_subt(m1, m2):
        print("\n--- PASSO A PASSO DA SOMA ---")
        print("Para subtrair as matrizes, subtraímos os elementos que estão na mesma posição:")
        linhas = len(m1)
        colunas = len(m1[0])

        for i in range(linhas):
            for j in range(colunas):
                v1 = m1[i][j]
                v2 = m2[i][j]
                print(f"Posição [{i + 1}][{j + 1}]: {v1} - {v2} = {v1 - v2}")

    def explicar_subt_multipla(lista_matrizes):
        print("\n--- PASSO A PASSO DA SUBTRAÇÃO (MÚLTIPLAS MATRIZES) ---")
        print("Subtraímos os elementos correspondentes das matrizes na ordem selecionada:")
        linhas = len(lista_matrizes[0])
        colunas = len(lista_matrizes[0][0])

        for i in range(linhas):
            for j in range(colunas):
                valores = [m[i][j] for m in lista_matrizes]
                conta_visual = " - ".join(str(v) for v in valores)
                resultado_posicao = valores[0] - sum(valores[1:])

                print(f"Posição [{i + 1}][{j + 1}]: {conta_visual} = {resultado_posicao}")


    def mult_int():
        print("Matrizes disponiveis: ")
        mostrar_matrizes(matrizes)
        escolhida = []
        resultado = []
        escolhida = escolher_matriz(matrizes)
        linhas = len(matrizes[0])
        colunas = len(matrizes[0][0])
        m1 = matrizes[escolhida[0]]

        for linha in matrizes[escolhida[0]]:
            resultado.append(linha.copy())

        numero = int(input("Digite o número inteiro: "))
        for i in range(linhas):
            for j in range(colunas):
                resultado[i][j] *= numero

        ver_passo = input("\nDeseja ver o passo a passo da multiplicação? (S/N): ").upper()
        if ver_passo == "S":
            explicar_multint(m1, numero)

        return resultado

    def explicar_multint(m1, num1):
        print("\n--- PASSO A PASSO DA MULTIPLICAÇÃO POR NÚMERO INTEIRO ---")
        print("Para multiplicar matrizes com um número inteiro, multiplicamos cada elemento com tal número: ")
        linhas = len(m1)
        colunas = len(m1[0])

        for i in range(linhas):
            for j in range(colunas):
                v1 = m1[i][j]
                v2 = v1 * num1
                print(f"Posição [{i + 1}][{j + 1}]: {v1} x {v2} = {v2}")

    def mult_matriz():
        matriz = []
        resultado = []

        if len(matrizes) > 2:
            escolhidas = escolher_matrizes(matrizes)
            linhas = len(matrizes[0])
            colunas = len(matrizes[0][0])
            
            for linha in matrizes[escolhidas[0]]:
                resultado.append(linha.copy())

            for indice in escolhidas[1:]:
                matriz = matrizes[indice]

                if len(resultado[0]) != len(matriz):
                    print("Não é possível multiplicar.")
                    return None

                novo_resultado = []
                for i in range(len(resultado)):
                    linha = []
                    for j in range(len(matriz[0])):
                        soma = 0
                        for k in range(len(matriz)):
                            soma += resultado[i][k] * matriz[k][j]
                        linha.append(soma)
                    novo_resultado.append(linha)

            resultado = novo_resultado

            ver_passo = input("\nDeseja ver o passo a passo da multiplicação? (S/N): ").upper()
            if ver_passo == "S":
                explicar_multmat(
                    matrizes[escolhidas[0]],
                    matrizes[escolhidas[1]]
                )

            return resultado
        elif len(matrizes) == 2:
            escolhidas = escolher_matriz()
            
            for linha in matrizes[escolhidas[0]]:
                resultado.append(linha.copy())
                
            for indice in escolhidas[1]:
                matriz = matrizes[indice]
                
                if len(resultado[0]) != len(matriz):
                    print("Não é possível multiplicar.")
                    return None
                
                novo_resultado = []
                for i in range(len(resultado)):
                    linha = []
                    for j in range(len(matriz[0])):
                        soma = 0
                        for k in range(len(matriz)):
                            soma += resultado[i][k] * matriz[k][j]
                        linha.append(soma)
                    novo_resultado.append(linha)
                resultado = novo_resultado 
                
            ver_passo = input("\nDeseja ver o passo a passo da multiplicação? (S/N): ").upper()
            if ver_passo == "S":
                explicar_multmat(
                    matrizes[escolhidas[0]],
                    matrizes[escolhidas[1]]
                )

            return resultado
            
        else:
            print("Crie outra matriz para realizar a multiplicação ")
            quantMatriz = int(input("\nQuantas matrizes você irá querer criar? "))
            for i in range(quantMatriz):
                criar_matriz()
            return mult_matriz()
        
    def explicar_multmat(m1, m2):
        print("\n--- PASSO A PASSO DA MULTIPLICAÇÃO DE MATRIZES ---")
        print("Para multiplicar duas matrizes, multiplicamos os elementos na mesma posição:")
        linhas = len(m1)
        colunas = len(m1[0])

        for i in range(linhas):
            for j in range(colunas):
                v1 = m1[i][j]
                v2 = m2[i][j]
                print(f"Posição [{i + 1}][{j + 1}]: {v1} x {v2} = {v1 * v2}")

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
                print(f"posição [{i + 1}][{j + 1}] -> [{j + 1}][{i + 1}] = {matriz[i][j]}")

                nova_linha.append(matriz[i][j])

            resultado.append(nova_linha)

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
            return []

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


    for i in range(quantMatriz):
        criar_matriz()


    def calculo():
        print("\n === Calculadora ==="
              "\n1 - Soma"
              "\n2 - Subtração"
              "\n3 - Multiplicação por número inteiro"
              "\n4 - Multiplicação por outra matriz"
              "\n5 - Matriz transposta"
              "\n6 - Determinante"
              "\n7 - Matriz inversa"
              "\n0 - Sair do programa")
        calc = int(input("\nEscolha uma opção: "))
        if (calc == 0):
            fechar_programa()

        if (calc == 1):
            resultado = adicao_matriz()

            if resultado != None:
                print("\nResultado da adição: ")
                time.sleep(2)
                mostrar_matriz(resultado)
                time.sleep(3)

            print("\n === Calculadora ==="
                  "\n1 - Deseja fechar o programa"
                  "\n2 - Escolher operação"
                  "\n3 - Fazer novas matrizes")
            exc = int(input())
            if exc == 1:
                fechar_programa()
            if exc == 2:
                return calculo()
            if exc == 3:
                criar_matriz()

        if (calc == 2):
            resultado = subt_matriz()
            
            if resultado != None:
                print("\nResultado da subtração: ")
                time.sleep(2)
                mostrar_matriz(resultado)
                time.sleep(3)

            print("\n === Calculadora ==="
                  "\n1 - Deseja fechar o programa"
                  "\n2 - Escolher operação"
                  "\n3 - Fazer novas matrizes")
            exc = int(input())
            if exc == 1:
                fechar_programa()
            if exc == 2:
                return calculo()
            if exc == 3:
                criar_matriz()

        if (calc == 3):
            resultado = mult_int()
            
            if resultado != None: 
                print("\nResultado da multiplicação por número inteiro: ")
                time.sleep(2)
                mostrar_matriz(resultado)
                time.sleep(3)

            print("\n === Calculadora ==="
                  "\n1 - Deseja fechar o programa"
                  "\n2 - Escolher operação"
                  "\n3 - Fazer novas matrizes")
            exc = int(input())
            if exc == 1:
                fechar_programa()
            if exc == 2:
                return calculo()
            if exc == 3:
                criar_matriz()

        if (calc == 4):
            resultado = mult_matriz()
            
            if resultado != None: 
                print("\nResultado da multiplicação de matrizes: ")
                time.sleep(2)
                mostrar_matriz(resultado)
                time.sleep(3)

            print("\n === Calculadora ==="
                  "\n1 - Deseja fechar o programa"
                  "\n2 - Escolher operação"
                  "\n3 - Fazer novas matrizes")
            exc = int(input())
            if exc == 1:
                fechar_programa()
            if exc == 2:
                return calculo()
            if exc == 3:
                criar_matriz()

        if calc == 5:
            resultado = matriz_transposta()
            
            if resultado != None:
                print("\nResultado da matriz transposta: ")
                time.sleep(2)
                mostrar_matriz(resultado)
                time.sleep(3)

            print("\n === Calculadora ==="
                  "\n1 - Deseja fechar o programa"
                  "\n2 - Escolher operação"
                  "\n3 - Fazer novas matrizes")
            exc = int(input())
            if exc == 1:
                fechar_programa()
            if exc == 2:
                return calculo()
            if exc == 3:
                criar_matriz()

        if calc == 6:
            resultado = determinante()
            
            if resultado != None: 
                print("\nResultado do determinante:")
                time.sleep(2)
                print(resultado)
                time.sleep(3)

            print("\n === Calculadora ==="
                  "\n1 - Deseja fechar o programa"
                  "\n2 - Escolher operação"
                  "\n3 - Fazer novas matrizes")
            exc = int(input())
            if exc == 1:
                fechar_programa()
            if exc == 2:
                return calculo()
            if exc == 3:
                criar_matriz()

        if calc == 7:
            resultado = matriz_inversa()

            if resultado != None:
                print("\nResultado da matriz inversa: ")
                time.sleep(2)
                mostrar_matriz(resultado)
                time.sleep(3)

            print("\n === Calculadora ==="
                  "\n1 - Deseja fechar o programa"
                  "\n2 - Escolher operação"
                  "\n3 - Fazer novas matrizes")
            exc = int(input())
            if exc == 1:
                fechar_programa()
            if exc == 2:
                return calculo()
            if exc == 3:
                criar_matriz()


    print("\nMatrizes Geradas: ")
    mostrar_matrizes(matrizes)
    calculo()
