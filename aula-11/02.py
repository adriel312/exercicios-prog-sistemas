nota = float(input("Informe uma nota: "))

while nota<0 or nota>10:
    print("Informe uma nota maior que 0 e menor que 10")
    nota = float(input("Informe uma nota: "))
print("Nota inserida com sucesso!")