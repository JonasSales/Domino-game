from piece import piece_distributor, wagon

wagon = wagon()

class Player:
    def __init__(self, nome):
        self.nome = nome
        self.piece = []

@staticmethod
def player():
    piece_player = piece_distributor()
    player1 = Player("Jogador 1")
    player1.piece = piece_player[0]

    player2 = Player("Jogador2")
    player2.piece = piece_player[1]

    player3 = Player("Jogador3")
    player3.piece = piece_player[2]

    player4 = Player("Jogador4")
    player4.piece = piece_player[3]

    return player1.piece,player2.piece,player3.piece,player4.piece

def show_piece(piece):
    for x in piece:
        if x in wagon.values():
            print(f"[{x}] É uma carroça")
        else:
            print(f"[{x}] Não é carroça")

