from pygame import mixer
import json
import sys
import os


def menu():
    print(" ___________________________________________ ")
    print("|                                           |")
    print("|           ###################             |")
    print("|           #   CAMPO MINADO  #             |")
    print("|           ###################             |")
    print("|                                           |")
    print("|                                           |")
    print("|           1) Iniciar Novo Jogo            |")
    print("|                                           |")
    if os.path.isfile("campoMinado.json"):
        print("|           2) Continuar Jogo               |")
        print("|                                           |")
    print("|           3) Sair                         |")
    print("|                                           |")
    print("|                                           |")
    print("|           ###################             |")
    print("|           #   CAMPO MINADO  #             |")
    print("|           ###################             |")
    print("|___________________________________________|")

def pegaValores():
    os.system("cls")
    print("#############################################")
    print("#                                           #")
    print("#  O TABULEIRO DO CAMPO MINADO SERÁ DE NxN  #")
    print("#       (3,3) (4,4) (5,5) (6,6) (7,7)       #")
    print("#                                           #")
    print("#############################################")
    linhaColuna  = int(input("\n\nDigite o número de linhas e colunas do seu tabuleiro: "))
    input("\n\nCarregando jogo ... Pressione Enter para continuar: ")
    os.system("cls")
    return linhaColuna

def fimDeJogo():
    os.system("cls")
    mixer.init()
    mixer.music.load('bomb.mp3')
    mixer.music.play()
    print("#############################################")
    print("#                                           #")
    print("#             BOOOOOOOM EXPLODIU!           #")
    print("#               TENTE NOVAMENTE             #")
    print("#                                           #")
    print("#############################################")
    escolha = str(input("\n\nDeseja jogar novamente(S/N)? "))
    if(escolha != "s" and escolha != "S"):
        if(escolha != "n" and escolha != "N"):
            input("\n\nDigite S OU N! ... Pressione Enter para continuar: ")
        else:
            os.system("cls")
            sys.exit(0)
    return 

def vitoria():
    print("#############################################")
    print("#                                           #")
    print("#             PARABÉNS VOCÊ VENCEU!         #")
    print("#               JOGUE NOVAMENTE             #")
    print("#                                           #")
    print("#############################################")
    print("\n\n\n")
    escolha = str(input("\n\nDeseja jogar novamente(S/N)? "))
    if(escolha != "s" and escolha != "S"):
        if(escolha != "n" and escolha != "N"):
            input("\n\nDigite S OU N! ... Pressione Enter para continuar: ")
        else:
            os.system("cls")
            sys.exit(0)
    return 

def iniciaJogo():
        try:
            linha = int(input("\nPosição da linha :"))
        except:
            input("\nOpção inválida! Pressione ENTER")
            iniciaJogo()
        try:
            coluna = int(input("\nPosição da coluna :"))
        except:
            input("\nOpção inválida! Pressione ENTER")
            iniciaJogo()
        valor = str(linha)+";"+str(coluna)
        return valor
