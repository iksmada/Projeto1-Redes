from random import randint

class Pacote(object):
    def __init__ (self):
        self.nSequencia=randint(0,0xFFFFFFFF)
        self.ack=0
        self.flags=[0,0,0]
        self.checksum=0
        self.data= ""
        '''
        pacote[0:4]   : Numero de sequencia (Aleatorio) 4 bytes
        pacote[5:9]   : ACK = 1+numero_seq_recebido     4 bytes
        pacote[10:15] : Checksum                        2 bytes
        pacote[3] : ACK, SYN, FIN                     3 bytes
        pocate[15:]   : Data                            20 bytes

        total bytes:                                    33 bytes
        '''

    def toString(self):
        retorno=""
        retorno+=chr((self.nSequencia/0xFFFFFF))
        retorno+=chr((self.nSequencia/0xFFFF)&0xFF)
        retorno+=chr((self.nSequencia/0xFF)&0xFF)
        retorno+=chr(self.nSequencia&0xFF)
        # seq += "000"+str(self.nSequencia)
        # tamanho = len(seq)
        # tamanho =tamanho-4
        # retorno=seq[tamanho:]

        retorno+=chr((self.ack/0xFFFFFF))
        retorno+=chr((self.ack/0xFFFF)&0xFF)
        retorno+=chr((self.ack/0xFF)&0xFF)
        retorno+=chr(self.ack&0xFF)
        # aqi +="000"+str(self.ack)
        # tamanho = len(aqi)
        # tamanho =tamanho-4
        # retorno+= aqi[tamanho:]

        for i in self.flags: retorno+=str(i)

        retorno+=chr((self.checksum/0xFF))
        retorno+=chr(self.checksum&0xFF)

        for i in self.data: retorno+=i
        return retorno

    def toPacote(self,msg):
        header=msg[0:13]
        dados=msg[13:]

        for i in dados: self.data+=dados
        self.nSequencia=int(header[0:4])
        self.ack= int(header[4:8])

        j=0
        for i in header[8:11]:
            self.flags[j]=i
            j+=1

        self.checksum= int(header[11:13])




p=Pacote()
print p.nSequencia
print p.toString()
p.toPacote(p.toString())
print p.nSequencia
