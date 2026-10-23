import random

fichas = 500
simbolos = ["🚀",
            "🦆","🦆",
            "🍒","🍒","🍒",
            "🐍","🐍","🐍"]
pontuacao = {
    "🚀":100,
    "🦆":10,
    "🍒":5,
    "🐍":1.5
}

def receber_aposta():
    while True:
        aposta = input("Digite o número de fichas que irá apostar: ")

        if not aposta.isdigit():
            print("O valor deve ser númérico")
        elif not 0 < int(aposta) <= fichas:
            print("O valor deve ser um número de fichas válido")
        else:
            return aposta

def gerar_fitas():
    fitas = []
    for _ in range(1, 4):
        fitas.append(random.sample(simbolos, len(simbolos)))
    return fitas

def puxar_alavanca(fitas):
    resultado = set()
    posicao = random.randint(0, len(simbolos) - 1)

    for linha in range(0, len(fitas)):
        if linha == 1:
            print(">| ", end="")
        else:
            print(" | ", end="")
        for coluna in range(0, len(fitas)):
            print(fitas[coluna][posicao], end=" | ")
            if linha == 1:
                resultado.add(fitas[coluna][posicao])

            if posicao == len(simbolos) - 1:
                posicao = 0
            else:
                posicao += 1
        print()

    return resultado

def jogar():
    global fichas
    fitas = gerar_fitas()

    while True:
        print("--- MÁQUINA CAÇA-NÍQUEL ---")
        print(f"Fichas: {fichas:.0f}")
        aposta = int(receber_aposta())
        resultado = puxar_alavanca(fitas)

        if len(resultado) > 1:
            fichas -= aposta
            if fichas == 0:
                print("Que pena... você não tem mais fichas...")
                break
            else:
                print("Você perdeu!")
        else:
            print("Você ganhou!")
            simbolo = next(iter(resultado))
            fichas += pontuacao.get(simbolo) * aposta

        continuar = input("Quer continuar jogando? (y/n): ").lower()
        match continuar:
            case "y":
                continue
            case "n":
                print("Azar seu!!")
                break
            case _:
                print("Vou entender isso como um sim!")

jogar()