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
    janela = 3
    numeroSequenciaEsperado = 0

    while(True):
        try:
            pacoteRecebido = RecebePacote()
        except socket.timeout:
            enviocorreto = 0
        envioCorreto = VerificaPacote(pacoteRecebido)
        if envioCorreto:
            #muda os parametros do pacote pra pedir o proximo e salva o texto recebido
            arquivoRecebido += pacoteRecebido.data
            EnviaAck(s, pacoteRecebido, host, port)
            numeroSequenciaEsperado += 1
        else:
            #pede pra reenviar, esse else ta aqui so pra melhorar o entendimento, a ideia eh reenviar
            #o mesmo pacote que foi enviado enteriormente, pois houve erro
            pass

        EnviaPacote(PacoteEnviar, s, host, port)

    #Cliente aceita encerrar e acaba a comunicacao
    s.close()
    EscreveArquivo(arquivoRecebido)

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

def EnviaAck(s,pacoteRecebido, host, porta):
    """ACK the given seq_num pkt"""
    pacoteRecebido.data = ''
    s.sendto(pacoteRecebido.toString(), (host, porta)) #Envia o pacote todo, mas so importa o numero de sequencia
    print 'Servidor enviou ACK, nro sequencia: ', pacoteRecebido.numeroSequencia

def EscreveArquivo(arquivo):
    ''' Escreve o texto recebido do servidor em um arquivo chamado Arquivo_recebido.txt '''
    arquivo = open("Arquivo_recebido.txt", "w")
    arquivo.write(arquivo)

if __name__ == '__main__':
    Cliente(sys.argv)
