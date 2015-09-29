import socket

def servidor(cmd):
    #print "entrou back"
    data = ''
    host = ''
    porta = 5000
    endereco = ((host, porta))
    conexaoServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexaoServidor.bind(endereco)
    # #escuta no maximo tres maquinas
    conexaoServidor.listen(3)
    # #aceita conexao
    con, addrCli = conexaoServidor.accept()
    #while True:
        #Envia comandos
    if cmd:
    #for comando in cmd:
        con.send(cmd)
        cmd=""
        #recebe e printa comandos
        data += con.recv(1024)

    conexaoServidor.close()
    return data
