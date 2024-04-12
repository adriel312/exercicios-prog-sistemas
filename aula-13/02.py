'''Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';'''

nome = input("Insira seu nome: ")
while len(nome) <= 2:   #len(nome) retorna o tamanho do nome inserido pelo usuário  #while verifica enquanto o nome tiver menos que 2 letras e pede para usuário inserir um nome válido
    print("Informe um nome com mais de 2 caracteres!!!")
    nome = input("Insira seu nome novamente: ")

idade = int(input("Informe a sua idade: "))
while idade<0 and idade>150:    #enquanto a idade for menor que 0 e maior que 150 pedir para informar novamente
    print("Informe uma idade válida (Maior que 0 e menor que 150)!")
    idade = int(input("Informe a sua idade novamente: "))

salario = float(input("Informe o seu salário: "))
while salario<0:    #enquanto o salario for menor que 0 pedir para informar novamente
    print("Informe uma salário maior que 0!")
    salario = float(input("Informe o seu salário novamente: "))

sexo = input("Informe o seu sexo: ").lower()    #.lower(), função para transformar tudo que foi digitado em minusculo
while sexo!="f" and sexo!="m":  #enquanto o sexo for diferente de m e f, informar novamente
    print("Informe um sexo compátivel, f - feminino m - masculino")

estado_civil = input("Informe seu estado civil: ")
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":  #enquanto o estado civil for diferente de um valor certo, informar novamente
    print("Estado Civil inválido, s - solteiro(a) c - casado(a) v - viuvo(a) d - divorciado(a)")
    estado_civil = input("Informe seu estado civil novamente: ")