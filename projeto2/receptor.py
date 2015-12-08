# -*- coding: UTF-8 -*-
#Cliente, faz requisicoes

import socket
import sys
from time import sleep
from Pacote import Pacote

def Cliente(args):
    if len(args) < 3:
        print 'Entrada errada. execucao se da por:\n\tpython receptor.py <hostname> <porta> <nome_arquivo>'
        sys.exit()
    pacoteEnviar = Pacote()
    pacoteRecebido = Pacote()
    arquivoRecebido = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #recebe ip, porta e nome do arquivo pela linha de comando
    host = args[1]
    port = int(args[2])
    arq_name = args[3]
    #Numero de pacotes que podem ser enviados sem confirmação
    janela = 3
    numeroSequenciaEsperado = 0
    numeroSequenciaAntigo = 0

    while(True):
        try:
            EnviaAck(s, pacoteRecebido, host, port)
            pacoteRecebido, addr = RecebePacote(s)
        except socket.timeout:
            enviocorreto = 0
        envioCorreto = VerificaPacote(pacoteRecebido)
        print envioCorreto
        sleep(0.2)
        if envioCorreto and numeroSequenciaEsperado==pacoteRecebido.numeroSequencia :
            #muda os parametros do pacote pra pedir o proximo e salva o texto recebido
            arquivoRecebido += pacoteRecebido.data
            #print arquivoRecebido
            EnviaAck(s, pacoteRecebido, host, port)
            numeroSequenciaAntigo = numeroSequenciaEsperado
            numeroSequenciaEsperado += 1
        else:
            #pacoteRecebido.numeroSequencia = numeroSequenciaAntigo
            EnviaAck(s, pacoteRecebido, host, port)
            print "recebi errado, esperava",numeroSequenciaEsperado
        if pacoteRecebido.numeroSequencia==54:
            break
    #Cliente aceita encerrar e acaba a comunicacao
    s.close()
    print arquivoRecebido
    EscreveArquivo(arquivoRecebido)

def RecebePacote(s):
    ''' Recebe o pacote e coloca em um formato mais facil de trabalhar'''
    pacoteRecebido = Pacote()
    msg, addr = s.recvfrom(4096)
    pacoteRecebido.ToPacote(msg)
    return pacoteRecebido, addr

def VerificaPacote(pacoteRecebido):
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
    #print pacoteRecebido.ToString()
    s.sendto(pacoteRecebido.ToString(), (host, porta)) #Envia o pacote todo, mas so importa o numero de sequencia
    print 'Cliente enviou ACK, nro sequencia: ', pacoteRecebido.numeroSequencia

def EscreveArquivo(conteudo):
    ''' Escreve o texto recebido do servidor em um arquivo chamado Arquivo_recebido.txt '''
    try:
        arquivo = open("Arquivo_recebido.txt", "w")
        arquivo.write(conteudo)
    except Exception:
        print 'Impossível escrever arquivo:\n\tVerifique se o arquivo já existe e o programa tem permissão de escrita'

if __name__ == '__main__':
    Cliente(sys.argv)
