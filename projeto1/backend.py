import socket

def servidor(cmd):
    #print "entrou back"
    data = ''
    host = '127.0.0.1'
    porta = 5000
    conexaoServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destino = ((host, porta))
    output = ""
    conexaoServidor.connect(destino)
    #while True:
        #Envia comandos
    if cmd:
    #for comando in cmd:
        conexaoServidor.send(cmd)
        cmd=""
        #recebe e printa comandos
        data = conexaoServidor.recv(1024)

    conexaoServidor.close()
    return data
