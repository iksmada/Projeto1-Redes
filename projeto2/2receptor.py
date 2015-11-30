#Cliente, faz requisicoes

import socket
import sys
from time import sleep
from dPacote import Pacote

def Cliente(args):
    pacoteEnviar = Pacote()
    pacoteRecebido = Pacote()
    arquivoRecebido = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #recebe ip, porta e nome do arquivo pela linha de comando
    host = args[1]
    port = args[2]
    arq_name = args[3]

    while(True):
        IniciaConexao(s, host, port)
        pacoteRecebido = RecebePacote()
        envioCorreto = VerificaPacote(pacoteRecebido)
        if envioCorreto:
            #muda os parametros do pacote pra pedir o proximo e salva o texto recebido
            arquivoRecebido += pacoteRecebido.data
            pacoteEnviar.numeroSequencia = pacoteRecebido.ack
            pacoteEnviar.ack = pacoteRecebido.ack + pacoteRecebido.numeroSequencia
            if(pacoteRecebido.flags[2] == 1): #Flago[2] indica FIN
                pacoteEnviar.flags[2] = 1
                EnviaPacote(PacoteEnviar, s, host, port) #Envia o pacote e sai
                break
        else:
            #pede pra reenviar, esse else ta aqui so pra melhorar o entendimento, a ideia eh reenviar
            #o mesmo pacote que foi enviado enteriormente, pois houve erro
            pass

        EnviaPacote(PacoteEnviar, s, host, port)

    #Cliente aceita encerrar e acaba a comunicacao
    s.close()

def RecebePacote():
    ''' Recebe o pacote e coloca em um formato mais facil de trabalhar'''
    msg, addr = s.recvfrom(33)
    pacoteRecebido.ToPacote(msg)
    return pacoteRecebido

def VerificaPacote(pacoteRecebido, host):
    ''' Verifica se checksum e ack estao corretos '''
    if pacoteRecebido.checksum == pacoteRecebido.CalculaChecksum(pacoteRecebido.data):
        return True
    return False

def EnviaPacote(pacote, s, host, port):
    ''' coloca o pacote no formato certo e envia'''
    s.sendto(pacote.ToString(), (host, port))

def IniciaConexao(s, host, port):
    ''' Faz a conexão inicial, envia um SYN, recebe um SYN ACK e envia um ACK'''
    pacoteEnvia = Pacote()
    pacoteRecebe = Pacote()
    pacoteEnvia.flags[0] = 1
    while True:
        #Espera receber um SYN ACK
        EnviaPacote(pacoteEnvia, s, host, port)
        pacoteRecebe = RecebePacote()
        if VetificaPacote(pacoteRecebe) and pacoteRecebe.flags[0] == 1 and pacoteRecebe.flags[1] == 1:
            break

    pacoteEnvia.numeroSequencia = pacoteRecebe.ack
    pacoteEnviar.ack = pacoteRecebe.ack + pacoteRecebe.numeroSequencia
    #Considerar que o ACK vai ser o pedido do arquivo, agora

if __name__ == '__main__':
    Cliente(sys.argv)
