import generete_player
from piece_generator import wagon
from time import sleep
from random import randint
import os



def play(player,chosen_piece):
    p1 = (player[chosen_piece-1][0])
    p2 = (player[chosen_piece-1][-1])
    if p1 == table[0]:
        table.insert(0,p1)
        table.insert(0,p2)
        player.pop(chosen_piece-1)
    elif p2 == table[0]:
        table.insert(0,p2)
        table.insert(0,p1)
        player.pop(chosen_piece-1)
    elif p1 == table[-1]:
        table.insert(len(table),p1)
        table.insert(len(table),p2)
        player.pop(chosen_piece-1)
    elif p2 == table[-1]:
        table.insert(len(table),p2)
        table.insert(len(table),p1)
        player.pop(chosen_piece-1)
    else:
        clear_screen_delay()


def pull_piece(player):
    os.system("cls")
    print("Como este jogador não tinha peças para jogar"
    "\npuxamos uma para a sua mão.")
    sleep(2)
    random_piece = mount.pop(randint(0,(len(mount))-1))
    player.append(random_piece)



def clear_screen_delay():
    os.system('cls')
    print("Movimento inválido.")
    sleep(2)



def show_table(table,player):
    os.system("cls")
    print(table)
    generete_player.show_piece(player)



def first_play(player):
    while True:
        try:    
            show_table(table,player)
            chosen_piece = int(input("Digite uma peça para jogar:"))
            if player[chosen_piece-1] in carrocoes.values():
                table.append(player[chosen_piece-1][0])
                table.append(player[chosen_piece-1][-1])
                player.pop(chosen_piece-1)
                break
            else:
                clear_screen_delay()
        except:
            clear_screen_delay()



def first_move_check(player):
    for piece in player:
        if piece in carrocoes.values():
            return True,piece
    return False,piece

        
                   
def middlegame(player):
    while True:
        try:    
            show_table(table,player)
            chosen_piece = int(input("Digite uma peça para jogar:"))
            player_piece = player[chosen_piece-1]
            if check_table(table,player_piece) == True:
                play(player,chosen_piece)
                break
            else:
                clear_screen_delay()
        except:
            clear_screen_delay()            



def check_table(table,player_piece):
    p1 = player_piece[0]
    p2 = player_piece[-1]
    if p1 in table[0]:
        return True
    elif p2 in table [0]:
        return True
    elif p1 in table[-1]:
        return True
    elif p2 in table[-1]:
        return True
    return False



def move_check(player_piece):
    for piece in player_piece:
        if piece[0] in table[0]:
            return True,piece
        elif piece[0] in table[-1]:
            return True,piece
        if piece[-1] in table[0]:
            return True,piece
        elif piece[-1] in table[-1]:
            return True,piece
    return False,piece



def play_player(player_piece,player_name):
    if len(table) == 0:
        while True:
            if first_move_check(player_piece)[0] == True:
                if player_name == "Jogador 1":
                    show_table(table,player_piece)
                    first_play(player_piece)
                    break
                else:
                    first_play_bot(player_piece,first_move_check(player_piece)[1])
                    break
            else:
                if len(mount) > 0:
                    sleep(2)
                    pull_piece(player_piece)
                    break
                play_unavailable()
                break                
    else:
        while True:
            if move_check(player_piece)[0] == True:
                if player_name == "Jogador 1":
                    middlegame(player_piece)
                    break
                else:
                    middlegame_bot(player_piece,move_check(player_piece)[1])
                    break  
            else:
                if len(mount) > 0:
                    pull_piece(player_piece)
                    break
                play_unavailable()
                break



def play_unavailable():
    os.system('cls')
    print("Como este jogador não tinha jogadas disponiveis\n "
            "Então ele joga na proxima rodada")
    sleep(2) 



def first_play_bot(player_piece,piece):
    table.append(piece[0])
    table.append(piece[-1])
    player_piece.remove(piece)



def middlegame_bot(player,play):
    for x in player:
        if play == x:
            break
    p1 = play[0]
    p2 = play[-1]
    if p1 in table[0]:
        table.insert(0,p1)
        table.insert(0,p2)
        player.remove(x)
    elif p2 in table[0]:
        table.insert(0,p2)
        table.insert(0,p1)
        player.remove(x)
    elif p1 in table[-1]:
        table.insert(len(table),p1)
        table.insert(len(table),p2)
        player.remove(x)
    elif p2 in table[-1]:
        table.insert(len(table),p2)
        table.insert(len(table),p1)
        player.remove(x)



def turn_player(player_piece,player_name):
    if player_name == 'Jogador 1':
        os.system('cls')
        print (f"É a vez do {player_name}")
        sleep(2)
        play_player(player_piece,player_name)
    #Jogada dos bots
    else:
        os.system('cls')
        print (f"É a vez do {player_name}")
        sleep(2)
        play_player(player_piece,player_name)



def win_player(player_piece,player_name):
    if len(player_piece) == 0:
        os.system('cls')
        print(f"O {player_name} ganhou")
        sleep(2)
        return True



def checking_movements_on_the_table(player,table):
    for x in player:
        if (x[0] or x[-1]) in table:
            return True



while True:
    win = False
    carrocoes = wagon()
    player = generete_player.Player.player()
    mount = (player[2].piece+player[3].piece)
    table = []
    os.system("cls")
    print(f"{'*'*44}")
    print("|       [1] Modo com 4 players             |\n"
          "|       [2] Modo com 2 players             |\n"
          "|       [3] Para sair do jogo              |")
    print(f"{'*'*44}")
    action = int(input("        Deseja jogar qual em qual modo?\n"
                     "--------->"))

    if action == 1:
        mount = []
        while win == False:
            for x in range(4):
                turn_player(player[x].piece,player[x].name)
                if win_player(player[x].piece,player[x].name) == True:
                    win = True
                    break
            piece_players = (player[0].piece+
                            player[1].piece+
                            player[2].piece+
                            player[3].piece)
            if checking_movements_on_the_table(piece_players,
                                               table) == True:
                ...
            else:
                os.system('cls')
                print("Como não havia jogadas disponiveis entre os jogadores\n"
                  "se foi obrigado fechar o jogo.")
                sleep(2)
                win = True
                break         
                


    elif action == 2:
        while win == False: 
            for x in range(2):
                turn_player(player[x].piece,player[x].name)
                if win_player(player[x].piece,player[x].name) == True:
                    win = True
                    break
            piece_players = (player[0].piece+
                            player[1].piece)
            if checking_movements_on_the_table(piece_players,
                                               table) == True:
                ...
            else:
                os.system('cls')
                print("Como não havia jogadas disponiveis entre os jogadores\n"
                  "se foi obrigado fechar o jogo.")
                sleep(2)
                win = True
                break    
    elif action == 3:
        os.system('cls')
        break