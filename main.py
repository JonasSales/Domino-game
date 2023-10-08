from player import player,show_piece
from piece import wagon
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
    show_piece(player)



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
    for x in player:
        if x in carrocoes.values():
            return True,x
    return False,x

        
                   
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



def move_check(player):
    for x in player:
        if x[0] in table[0]:
            return True,x
        elif x[0] in table[-1]:
            return True,x
        if x[-1] in table[0]:
            return True,x
        elif x[-1] in table[-1]:
            return True,x
    return False,x



def player(player):
    show_table(table,player)
    if len(table) == 0:
            while True:
                verification = first_move_check(player)[0]
                if verification == True:
                    first_play(player)
                    break
                else:
                    if len(mount) > 0:
                        sleep(2)
                        pull_piece(player)
                        break
                    play_unavailable()
                    break                
    else:
        while True:
            if move_check(player)[0] == True:
                middlegame(player)
                break
            else:
                if len(mount) > 0:
                    pull_piece(player)
                    break
                play_unavailable()
                break



def play_unavailable():
    os.system('cls')
    print("Como este jogador não tinha jogadas disponiveis\n "
            "Então ele joga na proxima rodada") 



def bot(player):
    if len(table) == 0:
        while True:
            verification = first_move_check(player)[0]
            play = first_move_check(player)[1]
            if verification == True:
                first_play_bot(player,play)
                break
            else:
                if len(mount) > 0:
                    pull_piece(player)
                    break
                play_unavailable()                
                break
    else:
        while True:
            verification = move_check(player)[0]
            bot_play = move_check(player)[1]
            if verification == True:
                middlegame_bot(player,bot_play)
                break
            else:
                if len(mount) > 0:
                    pull_piece(player)
                    break
                play_unavailable()                
                break



def first_play_bot(player,play):
    table.append(play[0])
    table.append(play[-1])
    player.remove(play)



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



def turn_player(player,x):
    os.system('cls')
    print (f"É a vez do jogador {x}")
    sleep(2)
    bot(player)



def win_player(x):
    os.system('cls')
    print(f"Jogador {x} ganhou")
    sleep(2)



def checking_movements_on_the_table(j1,j2,j3,j4,mesa):
    players = j1+j2+j3+j4
    while True:
        for x in players:
            if (x[0] or x[-1]) in mesa:
                return True           
        return False

while True:
    parts = player()
    carrocoes = wagon()
    player_1 = (parts[0])
    player_2 = (parts[1])
    player_3 = (parts[2])
    player_4 = (parts[3])
    mount = (player_3+player_4)
    table = []

    os.system("cls")
    print(f"{'*'*44}")
    print("|       [1] Modo com 4 players       |\n"
          "|       [2] Modo com 2 players             |\n"
          "|       [3] Para sair do jogo              |")
    print(f"{'*'*44}")
    action = int(input("        Deseja jogar qual em qual modo?\n"
                     "--------->"))

    if action == 1:
        mount = []
        while True:          
            if len(player_1) == 0:
                win_player(1)
                break
            elif len(player_2) == 0:
                win_player(2)
                break
            elif len(player_3) == 0:
                win_player(3)
                break 
            elif len(player_4) == 0:
                win_player(4)
                break
            player(player_1)
            turn_player(player_2,2)
            turn_player(player_3,3)
            turn_player(player_4,4)
            if checking_movements_on_the_table(player_1,player_2,player_3,player_4,table) == False:
                os.system('cls')
                sleep(2)
                print("Infelizmente não havia mais nenhuma jogada possível\n"
                      "e se foi obrigado fechar o jogo.")
                break
    elif action == 2:
        while True:
            if len(player_1) == 0:
                win_player(1)
                break
            elif len(player_2) == 0:
                win_player(2)
                break
            player(player_1)
            turn_player(player_2,2)
            if checking_movements_on_the_table(player_1,player_2,"","",table) == False:
                os.system('cls')
                sleep(2)
                print("Infelizmente não havia mais nenhuma jogada possível\n"
                      "e se foi obrigado fechar o jogo.")
                break    
    elif action == 3:
        os.system('cls')
        break