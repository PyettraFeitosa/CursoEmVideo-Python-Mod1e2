#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o seu salário: "))

if salario > 1250:
    novo_sal = salario + (salario * 0.1)
    print("Seu novo salário é: {}." .format(novo_sal))
else:
    novo_sal = salario + (salario * 0.15)
    print("Seu novo salário é: {}." .format(novo_sal))