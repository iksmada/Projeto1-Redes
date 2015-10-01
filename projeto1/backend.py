import socket


def enviarMsg(cmd):
    host = '127.0.0.1'
    porta = 5000
    conexaoServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destino = ((host, porta))
    try:
        conexaoServidor.connect(destino)
        if cmd:
    #for comando in cmd:
            conexaoServidor.send(cmd)
            cmd=""
        #recebe e printa comandos
            data = conexaoServidor.recv(1024)
            data = validaData(data)
        else:
            data="Comando nulo"

        conexaoServidor.close()

    except Exception:
        data="Sem conexao"

    return data

def validaData(mensagem):
    lista = mensagem.split()
    if lista[0] != "RESPONSE":
        return "Resposta Invalida"
    lista = mensagem.split("RESPONSE")    
    return  lista[1]
