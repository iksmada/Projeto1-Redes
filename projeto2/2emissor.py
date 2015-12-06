#Servidor, responde requisicoes

import socket
import sys
import select
from dPacote import Pacote

TIMEOUT = 1.1

def Servidor(args):
    #recebe a porta pela linha de comando
    port = int(args[1])
    #Nao consegui fazer o cliente pedir o arquivo, tem que entrar com o nome
    nomeArquivo = args[2]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", port))
    pacoteEnviar = Pacote()
    pacoteRecebido = Pacote()
    janela = 3
    texto = LeArquivo(nomeArquivo)
    pacotes = CriaPacotes(texto)

    nackAntigo = 0
    nack = 0
    #Logica do rdt send
    while nackAntigo < len(pacotes):
        # Can we send a packet, do we need to send pkt
        if nack < janela and (nack + nackAntigo) < len(pacotes):
            send_pkt(pacotes[nackAntigo + nack], s)
            nack += 1
        else:
            #Espera pelos acks do cliente
            ready = select.select([s], [], [], TIMEOUT)
            if ready[0]:
                pacoteRecebido, addr = RecebePacote()
            else: # Janela encheu
                print "Atingiu timeout"
                nack = 0

            if pacoteRecebido.numeroSequencia == nackAntigo:
                nackAntigo += 1
                nack -= 1
            else:
                nack = 0
    # Close server connection and exit successfully
    sock.close()
    sys.exit(0)

def RecebePacote():
    ''' Recebe o pacote e coloca em um formato mais facil de trabalhar'''
    msg, addr = s.recvfrom(4096)
    pacoteRecebido.ToPacote(msg)
    return pacoteRecebido, addr

def VerificaPacote(pacoteRecebido, host):
    ''' Verifica se checksum e ack estao corretos '''
    if pacoteRecebido.checksum == pacoteRecebido.CalculaChecksum(pacoteRecebido.data):
        return True
    return False

def EnviaPacote(pacoteEnviar, s, addr, port):
    ''' coloca o pacote no formato certo e envia'''
    s.sendto(pacoteEnviar.ToString(), (addr, port))

def LeArquivo(nome):
    ''' Le o arquivo e joga tudo em uma variavel '''
    texto = open(nome, 'r')
    return texto.read()

def CriaPacotes(texto):
    ''' forma uma lista de pacotes que contem todos os pacotes que serao enviados '''
    numeroSequencia = 0
    pacotes = []
    pacote = Pacote()
    while texto:
        #Forma o pacote
        pacote.numeroSequencia = numeroSequencia
        pacote.ack = 0
        #Envia de 20 em 20 caracteres
        pacote.data = text[:20]
        pacote.checksum = pacote.CalculaChecksum(pacote.data)
        pacote.chegou = False
        #adciona o pacote na lista de pacotes
        pacotes.append(pacote)
        texto = texto[:20]
        seq_num += 1
    # Newly built list of pacotes
    return pacotes


if __name__ == "__main__":
    Servidor(sys.argv)
