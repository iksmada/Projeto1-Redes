#Servidor, responde requisicoes

import socket
import sys
from dPacote import Pacote

def Servidor(args):
    #recebe a porta pela linha de comando
    port = args[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", port))
    pacoteEnviar = Pacote()
    pacoteRecebido = Pacote()

    while True:
        pacoteRecebido, addr = RecebePacote(s.recvfrom(43))
        envioCorreto = VerificaPacote(pacoteRecebido)
        if envioCorreto:
            #muda os parametros do pacote pra pedir o proximo e salva o texto recebido
            arquivoRecebido += pacoteRecebido.data
            pacoteEnviar.numeroSequencia = pacoteRecebido.ack
            pacoteEnviar.ack = pacoteRecebido.ack + pacoteRecebido.numeroSequencia

        else:
            #pede pra reenviar, esse else ta aqui so pra melhorar o entendimento, a ideia eh reenviar
            #o mesmo pacote que foi enviado enteriormente, pois houve erro
            pass

        EnviaPacote(PacoteEnviar, s, addr, port)

    s.close()

def RecebePacote(pacoteRecebido):
    ''' Recebe o pacote e coloca em um formato mais facil de trabalhar'''
    msg, addr = s.recvfrom(33)
    pacoteRecebido.ToPacote(msg)
    return pacoteRecebido

def VerificaPacote(pacoteRecebido, host):
    ''' Verifica se checksum e ack estao corretos '''
    if pacoteRecebido.checksum == pacoteRecebido.CalculaChecksum(pacoteRecebido.data):
        return True
    return False

def EnviaPacote(pacoteEnviar, s, addr, port):
    ''' coloca o pacote no formato certo e envia'''
    s.sendto(pacoteEnviar.ToString(), (addr, port))

if __name__ == "__main__":
    Servidor(sys.argv)
