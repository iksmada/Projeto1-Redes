import socket

def servidor(cmd):
    host = ''
    porta = 5000
    endereco = ((host, porta))
    conexaoServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexaoServidor.bind(endereco)
    #escuta no maximo tres maquinas
    conexaoServidor.listen(3)
    #aceita conexao
    con, addrCli = conexaoServidor.accept()

    while True:
        #Envia comandos
        for comando in cmd:
            con.send(comando)
            #recebe e printa comandos
            con.recv(1024)

    conexaoServidor.closse()

if __name__ == "__main__":
    servidor("1")
