from random import randint
from binascii import hexlify

'''
Referencias:
http://packetlife.net/blog/2010/jun/7/understanding-tcp-sequence-acknowledgment-numbers/
'''

class Pacote(object):
    def __init__(self):
        self.numeroSequencia = 0                             #8 bytes
        self.ack = 0                                         #8 bytes
        self.checksum = 0                                    #4 bytes
        self.sair = 0                                        #1 byte
        self.data = ""                                       #20 bytes ... 20 caracteres por vez
                                                             #Total: 41 bytes por pacote

    def ToString(self):
        ''' Prepara o pacote para ser enviado '''
        numeroSequencia = str(self.numeroSequencia + 1000000000)[2:]
        ack = str(self.ack + 1000000000)[2:]
        self.checksum = self.CalculaChecksum(self.data)
        checksum = str(self.checksum + 1000000)[2:]
        return (numeroSequencia + ack + checksum + str(self.sair) + self.data)

    def ToPacote(self, mensagem):
        ''' "descompacta" o pacote que foi recebido '''
        self.numeroSequencia = int(mensagem[0:8])
        self.ack = int(mensagem[8:14])
        self.checksum = int(mensagem[16:21])
        self.sair = int(mensagem[21:22])
        self.data = mensagem[22:]

    def CalculaChecksum(self, msg):
        ''' Calcula o checksum utilizando o conteudo da mensagem '''
        # Force data into 16 bit chunks for checksum
        if msg == '':
            return 0
        if (len(msg) % 2) != 0:
            msg += "0"
        s = 0
        for i in range(0, len(msg), 2):
            w = ord(msg[i]) + (ord(msg[i+1]) << 8)
            s = ((s+w) & 0xffff) + ((s+w) >> 16)
        return ~s & 0xffff
