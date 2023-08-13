from pecas import distribuidor_de_pecas, carroca

carrocoes = carroca()

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pecas = []

@staticmethod
def jogador():
    pecas_jogadores = distribuidor_de_pecas()
    jogador1 = Jogador("Jogador 1")
    jogador1.pecas = pecas_jogadores[0]

    jogador2 = Jogador("Jogador2")
    jogador2.pecas = pecas_jogadores[1]

    jogador3 = Jogador("Jogador3")
    jogador3.pecas = pecas_jogadores[2]

    jogador4 = Jogador("Jogador4")
    jogador4.pecas = pecas_jogadores[3]

    return jogador1.pecas,jogador2.pecas,jogador3.pecas,jogador4.pecas

def mostrar_pecas(pecas):
    for x in pecas:
        if x in carrocoes.values():
            print(f"[{x}] É uma carroça")
        else:
            print(f"[{x}] Não é carroça")

