import os
import socket

def main():
    print "entrou deamon"
    #conexao com socket recebe comando
    saidaTerminal = ''
    host = ''
    porta = 5000
    endereco = ((host, porta))
    conexaoCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexaoCliente.bind(endereco)
    # #escuta no maximo tres maquinas
    conexaoCliente.listen(3)
    # #aceita conexao

    while True:
        con, addrCli = conexaoCliente.accept()
        #recebe comando
        mensagem = con.recv(1024)
        #fecha conexao se receber "fechar" do servidor
                    #recebe o comando partindo do codigo recebido
        comando = decodifica(mensagem)
        if comando == "fechar":
            output = "mensagem bugada"
        else:
            #print "exec Comando "+ comando + "\n"
            #executa comando(S)
            output = "RESPONSE "+comando + os.popen(comando).read()
        #cenvia saida do(S) comando(S)
        try:
            con.send(output)

        except Exception:
            conexaoCliente.close()
            break

def decodifica(cmd):
    print "cmd:"+cmd+"|\n"
    lista = cmd.split()
    if lista[0] != "REQUEST":
        return "fechar"
    if lista[1] == "1":
        resultado = "ps"
        args=cmd.split("1")
    if lista[1] == "2":
        resultado = "df"
        args=cmd.split("2")
    if lista[1] == "3":
        resultado = "finger"
        args=cmd.split("3")
    if lista[1] == "4":
        resultado = "uptime"
        args=cmd.split("4")
    resultado += args[1]
    resultado = protege(resultado)
    return resultado

def protege(cmd):
    cmd = cmd.replace("|","")
    cmd = cmd.replace(">","")
    cmd = cmd.replace(";","")
    cmd = cmd.replace(".","")
    return cmd
    

if __name__ == "__main__":
    main()
