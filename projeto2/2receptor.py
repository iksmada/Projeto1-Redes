#Cliente, faz requisições

import socket
import sys
from time import sleep
from Pacote import Pacote

def Cliente(args):
    pacoteEnviar = Pacote()
    pacoteRecebido = Pacote()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #recebe ip, porta e nome do arquivo pela linha de comando
    host = args[1]
    port = args[2]
    arq_name = args[3]

    #cliente fica enviando ack de 1 em 1 segundo
    while(True):
        pacoteRecebido = RecebePacote(s.recvfrom(33))
        envioCorreto = VerificaPacote(pacoteRecebido)
        if envioCorreto:
            pacoteCorreto.ack 
            #muda os parametros do pacote pra pedir o proximo
        else:
            pass
            #pede pra reenviar

        EnviaPacote(PacoteEnviar, s, host, port)

    #Cliente aceita encerrar e acaba a comunicacao
    s.close()

def RecebePacote(pacoteRecebido):
    ''' Recebe o pacote e coloca em um formato mais facil de trabalhar'''
    msg, addr = s.recvfrom(33)
    pacoteRecebido.ToPacote(msg)
    return pacoteRecebido, addr

def VerificaPacote(pacoteRecebido, host):
    ''' Verifica se checksum e ack estão corretos '''
    if pacoteRecebido.checksum == pacoteRecebido.CalculaChecksum(pacoteRecebido.data):
        return True
    return False

def EnviaPacote(pacote, s, host, port):
    ''' coloca o pacote no formato certo e envia'''
    s.sendto(pacote.ToString(), (host, port))

if __name__ == '__main__':
    Cliente(sys.argv)
