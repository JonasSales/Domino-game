from jogador import jogador,mostrar_pecas
from pecas import carroca
from time import sleep
from random import randint
import os



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
    print("A quantidade de peças jogadas foi de: ",len(mesa)/2,
          "\nA quantidade de jogadas foi de:",len(mesa)/4)

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
    return verificacao,x

        
                   
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
                verificacao = verificador_primeira_jogada(jogador)[0]
                if verificacao == True:
                    primeira_jogada(jogador)
                    break
                else:
                    os.system('cls')
                    print("Como você não tinha carroças no inicio do jogo\n"
                          "Jogue na proxima rodada")
                    sleep(2)
                    break                
    else:
        while True:
            if meio_de_jogo(jogador)[0] == True:
                jogada_no_meio_do_jogo_player(jogador)
                break
            else:
                os.system('cls')
                print("Como você não tinha jogadas disponiveis\n "
                      "Jogue na proxima rodada")
                sleep(2)
                break



def bot(jogador):
    if len(mesa) == 0:
        while True:
            verificacao = verificador_primeira_jogada(jogador)[0]
            jogada = verificador_primeira_jogada(jogador)[1]
            if verificacao == True:
                primeira_jogada_bot(jogador,jogada)
                break
            else:
                os.system('cls')
                print("Como este jogador não tinha jogadas disponiveis\n "
                      "Então ele joga na proxima rodada")
                sleep(2)                
                break
    else:
        while True:
            verificacao = meio_de_jogo(jogador)[0]
            jogada_bot = meio_de_jogo(jogador)[1]
            if verificacao == True:
                jogada_no_meio_do_jogo_bot(jogador,jogada_bot)
                break
            else:
                os.system('cls')
                print("Como este jogador não tinha jogadas disponiveis\n "
                      "Então ele joga na proxima rodada")
                sleep(2)                
                break



def primeira_jogada_bot(jogador,jogada):
    mesa.append(jogada[0])
    mesa.append(jogada[-1])
    jogador.remove(jogada)



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



def vez_jogador(jogador,x):
    os.system('cls')
    print (f"É a vez do jogador {x}")
    sleep(2)
    bot(jogador)



while True:
    pecas = jogador()
    carrocoes = carroca()
    jogador1 = (pecas[0])
    jogador2 = (pecas[1])
    jogador3 = (pecas[2])
    jogador4 = (pecas[3])
    monte = (jogador3+jogador4)
    mesa = []
    vez = True

    os.system("cls")
    x = "*"
    print(f"{x*44}")
    print("|       [1] Para jogar com 4 players       |\n"
          "|       [2] Em breve                       |\n"
          "|       [0] Para sair do jogo              |")
    print(f"{x*44}")
    acao = int(input("        Deseja jogar qual em qual modo?\n"
                     "--------->"))

    if acao == 1:
        while True:
            if vez == True:
                vez_jogador(jogador1,1)
                player(jogador1)
                if len(jogador1) == 0:
                    os.system('cls')
                    print("Jogador 1 ganhou")
                    sleep(2)
                    break
                vez_jogador(jogador2,2)
                if len(jogador2) == 0:
                    os.system('cls')
                    print("Jogador 2 ganhou")
                    sleep(2)
                    break
                vez_jogador(jogador3,3)
                if len(jogador3) == 0:
                    os.system('cls')                   
                    print("Jogador 3 ganhou")
                    sleep(2)
                    break
                vez_jogador(jogador4,4)
                if jogador4 == 0:
                    os.system('cls')
                    print("Jogador 4 ganhou")
                    sleep(2)
                    break
            else:
                sleep(2)
                print("O jogo fechou, infelizmente não houve ganhador!!")
                break              
    elif acao == 2:
        os.system('cls')
        for x in range(0,10):
            print("*************Em breve*************")
        sleep(2)
    elif acao == 0:
        os.system('cls')
        break