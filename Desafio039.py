'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar 
ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento

if idade == 18:
    print("Está na hora de se alistar!")
elif idade < 18:
    tempo = 18 - idade
    print("Ainda não está na hora de se alistar, faltam {} anos." .format(tempo))
else:
    tempo = idade - 18
    print("Já se passaram {} anos desde a sua época de alistamento." .format(tempo))
