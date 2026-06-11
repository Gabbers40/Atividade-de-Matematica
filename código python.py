# Implementar em Python. Não é permitido usar nenhuma função ou biblioteca pronta para cálculo matemático (por exemplo a Num.py): todas as funções deverão ser construídas do zero.
# O programa deverá ser capaz de:
# --> receber as dimensões das matrizes, a quantidade de matrizes, e os elementos das matrizes (números reais) através de interface com o usuário;
# --> perguntar ao usuário, a partir da entrada fornecida, o que ele deseja fazer (por exemplo, se entrou com uma matriz de ordem 2x3, a função de determinante não estará disponível).
# --> deve ser capaz de calcular: soma/subtração de matrizes, multiplicação de matrizes, multiplicação de matriz por número inteiro, matriz transposta (e cálculos com a transposta gerada), matriz inversa, determinante.
# --> deverá ser capaz de exportar o resultado.
# --> IMPORTANTE: O PROGRAMA NÃO DEVE SÓ APRESENTAR O RESULTADO, MAS MOSTRAR O PASSO-A-PASSO DAS OPERAÇÕES.
# Apresentação/entrega do código, demonstração do programa e resposta a pergunta que o professor irá fazer sobre o código.
import time

MENU = 0
matrizes = [] # agrupa todas as matrizes

print("Bem-vindo ao programa de operações envolvendo matrizes")
time.sleep(3)

print("\033[H\033[J", end="")

quantMatriz = int(input("Quantas matrizes você quer gerar? "))

for i in range(quantMatriz):
    print(f"\nMatriz {i + 1}:")
    m = int(input("Coloque o número de linhas da sua matriz: ")) 
    n = int(input("Coloque o número de colunas da sua matriz: "))

    matriz = [] # cria apenas uma matriz

    print("Digite os números da sua matriz:") 

    for i in range(m): # função de adicionar valores

        linha = []

        for j in range(n):

            valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)

        matriz.append(linha) 

    matrizes.append(matriz) # adiciona o valor a linha, da linha para a matriz, e da matriz para o grupo de matrizes

print("\nMatrizes Geradas: ")

for indice, matriz in enumerate(matrizes):

    print(f"\nMatriz {indice + 1}:") # mostra todas as matrizes

    for linha in matriz:
        print(linha)

# para ver se a matriz tem a mesma quantidade
# de linha e colunas
if ( m = n )

# teste cálculo matriz soma/subtração - Angelo
# Na teoria, eu teria que criar uma função para criar variáveis
# de cada elemento de cada matriz, onde essa variável guarda o
# valor de a11, e outra guarda a de a12 e assim em diante.
# No fim, a varíavel mat1elem1 soma com o mat2elem1,
# o mat1elem2 soma com o mat2elem2 até somar o último elemento
# da matriz1 com a da matriz2. Aí usa matriz.append(linha) e
# matrizes.append(matriz) para gerar a matriz resultante e imprimir.
mat1elem1 = matrizes[0][0][0]
mat1elem2 = matrizes[0][0][1]
mat1elem3 = matrizes[0][1][0]
mat1elem4 = matrizes[0][1][1]

mat2elem1 = matrizes[1][0][0]
mat2elem2 = matrizes[1][0][1]
mat2elem3 = matrizes[1][1][0]
mat2elem4 = matrizes[1][1][1]
