#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
numero_1 = int(input("Informe o número 1: "))
numero_2 = int(input("Informe o número 2: "))

while numero_1 <= numero_2: #enquanto o número_1 for menor ou igual a numero_2, iremos imprimir o menor número e somar +1 para imprimir o número depois dele, e continuar o loop
    print(numero_1)
    numero_1 += 1