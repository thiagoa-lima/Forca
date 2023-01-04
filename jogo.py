import time

# ------------------------------------------------------------
# --------------- MENSAGEM DE ABERTURA DO JOGO ---------------
# ------------------------------------------------------------

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
        chances = 10
    elif nivel == 2:
        chances = 7
    elif nivel == 3:
        chances = 4
    else:

        print("\nOpção ínvalida. Vamos começar novamente?")
        print(" ")
        time.sleep(1)
        print("******************************************************\n")


# ------------------------------------------------------------
# ---------------------- Início do jogo ----------------------
# ------------------------------------------------------------

tentativas = 0
chances = chances
palavra_secreta = "BANANA"
situacao_atual = ["_"] * len(palavra_secreta)
letras_escolhidas = []

time.sleep(1)
print(f"Muito bem!! ")
print(f"A partir de agora você tem {chances} chances para concluir o jogo.")
print("")
print("******************************************************")
print(f"**** VAMOS COMEÇAR? A palavra abaixo tem {len(situacao_atual)} letras ****")
print("******************************************************")
print("")

# ------------------------------------------------------------
# -------------------- Escolha das letras --------------------
# ------------------------------------------------------------

while tentativas < chances:
    letra = str(input("Qual letra você gostaria de tentar? ")).upper()
    letras_escolhidas.append(letra)

    if letra in palavra_secreta:
        print(f"\nPARABÉNS! A palavra secreta contem a letra {letra.upper()}")

    else:
        print("QUE PENA! Essa letra não tem na palavra secreta")
        tentativas += 1
        print(f"Você já tentou {tentativas} vezes e ainda tem mais {chances - tentativas} chances")

    print(" ".join(situacao_atual).strip())
    print("As letras que voce ja utilizou foram:")
    print("  ".join(letras_escolhidas).strip())
    print("")
