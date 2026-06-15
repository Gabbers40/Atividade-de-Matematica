#Código do Angelo
# Teste teste github extension worked yay
# O que adicionei:
# Função "fechar_programa" para sair do programa
# Edição no código de mostrar matriz
# Código da função calcular() quase completo
# Criação da função de explicar passo a passo das contas
# Notas

import time
import sys
matrizes = [] # agrupa todas as matrizes

print("Bem-vindo ao programa de operações envolvendo matrizes")
time.sleep(3)
print("\033[H\033[J", end="")

while True: 

    quantMatriz = int(input("Quantas matrizes você quer gerar? "))

    def fechar_programa():
        dec = str(input("Você deseja sair do programa? S/N : ")).upper()
        if dec == "S":
            print("Saindo do programa...")
            time.sleep(3)
            sys.exit()
        elif dec == "N":
            return

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
        for indice, matriz in enumerate(lista):
            lin = len(matrizes[0])
            col = len(matrizes[0][0])
            print(f"\nMatriz {indice + 1}:") # mostra todas as matrizes
            print(f"Dimensão: {lin} x {col}")
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
        mostrar_matriz(matrizes)
        resultado = []
        escolhidas = []
        print("Quantas você irá querer utilizar?")
        ma = int(input()) 

        if mesma_ordem(matrizes):
            for l in range(ma):
                quant = int(input("Digite qual você irá querer utilizar: "))
                escolhidas.append(quant-1)

            linhas = len(matrizes[0])
            colunas = len(matrizes[0][0])
            
            resultado = [[0 for _ in range(colunas)] for _ in range(linhas)]
        
            passo_a_passo = "Passo a passo da Adição:\n"

            for i in range(linhas):
                for j in range(colunas):
                    termos_soma = []
                    soma_posicao = 0
                    
                    for idx in escolhidas:
                        valor = matrizes[idx][i][j]
                        termos_soma.append(str(valor))
                        soma_posicao += valor
                    
                    resultado[i][j] = soma_posicao
                    
                    passo_a_passo += f"  Posição [{i+1}][{j+1}]: {' + '.join(termos_soma)} = {soma_posicao}\n"

            print("\n" + passo_a_passo)
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

            linhas = len(matrizes[escolhidas[0]])
            colunas = len(matrizes[escolhidas[0]][0])

            resultado = [[0 for _ in range(colunas)] for _ in range(linhas)]
            
            passo_a_passo = "Passo a passo da Subtração:\n"

            for i in range(linhas):
                for j in range(colunas):
                    termos_sub = []
                    
                    sub_posicao = matrizes[escolhidas[0]][i][j]
                    termos_sub.append(str(sub_posicao))
                    
                    for idx in escolhidas[1:]:
                        valor = matrizes[idx][i][j]
                        termos_sub.append(str(valor))
                        sub_posicao -= valor
                    
                    resultado[i][j] = sub_posicao
                    
                    passo_a_passo += f"  Posição [{i+1}][{j+1}]: {' - '.join(termos_sub)} = {sub_posicao}\n"

            print("\n" + passo_a_passo)
            return resultado
        
    def mult_int():
        print("Matrizes disponiveis: ")
        mostrar_matriz(matrizes)

        ma = int(input("Escolha a matriz: "))
        idx_matriz = ma - 1
        linhas = len(matrizes[idx_matriz])
        colunas = len(matrizes[idx_matriz][0])

        resultado = [[0 for _ in range(colunas)] for _ in range(linhas)]
        numero = float(input("Digite o número multiplicador: "))
        
        passo_a_passo = f"Passo a passo da Multiplicação por {numero}:\n"

        for i in range(linhas):
            for j in range(colunas):
                valor_original = matrizes[idx_matriz][i][j]
                resultado[i][j] = valor_original * numero
                
                passo_a_passo += f"  Posição [{i+1}][{j+1}]: {valor_original} x {numero} = {resultado[i][j]}\n"

        print("\n" + passo_a_passo)
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
    def calculo(): # Nota de Angelo: Não dá pra usar if com else aqui ou tanto faz?
        print("\n === Calculadora ==="
            "\n1 - Soma"
            "\n2 - Subtração"
            "\n3 - Multiplicação por outra matriz"
            "\n4 - Multiplicação por numero inteiro"
            "\n0 - Sair do programa" )
        calc = int(input("\nEscolha uma opção: "))

        if (calc == 1):
            resultado = adicao_matriz()
            print("\nResultado da adição: ")
            time.sleep(1)
            mostrar_matriz(resultado)
            time.sleep(3)
            
            print("\n === Calculadora ==="
                "\n1 - Deseja fechar o programa" 
                "\n2 - Escolher operação"
                "\n3 - Fazer/trocar matrizes" )
            exc = int(input())
            if exc == 1:
                fechar_programa()
            if exc == 2:
                return calculo()
            if exc == 3:
                criar_matriz() 
                
        if(calc == 2):
            resultado = subt_matriz()
            print("\nResultado da subtração: ")
            time.sleep(3)
            mostrar_matriz(resultado)
            time.sleep(3)
            
            print("\n === Calculadora ==="
                "\n1 - Deseja fechar o programa" 
                "\n2 - Escolher operação"
                "\n3 - Fazer/trocar matrizes" )
            exc = int(input())
            if exc ==  1:
                fechar_programa()
            if exc == 2:
                return calculo()
            if exc == 3:
                criar_matriz()

        if (calc == 3):
            resultado = mult_int()
            print("\nResultado da multiplicação : ")
            time.sleep(3)
            mostrar_matriz(resultado)
            time.sleep(3)

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

        if (calc == 4): # editar depois para multiplicação por número inteiro
            resultado = mult_int()
            print("\nResultado da multiplicação por número inteiro : ")
            time.sleep(3)
            mostrar_matriz(resultado)
            time.sleep(3)

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

        if (calc == 0):
            fechar_programa()

    print("\nMatrizes Geradas: ")
    mostrar_matriz(matrizes)
    calculo()
