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

print("Bem-vindo ao programa de operações envolvendo matrizes")
time.sleep(2) # Espera para o usuário ler

print("\033[H\033[J", end="") # Apaga o texto do prompt

quantMatriz = int(input("Quantas matrizes você quer gerar? ")) # Por enquanto só guarda quantas matrizes o usuário quer fazer, não foi usada ainda
m = int(input("Coloque o número de linhas da sua matriz: "))
n = int(input("Coloque o número de colunas da sua matriz: "))
matriz = []

print("Digite os números da sua matriz:")
for i in range(m):
    linha = []
    for j in range(n):
        valor = int(input(f"Digite o valor para a posição [{m}, {n}]: "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print("Matriz gerada:")
    print(linha)

print("")
operMatriz = int(input("Qual operação você deseja fazer?\n"))
