from socket import socket, AF_INET, SOCK_DGRAM
from pygame import mixer
from ast import literal_eval
import json
import sys
import os
import zmq


class CampoMinadoView:

    ENCODE = "UTF-8"

    PORT = "5559"

    def __init__(self):
            self.contexto = zmq.Context()
            self.socket = self.contexto.socket(zmq.REQ)
            self.socket.connect("tcp://localhost:%s" % self.PORT)

    def menu(self):
        print(" ___________________________________________ ")
        print("|                                           |")
        print("|           ###################             |")
        print("|           #   CAMPO MINADO  #             |")
        print("|           ###################             |")
        print("|                                           |")
        print("|                                           |")
        print("|           1) Iniciar Novo Jogo            |")
        print("|                                           |")
        # if os.path.isfile("campoMinado.json"):
        #     print("|           2) Continuar Jogo               |")
        #     print("|                                           |")
        print("|           3) Sair                         |")
        print("|                                           |")
        print("|                                           |")
        print("|           ###################             |")
        print("|           #   CAMPO MINADO  #             |")
        print("|           ###################             |")
        print("|___________________________________________|")

    def pegaValores(self):
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

    def fimDeJogo(self):
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

    def vitoria(self):
        os.system("cls")
        print("#############################################")
        print("#                                           #")
        print("#             PARABÉNS VOCÊ VENCEU!         #")
        print("#               JOGUE NOVAMENTE             #")
        print("#                                           #")
        print("#############################################")
        print("\n\n\n")
        text = "IT"
        requisicao(text)
        escolha = str(input("\n\nDeseja jogar novamente(S/N)? "))
        if(escolha != "s" and escolha != "S"):
            if(escolha != "n" and escolha != "N"):
                input("\n\nDigite S OU N! ... Pressione Enter para continuar: ")
            else:
                os.system("cls")
                sys.exit(0)
        return 

    # def carregarJogo(self):
    #         arquivo_campoMinado_json = open('campoMinado.json','r')
    #         dados = json.load(arquivo_campoMinado_json)
    #         linha = dados['linha']
    #         coluna = dados['coluna']
    #         jogadas = dados['jogadas']
    #         tabuleiro = dados['tabuleiro']
    #         bombas = []
    #         for x in dados['bombas']:
    #             bombas.append(tuple(x))
    #         localizacaoBombas = bombas
    #         text = "Carregar"+"."+str(linha)+"."+str(coluna)+"."+str(jogadas)+"."+str(tabuleiro)+"."+str(localizacaoBombas)
    #         self.requisicao(text)
    #         arquivo_campoMinado_json.close() 
    #         self.iniciaJogo()

    def iniciaJogo(self):
        text = "JR"
        jogadas_restantes = self.requisicao(text)
        if jogadas_restantes == "True":
            os.system("cls")
            #print(cm.localizacaoBombas)
            text = "IT"
            self.requisicao(text)
            try:
                linha = int(input("\nPosição da linha :"))
            except:
                input("\nOpção inválida! Pressione ENTER")
                self.iniciaJogo()
            try:
                coluna = int(input("\nPosição da coluna :"))
            except:
                input("\nOpção inválida! Pressione ENTER")
                self.iniciaJogo()
            text = "JG" + "." + str(linha) + "." + str(coluna)
            teste = int(self.requisicao(text))
            if teste == -1:
                self.fimDeJogo()
            elif teste == 0:
                input("\n\nCoordenadas inválidas! Insira valores aceitáveis ... Pressione Enter para continuar: ")
                self.iniciaJogo()
            elif teste == 2:
                self.vitoria()
            else:
                self.iniciaJogo()
                
    def requisicao(self,text):
            dados = text.encode(self.ENCODE)
            self.socket.send(dados)
            dados = self.socket.recv()
            return dados.decode(self.ENCODE)

if __name__ == "__main__":
    cm = CampoMinadoView()
    testa = True
    while testa:
        os.system("cls")
        cm.menu()
        opcao = int(input("\n\nDigite a opção desejada: "))
        if opcao == 1:
            linhaColuna = cm.pegaValores()
            text = "CJ" + "." + str(linhaColuna)
            cm.requisicao(text)
            cm.iniciaJogo()
        # elif opcao == 2:
        #     cm.carregarJogo()
        elif opcao == 3:
            input("\nFinalizando jogo ... Pressione Enter para continuar")
            os.system("cls")
            sys.exit(0)
        else:
            print("\nOpção inválida! Selecione uma das opções disponíveis")
            input("\nPressione ENTER para continuar")
            os.system("cls")
        
