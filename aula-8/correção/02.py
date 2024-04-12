lado_1 = float(input("Informe o tamanho do lado 1: "))
lado_2 = float(input("Informe o tamanho do lado 2: "))
lado_3 = float(input("Informe o tamanho do lado 3: "))

if lado_1==lado_2==lado_3:
    print("Triângulo Equilatero")
elif lado_1!=lado_2!=lado_3:
    print("Triângulo Escaleno")
else:
    print("Isósceles")