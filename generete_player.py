from piece_generator import piece_distributor, wagon

wagon = wagon()

class Player:
    def __init__(self, name,piece=[]):
        self.name = name
        self.piece = piece


    def player():
        piece_player = piece_distributor()
        player1 = Player("Jogador 1",piece_player[0])

        player2 = Player("Jogador 2",piece_player[1])

        player3 = Player("Jogador 3",piece_player[2])

        player4 = Player("Jogador 4",piece_player[3])

        return player1,player2,player3,player4,piece_player

def show_piece(piece):
    for x in piece:
        if x in wagon.values():
            print(f"[{x}] É uma carroça")
        else:
            print(f"[{x}] Não é carroça")
