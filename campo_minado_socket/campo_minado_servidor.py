import os,socket,json
from ast import literal_eval
from datetime import datetime
from campo_minado_negocio import CampoMinado

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = '127.0.0.1'     	       # Endereco IP do Servidor

def server():
    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)																
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    
    cm = CampoMinado()
    tradutor = []

    while True:
        #recebi dados
        resposta = []
        data, address = sock.recvfrom(MAX_BYTES) # Recebi dados do socket
        text = data.decode(ENCODE)               # Convertendo dados de BASE64 para UTF-8
        tradutor.append(text.split(";"))
        count = len(tradutor)
        for x in tradutor[count-1]:
            resposta.append(x)
        #print(resposta)
        #--------------------------------------------------#
        # REALIZAR TRATAMENTO DO QUE FOI ENVIADO -- IMPLEMENTAR
        #--------------------------------------------------# 
        text = gerenciamento(cm,resposta)
        
        
        #Envia resposta
        data = text.encode(ENCODE) # Codifica para BASE64 os dados 
        sock.sendto(data, address) # Enviando dados	

def gerenciamento(cm,resposta):
    
    opcao = {
        "1": novoJogo,
        "2": carregarJogo,
        "3": jogar,
        "4": tabuleiro,
        "5": jogada
    }
    func = opcao.get(resposta[0])
    return func(cm,resposta)

def tabuleiro(cm,resposta):
    tabuleiro = str(cm.tabuleiro)
    return tabuleiro

def jogada(cm,resposta):
    jogada = cm.jogadas
    return str(jogada)

def novoJogo(cm,resposta):
    linhaColuna = int(resposta[1])
    cm.novoJogo(linhaColuna,linhaColuna)
    cm.salvarJogo()
    print("\n\n")
    #print(cm.localizacaoBombas)
    return str(cm.jogadas)

def carregarJogo(cm,resposta):
    
    arquivo_campoMinado_json = open('campoMinado.json','r')
    dados = json.load(arquivo_campoMinado_json)
    cm.carregaDados(dados)
    arquivo_campoMinado_json.close()
    print("\n\n")
    print(cm.localizacaoBombas)
    return str(cm.jogadas)

def jogar(cm,valor):
    linha = int(valor[1])
    coluna = int(valor[2])
    return str(cm.jogar(linha,coluna))


if __name__ == "__main__":
    server()