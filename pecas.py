from random import sample
def retorno_pecas():
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

def carroca():
    return {0:'0:0',1:'1:1',2:'2:2',3:'3:3',4:'4:4',5:'5:5',6:'6:6'}

def distribuidor_de_pecas():
    pecas_jogadores = [[] for _ in range(4)]
    reserva_de_pecas = retorno_pecas()
    for _ in range(7):
        for jogador in range(2):
            peca_aleatoria = sample(reserva_de_pecas, 1)[0]
            pecas_jogadores[jogador].append(peca_aleatoria)
            reserva_de_pecas.remove(peca_aleatoria)
    ordem_aleatoria = sample(reserva_de_pecas,len(reserva_de_pecas))
    return pecas_jogadores,ordem_aleatoria
