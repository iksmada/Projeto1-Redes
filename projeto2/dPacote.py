from random import randint
from binascii import hexlify

'''
Referencias:
http://packetlife.net/blog/2010/jun/7/understanding-tcp-sequence-acknowledgment-numbers/
'''

class Pacote(object):
    def __init__(self):
        self.numeroSequencia = randint(100000000, 999999999) #8 bytes
        self.ack = 0                                         #8 bytes
        self.checksum = 0                                    #4 bytes
        self.flags = [0, 0, 0] # [SYN, ACK, FIN]              3 bytes
        self.data = ""                                       #20 bytes ... 20 caracteres por vez
                                                             #Total: 43 bytes por pacote

    def ToString(self):
        ''' Prepara o pacote para ser enviado '''
        numeroSequencia = str(self.numeroSequencia)[1:]
        ack = str(self.ack + 1000000000)[2:]
        self.checksum = self.CalculaChecksum(self.data)
        checksum = str(self.checksum + 100000)[2:]
        flags = ""
        for i in self.flags: flags += str(i)
        return (numeroSequencia + ack + checksum + flags + self.data)

    def ToPacote(self, mensagem):
        ''' "descompacta" o pacote que foi recebido '''
        self.numeroSequencia = int(mensagem[0:8])
        self.ack = int(mensagem[8:15])
        self.checksum = self.CalculaChecksum(mensagem[21:])#int(mensagem[8:12])
        self.flags = []
        for i in mensagem[18:21]: flags.append(int(i))
        self.flags = flags
        self.data = mensagem[21:]

    def CalculaChecksum(self, data):
        ''' Soma todos os dados e cria o checksum'''
        soma = 0
        for i in data: soma += ord(i)
        byte1 = chr(soma / 0xFF)
        byte2 = chr(soma & 0xFF)
        checksum = hexlify(byte1) + hexlify(byte2)
        return int(checksum)
