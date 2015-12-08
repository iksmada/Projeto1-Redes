# -*- coding: UTF-8 -*-
#Servidor, responde requisicoes

import socket
import sys
import select
from time import sleep
from Pacote import Pacote

TIMEOUT = 1.1

def Servidor(args):
    if len(args) != 2:
        print 'Entrada errada. execução se da por:\n\tpython emissor.py <porta>'# <nome_arquivo>'
        sys.exit()
    #recebe a porta pela linha de comando
    port = int(args[1])
    #Nao consegui fazer o cliente pedir o arquivo, tem que entrar com o nome
    #nomeArquivo = args[2]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", port))
    pacoteEnviar = Pacote()
    pacoteRecebido = Pacote()
    janela = 3
    tripleNack= []
    print 'Esperando o cliente conectar'
    msg, addr = RecebePacote(s)
    print msg.data
    print 'Descobri o endereco do cliente: ', addr
    for i in range(janela):
        tripleNack.append(0)
    texto = LeArquivo(msg.data)
    if texto == False:
       print 'Arquivo não existe ou não tem permissão para leitura:\n\tVerifique se o arquivo existe\n\tTente mudar a permissao (chmod)'
       print 'saindo...'
       pacoteEnviar.sair = 1
       pacotes = []
       pacotes.append(pacoteEnviar)
       #sys.exit()
    else:
       pacotes = CriaPacotes(texto)
    #Descobre o endereço do cliente
    nackAntigo = 0
    nack = 0
    #Logica do rdt send
    while nackAntigo < len(pacotes):
        # Can we send a packet, do we need to send pkt
        if nack < janela and (nack + nackAntigo) < len(pacotes):
            EnviaPacote(pacotes[nackAntigo + nack], s, addr)
            print 'Enviando pacote ', pacotes[nackAntigo + nack].numeroSequencia
            nack += 1
            #pacoteRecebido, addr = RecebePacote(s)
            sleep(0.2)
        else:
            #Espera pelos acks do cliente
            ready = select.select([s], [], [], TIMEOUT)
            if ready[0]:
                pacoteRecebido, addr = RecebePacote(s)
            else: # Janela encheu
                print "Atingiu tempo limite, reenviando"
                nack = 0
            print "Número de sequencia recebido: ", pacoteRecebido.numeroSequencia,", Ack conhecido:", nackAntigo
            if pacoteRecebido.numeroSequencia == nackAntigo:
                tripleNack[nackAntigo%janela]=0
                nackAntigo += 1
                nack -= 1
            else:
                tripleNack[nackAntigo%janela]+=1
                if tripleNack[nackAntigo%janela]==3:
                    tripleNack[nackAntigo%janela]=0
                    nack = 0
    # Close server connection and exit successfully
    s.close()
    sys.exit(0)

def RecebePacote(s):
    ''' Recebe o pacote e coloca em um formato mais facil de trabalhar'''
    pacoteRecebido = Pacote()
    msg, addr = s.recvfrom(4096)
    pacoteRecebido.ToPacote(msg)
    return pacoteRecebido, addr

def VerificaPacote(pacoteRecebido, host):
    ''' Verifica se checksum e ack estao corretos '''
    if pacoteRecebido.checksum == pacoteRecebido.CalculaChecksum(pacoteRecebido.data):
        return True
    return False

def EnviaPacote(pacoteEnviar, s, addr):
    ''' coloca o pacote no formato certo e envia'''
    s.sendto(pacoteEnviar.ToString(), addr)

def LeArquivo(nome):
    ''' Le o arquivo e joga tudo em uma variavel '''
    try:
        texto = open(nome, 'r')
        return texto.read()
    except Exception:
        return False

def CriaPacotes(texto):
    ''' forma uma lista de pacotes que contem todos os pacotes que serao enviados '''
    numeroSequencia = 0
    pacotes = []
    while texto:
        pacote = Pacote()
        #Forma o pacote
        pacote.numeroSequencia = numeroSequencia
        pacote.ack = 0
        #Envia de 20 em 20 caracteres
        pacote.data = texto[:20]
        pacote.sair = 0
        pacote.checksum = pacote.CalculaChecksum(texto[:20])
        #adciona o pacote na lista de pacotes
        pacotes.append(pacote)
        texto = texto[20:]
        numeroSequencia += 1
    #Forma o pacote para sair, a unica coisa que importa aqui é sair = 1
    pacote = Pacote()
    pacote.numeroSequencia = numeroSequencia
    pacote.checksum = 0
    pacote.texto = ''
    pacote.sair = 1
    pacotes.append(pacote)

    return pacotes

if __name__ == "__main__":
    Servidor(sys.argv)
