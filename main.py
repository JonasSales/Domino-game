from jogador import jogador,mostrar_pecas
from pecas import carroca
from time import sleep
from random import randint
import os



pecas = jogador()
carrocoes = carroca()
jogador1 = (pecas[0])
jogador2 = (pecas[1])
monte = (pecas[2])
mesa = []
vez = 0



def jogada(jogador,peca_escolhida):
    p1 = (jogador[peca_escolhida-1][0])
    p2 = (jogador[peca_escolhida-1][-1])
    if p1 == mesa[0]:
        mesa.insert(0,p1)
        mesa.insert(0,p2)
        jogador.pop(peca_escolhida-1)
    elif p2 == mesa[0]:
        mesa.insert(0,p2)
        mesa.insert(0,p1)
        jogador.pop(peca_escolhida-1)
    elif p1 == mesa[-1]:
        mesa.insert(len(mesa),p1)
        mesa.insert(len(mesa),p2)
        jogador.pop(peca_escolhida-1)
    elif p2 == mesa[-1]:
        mesa.insert(len(mesa),p2)
        mesa.insert(len(mesa),p1)
        jogador.pop(peca_escolhida-1)
    else:
        os.system("cls")
        print("Jogada invalida")
        sleep(2)



def puxar_peca(jogador):
    peca_aleatoria = monte.pop(randint(0,(len(monte))-1))
    jogador.append(peca_aleatoria)



def clear_screen_delay():
    os.system('cls')
    print("Movimento inválido.")
    sleep(2)



def mostrar_mesa(mesa,jogador):
    os.system("cls")
    print(mesa)
    mostrar_pecas(jogador)



def primeira_jogada(jogador):
    while True:
        try:    
            mostrar_mesa(mesa,jogador)
            peca_escolhida = int(input("Digite uma peça para jogar:"))
            if jogador[peca_escolhida-1] in carrocoes.values():
                mesa.append(jogador[peca_escolhida-1][0])
                mesa.append(jogador[peca_escolhida-1][-1])
                jogador.pop(peca_escolhida-1)
                break
            else:
                clear_screen_delay()
        except:
            os.system("cls")
            print("Jogada invalida")
            sleep(2)


def verificador_primeira_jogada(jogador):
    for x in jogador:
        if x in carrocoes.values():
            verificacao = True
            break
        else:
            verificacao = False
    return verificacao

        
                   
def jogada_no_meio_do_jogo_player(jogador):
    while True:
        try:    
            mostrar_mesa(mesa,jogador)
            peca_escolhida = int(input("Digite uma peça para jogar:"))
            peca_jogador = jogador[peca_escolhida-1]
            verificacao = verificar_mesa(mesa,peca_jogador)
            if verificacao == True:
                jogada(jogador,peca_escolhida)
                break
            else:
                os.system("cls")
                print("Jogada invalida")
                sleep(2)
        except:
                os.system("cls")
                print("Jogada invalida")
                sleep(2)            


def verificar_mesa(mesa,peca_escolhida):
    p1 = peca_escolhida[0]
    p2 = peca_escolhida[-1]
    if p1 in mesa[0]:
        retorno = True
    elif p2 in mesa [0]:
        retorno = True
    elif p1 in mesa[-1]:
        retorno = True
    elif p2 in mesa[-1]:
        retorno = True
    else:
        retorno = False
    return retorno



def meio_de_jogo(jogador):
    for x in jogador:
        if x[0] in mesa[0]:
            verificar = True
            break
        elif x[0] in mesa[-1]:
            verificar = True
            break
        if x[-1] in mesa[0]:
            verificar = True
            break
        elif x[-1] in mesa[-1]:
            verificar = True
            break        
        else:
            verificar = False
    return verificar,x



def player(jogador):
    mostrar_mesa(mesa,jogador)
    if len(mesa) == 0:
            while True:
                if verificador_primeira_jogada(jogador) == True:
                    primeira_jogada(jogador)
                    break
                else:
                    os.system('cls')
                    print("Como você não tinha carroças no inicio do jogo\n"
                        "fomos obrigados a puxar uma peça em seu jogo.\n"
                        "Jogue na proxima rodada")
                    sleep(2)
                    puxar_peca(jogador)
                    break                
    else:
        while True:
            if meio_de_jogo(jogador)[0] == True:
                jogada_no_meio_do_jogo_player(jogador)
                break
            else:
                os.system('cls')
                print("Como você não tinha jogadas disponiveis\n "
                    "fomos obrigados a puxar uma peça em seu jogo.\n"
                    "Jogue na proxima rodada")
                sleep(2)
                puxar_peca(jogador)
                break

def bot(jogador):
    if len(mesa) == 0:
        while True:
            if verificador_primeira_jogada(jogador) == True:
                primeira_jogada_bot(jogador)
                break
            else:
                puxar_peca(jogador)
                break
    else:
        while True:
            verificacao = meio_de_jogo(jogador)[0]
            jogada_bot = meio_de_jogo(jogador)[1]
            if verificacao == True:
                jogada_no_meio_do_jogo_bot(jogador,jogada_bot)
                break
            else:
                puxar_peca(jogador)
                break



def primeira_jogada_bot(jogador,jogada):
    for x in jogador:
        if jogada in carrocoes.values():
            remover_peca = len((x))
            mesa.append(jogador[jogada][0])
            mesa.append(jogador[jogada][-1])
            jogador.pop(remover_peca)



def jogada_no_meio_do_jogo_bot(jogador,jogada):
    for x in jogador:
        if jogada == x:
            break
    p1 = jogada[0]
    p2 = jogada[-1]
    if p1 in mesa[0]:
        mesa.insert(0,p1)
        mesa.insert(0,p2)
        jogador.remove(x)
    elif p2 in mesa[0]:
        mesa.insert(0,p2)
        mesa.insert(0,p1)
        jogador.remove(x)
    elif p1 in mesa[-1]:
        mesa.insert(len(mesa),p1)
        mesa.insert(len(mesa),p2)
        jogador.remove(x)
    elif p2 in mesa[-1]:
        mesa.insert(len(mesa),p2)
        mesa.insert(len(mesa),p1)
        jogador.remove(x)



while True:
    if vez == 0:
        os.system('cls')
        print ("É a vez do jogador 1")
        sleep(2)            
        player(jogador1)
        vez +=1
        if len(jogador1) == 0:
            os.system('cls')
            print("Jogador1 ganhou")
            break
    #Vez do jogador 2
    elif vez == 1:
        os.system('cls')
        print ("É a vez do jogador 2")
        sleep(2)
        bot(jogador2)
        vez -=1
        if jogador2 == 0:
            os.system('cls')
            print("Jogador 2 ganhou")
            break 

