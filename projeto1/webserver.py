#!/usr/bin/python
# coding=UTF-8

from backend import servidor
import cgi, cgitb
cmdMaquina1 = "REQUEST "
cmdMaquina2 = "REQUEST "
cmdMaquina3 = "REQUEST "
saidaMaquina1 = ""
saidaMaquina2 = ""
saidaMaquina3 = ""

print "Content-Type: text/html"
print
print '''\
<html>
    <head>
        <title> Trabalho 1 - Redes v3</title>
    </head>
    <body>
        <div id="containterCmd" style="width:90%; height :30%; text-align:center;margin:0 auto; border-radius:5px; padding:20px;">
            <div id="header" style="text-align:center;">
                <h1> Trabalho 1 - Redes </h1>
            </div>
            <form method="post" action="">
                <div id="maquina1" style="width:30%; height:30%; float:left;text-align:right">
                    <p>Comando - Maquina 1</p>
                    <div id="alinha1" style="float:right; text-align:left">
                        <input type="radio" name="cmd1" value="1">ps<br>
                        <input type="radio" name="cmd1" value="2">df<br>
                        <input type="radio" name="cmd1" value="3">finger<br>
                        <input type="radio" name="cmd1" value="4">uptime<br>
                        <input type="text" name="cmd1" placeholder="Argumentos"><br>
                    </div>
                </div>
                <div id="maquina2" style="width:30%; height:30%; float:left;">
                    <p>Comando - Maquina 2</p>
                    <div id="alinha2" style="float:center; text-aling:left;">
                        <input type="radio" name="cmd2" value="1">ps<br>
                        <input type="radio" name="cmd2" value="2">df<br>
                        <input type="radio" name="cmd2" value="3">finger<br>
                        <input type="radio" name="cmd2" value="4">uptime<br>
                        <input type="text" name="cmd2" placeholder="Argumentos"><br>
                    </div>
                </div>
                <div id="maquina3" style="width:30%; height:30%; float:left; text-align:left;">
                       <p>Comando - Maquina 3</p>
                       <input type="radio" name="cmd3" value="1">ps<br>
                        <input type="radio" name="cmd3" value="2">df<br>
                        <input type="radio" name="cmd3" value="3">finger<br>
                        <input type="radio" name="cmd3" value="4">uptime<br>
                        <input type="text" name="cmd3" placeholder="Argumentos"><br>
                                               
                        <br>
                       <input type="submit" value="Enviar" />
                </div>
            </form>
        </div>
'''
form = cgi.FieldStorage()
cmdMaquina1 += " ".join(form.getlist("cmd1"))
cmdMaquina2 += " ".join(form.getlist("cmd2"))
cmdMaquina3 += " ".join(form.getlist("cmd3"))
#Envia os comandos para a maquina 1
#print cmdMaquina1
if cmdMaquina1 !="REQUEST ":
    saidaMaquina1 += servidor(cmdMaquina1)
    cmdMaquina1 =="REQUEST "
#Envia os comandos para a maquina 2
if cmdMaquina2 !="REQUEST ":
    saidaMaquina2 += servidor(cmdMaquina2)
#Envia os comandos para a maquina 3
if cmdMaquina3 !="REQUEST ":
    saidaMaquina3 += servidor(cmdMaquina3)

print '''\
        <div id="containterCmd" style="width:90%; height :30%; text-align:center;margin:0 auto; border-radius:5px; padding:50px">
            <hr>
            <div id="maquina1r" style="width:30%; height:30%; float:left;text-align:right">
                <p>Resposta - Maquina 1</p>
'''
            #Escreve os comandos na caixa de texto da maquina 1
print "<textarea readonly name=\"comments1\" cols=\"25\" rows=\"50\">%s</textarea>" %saidaMaquina1
print '''\
            </div>
            <div id="maquina2r" style="width:30%; height:30%;float:left;">
                <p>Resposta - Maquina 2</p>
'''
            #Escreve os comandos na caixa de texto da maquina 2
print "<textarea readonly name=\"comments2\" cols=\"25\" rows=\"50\">%s</textarea>" %saidaMaquina2
print '''\
            </div>
            <div id="maquina3r" style="width:30%; height:30%;float:left;text-align:left">
                <p>Resposta - Maquina 3</p>
'''
            #Escreve os comandos na caixa de texto da maquina 3
print "<textarea readonly name=\"comments3\" cols=\"25\" rows=\"50\">%s</textarea>" %saidaMaquina3
print '''\
            </div>
        </div>
    </body>
</html>
'''
