from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from campo_minado_negocio import CampoMinado
from os.path import isfile
import json
import sys

cm = CampoMinado()

def novoJogo(linhas,colunas):
    cm.novoJogo(linhas, colunas)

def jogar(linha, coluna):
    return cm.jogar(linha, coluna)

def carregaDados(dados):
    return cm.carregaDados(dados)

def salvarJogo():
    return cm.salvarJogo()

def verificaJogada():
    return cm.verificaJogada()

def imprimeTabulerio():
    return cm.imprimeTabulerio()

if __name__ == "__main__":
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(novoJogo)
    serverRPC.register_function(jogar)
    serverRPC.register_function(carregaDados)
    serverRPC.register_function(salvarJogo)
    serverRPC.register_function(verificaJogada)
    serverRPC.register_function(imprimeTabulerio)
    print("Starting server")
    serverRPC.serve_forever()