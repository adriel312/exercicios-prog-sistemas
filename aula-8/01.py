print("M - Masculino F - Feminino")
sexo = input("Informe seu sexo: ")

if sexo == "m" or sexo == "M":
    altura = float(input("Informe sua altura: "))
    if altura >= 1.70:
        print("Você está apto a se alistar")
    else:
        print("Você não está apto a se alistar")
elif sexo =="f" or sexo =="F":
    altura = float(input("Informe sua altura: "))
    if altura >= 1.60:
        print("Você está apto a se alistar")
    else:
        print("Você não está apto a se alistar")
else:
    print("Informe um sexo válido!")