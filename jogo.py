import time

print(" ")
print("******************************************************")
print("************* Bem vindo ao jogo da forca *************")
print("******************************************************")
print(" ")

time.sleep(1)

print("Você tem a opção de escolher os níveis conforme abaixo")
print(" ")
print("[ 1 ] Nível fácil - você terá 10 chances")
print("[ 2 ] Nível médio - você terá 7 chances")
print("[ 3 ] Nível difícil - você terá 4 chances")
print(" ")

nivel = int(input("Qual nível você deseja escolher"))



palavra_secreta = "BANANA"
letras_escolhidas = []
situacao_atual = ["_"] * len(palavra_secreta)

# TRANSFORMA A PALAVRA SECRETA EM UMA LISTA
palavra_secreta = " ".join(palavra_secreta).split()
