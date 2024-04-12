#Faça um programa que solicite ao usuário os valores das 4 notas do bimestre. E calcule o valor da média.
nota_1 = float(input("Digite o valor da nota 1: "))
nota_2 = float(input("Digite o valor da nota 2: "))
nota_3 = float(input("Digite o valor da nota 3: "))
nota_4 = float(input("Digite o valor da nota 4: "))

media = (nota_1+nota_2+nota_3+nota_4)/4

print("A média das notas é:",media)