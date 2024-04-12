#Faça um programa que leia 5 números e informe o maior número.
maior = 0   #variável para guardar o valor do maior número

for i in range(5):  #loop com 5 iterações
    numero = int(input("Informe um número: ")) #5 vezes iremos pedir um número
    if numero > maior:  #confere se o número que acabei de informar é maior que o meu maior número encontrado até agora
        maior = numero  #se o novo número digitado for maior que todos, ele sera meu novo maior

print("O maior número é",maior)