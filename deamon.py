import os
import socket

def main():
    #conexao com socket recebe comando
    host = raw_input("Enedereco ip do servidor..: ")
    porta = 5000
    conexaoCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destino = ((host, porta))
    output = ""
    conexaoCliente.connect(destino)

    while True:
        #recebe comando
        comando = conexaoCliente.recv(1024)
        #fecha conexao se receber "fechar" do servidor
        if comando == "fechar":
            break
        #recebe o comando partindo do codigo recebido
        comando = decodifica(comando)
        #executa comando(S)
        print "Vou executar o comando: "+comando
        output = "\nComando "+comando+" saida:\n" + os.popen(comando).read() + "\n"
        #cenvia saida do(S) comando(S)
        conexaoCliente.send(output)
    conexaoCliente.close()

def decodifica(cmd):
    if cmd == "1":
        return "ps"
    if cmd == "2":
        return "df"
    if cmd == "3":
        return "finger"
    return"uptime"


if __name__ == "__main__":
    main()
