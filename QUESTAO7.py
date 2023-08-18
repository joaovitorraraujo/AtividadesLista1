# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a
# pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
# "Assassino". Caso contrário, ele será classificado como "Inocente".

print("Ouve um crime e você será julgado!!!\nPor Favor,responda as perguntas com apenas 'sim' ou 'não':")

contador = 0

pergunta1 = input("Telefonou para a vítima? ")
if pergunta1.lower() == "sim":
    contador  += 1

pergunta2 = input("Esteve no local do crime? ")
if pergunta2.lower() == "sim":
    contador  += 1

pergunta3 = input("Mora perto da vítima? ")
if pergunta3.lower() == "sim":
    contador  += 1

pergunta4 = input("Devia para a vítima? ")
if pergunta4.lower() == "sim":
    contador  += 1

pergunta5 = input("Já trabalhou com a vítima? ")
if pergunta5.lower() == "sim":
    contador  += 1

if contador  == 2:
    classificacao = "Suspeita"
elif contador ==3 or contador ==4:
    classificacao = "Cúmplice"
elif contador == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"Classificação: {classificacao}")
