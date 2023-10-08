from random import randint
def return_pieces():
    return ['0:0','0:1','1:1',
            '0:2','1:2','2:2',
            '0:3','1:3','2:3',
            '3:3','0:4','1:4',
            '2:4','3:4','4:4',
            '0:5','1:5','2:5',
            '3:5','4:5','5:5',
            '0:6','1:6','2:6',
            '3:6','4:6','5:6',
            '6:6']

def wagon():
    return {0:'0:0',1:'1:1',2:'2:2',3:'3:3',4:'4:4',5:'5:5',6:'6:6'}

def piece_distributor():
    pieces_players = [[] for _ in range(4)]
    pieces_reservation = return_pieces()
    for _ in range(7):
        for jogador in range(4):
            randon_piece =pieces_reservation.pop(randint(0,len(pieces_reservation)-1))
            pieces_players[jogador].append(randon_piece)
#            reserva_de_pecas.remove(peca_aleatoria)
    return pieces_players

