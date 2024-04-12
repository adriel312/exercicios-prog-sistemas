print("1 - Celsius para Fahrenheit 2 - Fahrenheit para Celsius")
opcao = int(input("Informe a opção desejada"))

if opcao == 1:
    temperatura = float(input("Informe a temperatura em Celsius: "))
    print("O valor de", temperatura,"C é igual a",(temperatura * 9/5) + 32,"F")
elif opcao == 2:
    temperatura = float(input("Informe a temperatura em Fahrenheit: "))
    print("O valor de", temperatura,"F é igual a",(temperatura - 32) * 5/9,"C")
else:
    print("Você informou uma opção inválida!")