#Cliente, faz requisições

import socket
import sys
from time import sleep
from random import randint

def Cliente(args):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #recebe ip, porta e nome do arquivo pela linha de comando
    host = args[1]
    port = args[2]
    arq_name = args[3]
    pacote = []
    '''
    pacote[0]   : Numero de sequencia (Aleatorio) 4 bytes
    pacote[1]   : ACK = 1+numero_seq_recebido     4 bytes
    pacote[2] : Checksum                          2 bytes
    pacote[3] : ACK, SYN, FIN                     3 bytes
    pacote[4] : tamanho                           2 bytes
    pocate[5]   : Data                            20 bytes

    total bytes:                                  35 bytes
    '''
    #Envia um ack e espera o servidor responder com ack, se não responder o
    #Gera numero sequencia aleatorio de 4 bytes
    pacote.append(randint(0,9999)) #numero de sequencia
    pacote.append("0000")
    pacote.append("00")
    pacote.append("010")
    pacote.append("00")
    pacote.append(None)


    while 1:
        s.sendto(pacote, (host, port))
    #cliente fica enviando ack de 1 em 1 segundo
    while(reply != "FIN"):
        msg = RecebePacote(s.recvfrom(33))
        envioCorreto = VerificaPacote(msg)
        EnviaPacote(msg, s, host, port)

    #Cliente aceita encerrar e acaba a comunicacao
    s.sendto("FIN", (host, port))
    s.close()

def RecebePacote(msg):
    ''' Recebe o pacote e coloca em um formato mais facil de trabalhar'''
    data, addr = msg
    msgLista = []
    msgLista.append(data[0:4])
    msgLista.append(data[5:9])
    msgLista.append(data[10:15])
    msgLista.append(data[15:18])
    msgLista.append(data[18:])
    return msgLista, addr

def VerificaPacote(msg, host):
    ''' Verifica se checksum e ack estão corretos '''


def EnviaPacote(msg, s, host, port):
    ''' coloca o pacote no formato certo, como aqui o receptor so recebe um arquivo enviara apenas acks e fin '''
    msgString = ''
    for i in msg: msgString += i
    s.sendto(msgString, (host, port))

if __name__ == '__main__':
    Cliente(sys.argv)
