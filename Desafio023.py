#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input("Digite um número de 0 até 9999: "))
milhar = num // 1000
centena = (num % 1000) // 100
dezena = (num % 100) // 10
unidade = num % 10
print("unidade: {}" .format(unidade))
print("dezena: {}" .format(dezena))
print("centena: {}" .format(centena))
print("milhar: {}" .format(milhar))