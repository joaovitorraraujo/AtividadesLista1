# faça um programa que solicite a senha do usuário 
# caso o usuário digite a senha correta, exibir a mensagem 
# "logado com sucesso" e terminar execução. Se o usuário errar 
# 3 vezes exibir "Resta apenas uma tentativa", caso erre a senha 4 vezes exibir "usuário bloqueado"
import getpass

senha = input('Olá, crie uma senha:')
print("Senha registrada com sucesso!")

contador = 0

while contador<4:
    digitado = getpass.getpass('Digite sua senha  e confirme com "enter"(para sua segurança, a senha digitada não será exibida):')
    if digitado == senha:
        print("Logado com sucesso")
        break
    else:
        contador+=1
        tentativas = 3 - contador

        if tentativas == 0:
            print("Usuário bloqueado")
            break
        elif tentativas == 1:
            print("Resta apenas uma tentaiva")
        else:
                print(f'Restam {tentativas} tentativas.')
            



