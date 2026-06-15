
import time
matrizes = [] # agrupa todas as matrizes

print("Bem-vindo ao programa de operações envolvendo matrizes")
time.sleep(3)
print("\033[H\033[J", end="")

while True: 

    quantMatriz = int(input("Quantas matrizes você quer gerar? "))

    def criar_matriz():
        print(f"\nMatriz {i + 1}:")
        lin = int(input("Coloque o número de linhas da sua matriz: ")) 
        col = int(input("Coloque o número de colunas da sua matriz: "))
        
        matriz = [] # cria apenas uma matriz

        print("Digite os números da sua matriz:") 

        for l in range(lin): # função de adicionar valores

            linha = []

            for j in range(col):
                valor = float(input(f"Digite o valor para a posição [{l+1}][{j+1}]: "))
                linha.append(valor)
            matriz.append(linha) 
        matrizes.append(matriz) # adiciona o valor a linha, da linha para a matriz, e da matriz para o grupo de matrizes

    def mostrar_matriz(lista):
        for indice, matriz in enumerate(matrizes):
            lin = len(matriz)
            col = len(matriz[0])
            print(f"\nMatriz {indice + 1}:") # mostra todas as matrizes
            print(f"Dimensão: {lin} x {col}")
            for linha in matriz:
                print(linha)

    def mesma_ordem(lista):
        linhas = len(matrizes)
        colunas = len(matrizes[0])

        for matriz in matrizes: 
            if len(matriz) != linhas:
                return False
            if len(matriz[0]) != colunas:
                return False
        return True

    def adicao_matriz():
        print("Matrizes disponiveis:")
        mostrar_matriz(matrizes)
        resultado = []
        escolhidas = []
        print("Quantas você irá querer utilizar?")
        ma = int(input()) 

        if mesma_ordem(matrizes):
            for l in range(ma):
                quant = int(input("Digite qual você irá querer utilizar: "))
                escolhidas.append(quant-1)

            linhas = len(matrizes)
            colunas = len(matrizes[0])
            
            for linha in matrizes[escolhidas[0]]:
                resultado.append(linha.copy())

            for indice in escolhidas[1:]:
                matriz = matrizes[indice]
                
                for i in range(linhas):

                    for j in range(colunas):

                        resultado[i][j] += matriz[i][j]

            return resultado
    
    def subt_matriz():
        print("Matrizes disponiveis:")
        mostrar_matriz(matrizes)
        resultado = []
        escolhidas = []
        print("Quantas você irá querer utilizar?")
        ma = int(input()) 

        if mesma_ordem(matrizes):
            for l in range(ma):
                quant = int(input("Digite quais você irá querer utilizar: "))
                escolhidas.append(quant-1)

            linhas = len(matrizes)
            colunas = len(matrizes[0])

            for linha in matrizes[escolhidas[0]]:
                resultado.append(linha.copy())

            for indice in escolhidas[1:]:
                matriz = matrizes[indice]
                
                for i in range(linhas):

                    for j in range(colunas):

                        resultado[i][j] -= matriz[i][j]

        return resultado
        
    def mult_int():
        print("Matrizes disponiveis: ")
        mostrar_matriz(matrizes)

        escolhida = []
        resultado = []
        ma = int(input("Escolha a matriz: "))
        escolhida.append(ma-1)
        linhas = len(matrizes)
        colunas = len(matrizes[0])

        for linha in matrizes[resultado[0]]:
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
    
    # para ver se a matriz tem a mesma quantidade
    # de linha e colunas
    def calculo():
        print("\n === Calculadora ==="
            "\n1 - Soma"
            "\n2 - subtração"
            "\n3 - Multiplicação por outra matriz"
            "\n4 - Multiplicação por numero inteiro"
            "\n0 - Sair do programa" )
        calc = int(input("\nEscolha uma opção: "))

        if (calc == 1):
            resultado = adicao_matriz()
            print("\nResultado da adição: ")
            mostrar_matriz(resultado)
            
            print("\n === Calculadora ==="
                "\n1 - Deseja fechar o programa" 
                "\n2 - Escolher operação"
                "\n3 - Fazer/trocar matrizes" )
            exc = int(input())
            if exc ==  1:
                return False; 
            if exc == 2:
                return calculo
            if exc == 3:
                criar_matriz() 
                
        if(calc == 2):
            resultado = subt_matriz()
            print("\nResultado da subração: ")
            mostrar_matriz(resultado)
            
            print("\n === Calculadora ==="
                "\n1 - Deseja fechar o programa" 
                "\n2 - Escolher operação"
                "\n3 - Fazer/trocar matrizes" )
            exc = int(input())
            if exc ==  1:
                return False; 
            if exc == 2:
                return calculo
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
                return False
            if exc == 2:
                return calculo
            if exc == 3:
                criar_matriz()

    print("\nMatrizes Geradas: ")
    mostrar_matriz(matrizes)
    calculo()
    if calculo == False:
        break
