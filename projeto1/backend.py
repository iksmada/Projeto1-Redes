import socket

def enviarMsg(cmd):
    host = '127.0.0.1'
    porta = 5000
    conexaoServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destino = ((host, porta))
    try:
        conexaoServidor.connect(destino)
        if cmd:
            cmd=codifica(cmd)
            lista=cmd.split()
            nroCmd =lista[1]
            conexaoServidor.send(cmd)
            cmd=""
        #recebe e printa comandos
            try:
                data = conexaoServidor.recv(1024)
                if data:
                    data = validaData(data,nroCmd)
                else:
                    data= "ERRO 08: Resposta nula"
            except Exception:
                data="ERRO 01: Nao recebe"
                
        else:
            data="ERRO 02:Comando nulo"

        conexaoServidor.close()
    except Exception:
        data="ERRO 03: nao conecta"

    return data

def codifica(cmd):
    return cmd.replace("-","")
    

def validaData(mensagem,nro):
    lista = mensagem.split()
    if lista[0] != "RESPONSE" or lista[1] != nro:
        return "ERRO 04: Resposta Invalida"
    lista = mensagem.split("RESPONSE")    
    return  lista[1]
