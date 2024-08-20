import math

#Fazer a soma
def somar(a, b):
    return a + b
#Fazer a subtração
def subtrair(a, b):
    return a - b
#Fazer a multiplicação
def multiplicar(a, b):
    return a * b
#Fazer a divisão
def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b
#Encontrar a raiz quadrada (esqueci como se diz)
def raiz_quadrada(a):
    if a < 0:
        return "Erro: Número negativo!"
    return math.sqrt(a)