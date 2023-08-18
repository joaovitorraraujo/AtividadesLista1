#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a
#mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
import getpass

print('Olá')
print('Em que turno você estuda?')
turno = getpass.getpass("M-matutino\nV-Vespertino\nN- Noturno\nAPERTE A LETRA E ENTER PARA CONFIRMAR!!!")

match turno.lower():
    case "m":
        print("Bom Dia!")
    case "v":
        print("Bom Tarde!")
    case "n":
        print("Boa Noite!")
    case _:
        print("Valor Inválido")
    
