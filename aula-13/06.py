#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!= 5*4*3*2*1=120
numero = int(input("Informe o número que você quer descobrir o fatorial: "))
fatorial = numero   #o primeiro valor do calculo do fatorial deve ser o número inserido

for i in range(numero-1,1,-1):  #iremos fazer um loop que começa no número após o primeiro, no exemplo iriamos começar em 4, e diminuir de 1 em 1 até 1
    fatorial = fatorial * i     #o resultado do fatorial seria o número anterior multiplicado pelo proximo número da sequencia, o i
print("O fatorial de",numero,"! =",fatorial)