acumulador = 0
num = int(input("Informe um número: "))

while num != 0:
    #acumulador = acumulador + num
    acumulador += num
    num = int(input("Informe um número: "))
print(acumulador)
