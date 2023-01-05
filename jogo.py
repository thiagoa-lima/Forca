import random
import time

def jogar():

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

    while nivel not in [1, 2, 3]:
        print("Você tem a opção de escolher os níveis conforme abaixo")
        print(" ")
        print("[ 1 ] NÍVEL FÁCIL - você terá 10 chances")
        print("[ 2 ] NÍVEL MÉDIO - você terá 7 chances")
        print("[ 3 ] NIVEL DIFÍCIL - você terá 4 chances")
        print(" ")

        nivel = int(input("Qual nível você deseja escolher: "))

        if nivel == 1:
            chances = 10
        elif nivel == 2:
            chances = 7
        elif nivel == 3:
            chances = 4
        else:
            print(" ")
            print("Opção ínvalida. Vamos começar novamente?")
            print(" ")
            time.sleep(1)
            print("******************************************************")
            print(" ")

    # ------------------------------------------------------------
    # ---------------------- Início do jogo ----------------------
    # ------------------------------------------------------------

    tentativas = 0
    chances = chances
    palavra_secreta = carrega_palavra_secreta()
    situacao_atual = ["_"] * len(palavra_secreta)
    letras_escolhidas = []

    time.sleep(.5)
    print("")
    print(f"Muito bem!! ")
    print(f"Agora você tem [{chances}] chances para concluir o jogo.")
    print("")
    print("******************************************************")
    print(f"**** VAMOS COMEÇAR? A palavra abaixo tem {len(situacao_atual)} letras ****")
    print("******************************************************")
    print("")
    print("[ {} ]".format(" ".join(situacao_atual).strip()))
    print("")

    # ------------------------------------------------------------
    # -------------------- Escolha das letras --------------------
    # ------------------------------------------------------------

    while tentativas < chances and "_" in situacao_atual:
        print("******************************************************")
        letra = str(input("Qual letra você gostaria de tentar? ")).upper()
        print("******************************************************")
        if letra in letras_escolhidas:
            print("")
            print("Você já escolheu essa letra. Vamos tentar novamente?")
            print("")
            continue
        else:
            letras_escolhidas.append(letra)

        if letra in palavra_secreta:
            print(f"PARABÉNS, VOCÊ ACERTOU A LETRA [{letra}]!")
            print("")
            for i in range(len(palavra_secreta)):
                if letra == palavra_secreta[i]:
                    situacao_atual[i] = letra
            print("A palavra secreta é: [ {} ]".format(" ".join(situacao_atual).strip()))

        else:
            print(f"QUE PENA, VOCÊ ERROU A LETRA [{letra}]!")
            print("")
            print("[ {} ]".format(" ".join(situacao_atual).strip()))
            print("")
            tentativas += 1
            print(f"Você errou [{tentativas}] vezes e ainda tem mais [{chances - tentativas}] chances")

        print("")
        print("As letras que você já tentou foram:")
        print("[ {} ]".format(" ".join(letras_escolhidas).strip()))

        print("")

    # ------------------------------------------------------------
    # ----------------------- Fim do Jogo ------------------------
    # ------------------------------------------------------------

    if tentativas == chances:
        voce_perdeu(palavra_secreta)
    else:
        voce_ganhou()

    print("")
    print("Você quer jogar novamente?")

    jogar_novamente = 0
    while jogar_novamente not in ["S", "N"]:
        jogar_novamente = str(input("Digite 'S' pra sim e 'N' para não: ")).upper()
        if jogar_novamente == "S":
            jogar()
        elif jogar_novamente == "N":
            print("")
            print("******************************************************")
            print("******************** FIM DE JOGO *********************")
            print("******************************************************")
            print(" ")
            pass
        else:
            print("")
            print("Opção ínvalida.")

def voce_ganhou():
    print("|       Parabéns, você ganhou!      |")
    print("|            ___________            |")
    print("|           '._==_==_=_.'           |")
    print("|           .-\:      /-.           |")
    print("|          | (|:.     |) |          |")
    print("|           '-|:.     |-'           |")
    print("|             \::.    /             |")
    print("|              '::. .'              |")
    print("|                ) (                |")
    print("|              _.' '._              |")
    print("|             '-------'             |")


def voce_perdeu(palavra_secreta):
    print("Que pena, você foi ENFORCADO")
    print("         ______________          ")
    print("        /              \         ")
    print("       /                \        ")
    print("    /\/                  \/\     ")
    print("    \ |   XXXX    XXXX   | /     ")
    print("     \|   XXXX    XXXX   |/      ")
    print("      |   XXX      XXX   |       ")
    print("      |                  |       ")
    print("      \__      XX      __/       ")
    print("        |\     XX     /|         ")
    print("        | |          | |         ")
    print("        |  I I I I I   |         ")
    print("        |  I I I I I   |         ")
    print("        \_            _/         ")
    print("          \_        _/           ")
    print("            \______/             ")
    print("")
    print(f"A palavra secreta era {palavra_secreta}")

def carrega_palavra_secreta():


    tipo_palavra = 0
    while tipo_palavra not in [1, 2]:
        print("")
        print("******************************************************")
        print("")
        print("Escolha a palavra secreta de acordo com as seguintes opcões")
        print(" ")
        print("[ 1 ] FRUTAS")
        print("[ 2 ] PAÍSES")
        print(" ")

        tipo_palavra = int(input("Qual você escolhe? "))

        if tipo_palavra == 1:
            print("Você escolheu FRUTAS.")
            arquivo = open("frutas.txt", "r")
        elif tipo_palavra == 2:
            print("Você escolheu PAÍSES.")
            arquivo = open("paises.txt", "r")
        else:
            print("Opção inválida. Vamos começar novamente.")
            continue

        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

        sorteio = random.randrange(0, len(palavras))
        palavra_secreta = palavras[sorteio].upper()

        return palavra_secreta




if (__name__ == "__main__"):
    jogar()
