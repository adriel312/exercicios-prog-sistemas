print("M - matutino, V - vespertino, N - noturno")
turno = input("Digite o turno que você estuda: ")

if turno == "m":
    print("Bom dia!")
elif turno == "v":
    print("Boa tarde!")
elif turno == "n":
    print("Boa noite!")
else:
    print("Valor Inválido!")