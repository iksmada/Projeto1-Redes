from random import randint
from binascii import hexlify

class Pacote(object):
    def __init__(self):
        self.numeroSequencia = randint(10000, 99999)
        self.ack = 0
        self.checksum = 0
        self.flags = [0, 0, 0]
        self.data = ""

    def ToString(self):
        ''' Prepara o pacote para ser enviado '''
        numeroSequencia = str(self.numeroSequencia)[1:]
        ack = str(self.ack + 10000)[1:]
        checksum = str(self.checksum + 10000)[1:]
        flags = ""
        for i in self.flags: flags += str(i)
        return (numeroSequencia + ack + checksum + flags + self.data)

    def ToPacote(self, mensagem):
        ''' "descompacta" o pacote que foi recebido '''
        self.numeroSequencia = int(mensagem[0:4])
        self.ack = int(mensagem[4:8])
        self.checksum = self.CalculaChecksum(mensagem[15:])#int(mensagem[8:12])
        self.flags = []
        for i in mensagem[12:15]: flags.append(int(i))
        self.flags = flags
        self.data = mensagem[15:]

    def CalculaChecksum(self, data):
        ''' Soma todos os dados e cria o checksum'''
        soma = 0
        for i in data: soma += ord(i)
        byte1 = chr(soma / 0xFF)
        byte2 = chr(soma & 0xFF)
        checksum = hexlify(byte1) + hexlify(byte2)
        return int(checksum)
