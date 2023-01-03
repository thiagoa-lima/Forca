import time

print(" ")
print("******************************************************")
print("************* Bem vindo ao jogo da forca *************")
print("******************************************************")
print(" ")

time.sleep(1)
nivel = 0

while nivel != 1 and nivel != 2 and nivel != 3:
    print("Você tem a opção de escolher os níveis conforme abaixo")
    print(" ")
    print("[ 1 ] Nível fácil - você terá 10 chances")
    print("[ 2 ] Nível médio - você terá 7 chances")
    print("[ 3 ] Nível difícil - você terá 4 chances")
    print(" ")

    nivel = int(input("Qual nível você deseja escolher: "))

    if nivel == 1:
        chance = 10
    elif nivel == 2:
        chance = 7
    elif nivel == 3:
        chance = 4
    else:
        print(" ")
        print("Opção ínvalida. Vamos começar novamente?")
        print(" ")
        time.sleep(1)
        print("******************************************************")
        print(" ")


palavra_secreta = "BANANA"
letras_escolhidas = []
situacao_atual = ["_"] * len(palavra_secreta)

# TRANSFORMA A PALAVRA SECRETA EM UMA LISTA
palavra_secreta = " ".join(palavra_secreta).split()
