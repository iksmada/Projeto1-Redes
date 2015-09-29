import os
import socket

def main():
    print "entrou deamon"
    #conexao com socket recebe comando
    host = '127.0.0.1'
    porta = 5000
    mensagem = 'REQUEST 1 -ef -t | ; > . . ..'
    if True:
        comando = decodifica(mensagem)
        if comando == "fechar":
            output = "mensagem bugada"
        else:
            print "exec Comando "+ comando + "\n"
            #executa comando(S)
            output = "\nComando "+comando+" saida:\n" + os.popen(comando).read() + "\n"
	print output
	raw_input()
        
def decodifica(cmd):
    print "cmd:"+cmd+"|\n"
    lista = cmd.split()
    print lista
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
    print resultado
    raw_input()
    return resultado

def protege(cmd):
    onde = '0'
    while onde>-1:
        onde = cmd.find('|')
        if onde>-1:
            cmd[onde]=' '
    onde = '0'
    while onde>-1:
        onde = cmd.find(';')
        if onde>-1:
            cmd[onde]=' '
    onde = '0'
    while onde>-1:
        onde = cmd.find('>')
        if onde>-1:
            cmd[onde]=' '
    onde = '0'
    while onde>-1:
        onde = cmd.find('.')
        if onde>-1:
            cmd[onde]=' '
    print cmd
    raw_input()
    return cmd

        
    

if __name__ == "__main__":
    main()
