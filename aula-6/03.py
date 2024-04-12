num_1 = int(input("Informe o valor para numero 1: "))
num_2 = int(input("Informe o valor para numero 2: "))
num_3 = int(input("Informe o valor para numero 3: "))

if num_1>num_2 and num_1>num_3:
    print(num_1,"é o maior número")
elif num_2>num_1 and num_2>num_3:
    print(num_2,"é o maior número")
else:
    print(num_3,"é o maior número")