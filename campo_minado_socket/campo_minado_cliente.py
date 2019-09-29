import socket,os,sys,math
from ast import literal_eval
from campo_minado_view import iniciaJogo,pegaValores,menu,fimDeJogo,vitoria
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos

def client(text):
    """ Procedimento responsavel por enviar dados para o servidor e receber alguma resposta por conta disso """ 
    data = text.encode(ENCODE)				    # Codifica para BASE64 os dados de entrada	
    
    #Enviando de dados
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Inicializar um socket UDP
    dest = (HOST, PORT)                                     # Define IP de origem e Porta de destino  
    sock.sendto(data, dest)                                 # Envia os dados para o destino

    #Resposta de envio ao servidor
    #print(sock.getsockname())				    # Imprime dados do socker de destino
    data, address = sock.recvfrom(MAX_BYTES)    # Recebendo dados
    text = data.decode(ENCODE)                  # Convertendo dados de BASE64 para UTF-8

    #Fechando Socket
    sock.close()
    #print(text)
    return text


def jogada():
    text = str("5")
    resposta = client(text)
    return int(resposta)


def imprimeTabuleiro():
    text = str("4")
    resposta = literal_eval(client(text))
    for posicao in resposta:
        print (str(posicao))

def gerenciamento():
    while jogada() > 0:
        os.system("cls")
        imprimeTabuleiro()
        valor = ("3;")
        valor += iniciaJogo()
        teste = int(client(valor))
        if teste == -1:
            fimDeJogo()
        elif teste == 0:
            input("\n\nCoordenadas inválidas! Insira valores aceitáveis ... Pressione Enter para continuar: ")
            gerenciamento()
        elif teste == 2:
            os.system("cls")
            imprimeTabuleiro()
            vitoria()
        else:
            gerenciamento()
def inicio():
    testa = True
    #escolha = []
    while testa:
        os.system("cls")
        menu()
        opcao = int(input("\n\nDigite a opção desejada: "))
        if opcao == 1:
            linhaColuna = pegaValores()
            escolha = str(opcao)+";"+str(linhaColuna)
            qtdJogadas = int(client(escolha))
            gerenciamento()
        elif opcao == 2:
            escolha = str(opcao)
            qtdJogadas = int(client(escolha))
            gerenciamento()
        elif opcao == 3:
            input("\nFinalizando jogo ... Pressione Enter para continuar")
            os.system("cls")
            sys.exit(0)
        else:
            print("\nOpção inválida! Selecione uma das opções disponíveis")
            input("\nPressione ENTER para continuar")
            os.system("cls")

  
    
if __name__ == "__main__":
    inicio()