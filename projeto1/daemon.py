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
        
        mensagem = con.recv(1024)
        print "Recebeu \"" + mensagem + "\""
        #fecha conexao se receber "fechar" do servidor
                    #recebe o comando partindo do codigo recebido
        if mensagem:
            comando = decodifica(mensagem)
            if comando == "fechar":
                output = "ERRO 05: mensagem sem protocolo"
            else:
                mensagem = mensagem.split()
                print "\n" +  comando+"\n"
                saidaTerminal = os.popen(comando).read()
                if not saidaTerminal:                
                    saidaTerminal = "ERRO 07: Comando nao executado com sucesso"

                output = "RESPONSE "+mensagem[1]+" "+ saidaTerminal
        else:
            output = "ERRO 06: mensagem nula"
        try:
            #print "Enviou \"" + output + "\""
            con.send(output)

        except Exception:
            conexaoCliente.close()
            break
##so pra 1 argumento
def decodifica(cmd):
    lista = cmd.split()
    if lista[0] != "REQUEST":
        return "fechar"
    if lista[1] == "1":
        resultado = "ps"
    if lista[1] == "2":
        resultado = "df"
        #args=cmd.split("2")
    if lista[1] == "3":
        resultado = "finger"
        #args=cmd.split("3")
    if lista[1] == "4":
        resultado = "uptime"
        #args=cmd.split("4")
    del lista[0]
    del lista[0]
    
    for arg in lista:
        resultado += " -"+arg
    #resultado += args[1]
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
