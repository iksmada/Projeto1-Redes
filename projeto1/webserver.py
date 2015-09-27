#!/usr/bin/python
# coding=UTF-8

from backend import servidor
import cgi

print "Content-Type: text/html"
print
print '''\
<html>
    <head>
        <title> Trabalho 1 - Redes, web v2</title>
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
                        <input type="checkbox" name="cmd1" value="1">ps<br>
                        <input type="checkbox" name="cmd1" value="2">df<br>
                        <input type="checkbox" name="cmd1" value="3">finger<br>
                        <input type="checkbox" name="cmd1" value="4">uptime<br>
                    </div>
                </div>
                <div id="maquina2" style="width:30%; height:30%; float:left;">
                    <p>Comando - Maquina 2</p>
                    <div id="alinha2" style="float:center; text-aling:left;">
                        <input type="checkbox" name="cmd2" value="1">ps<br>
                        <input type="checkbox" name="cmd2" value="2">df<br>
                        <input type="checkbox" name="cmd2" value="3">finger<br>
                        <input type="checkbox" name="cmd2" value="4">uptime<br>
                    </div>
                </div>
                <div id="maquina3" style="width:30%; height:30%; float:left; text-align:left;">
                       <p>Comando - Maquina 3</p>
                       <input type="checkbox" name="cmd3" value="1">ps<br>
                       <input type="checkbox" name="cmd3" value="2">df<br>
                       <input type="checkbox" name="cmd3" value="3">finger<br>
                       <input type="checkbox" name="cmd3" value="4">uptime<br>
                       <br>
                       <input type="submit" value="Enviar" />
                </div>
            </form>
        </div>
        <div id="containterCmd" style="width:90%; height :30%; text-align:center;margin:0 auto; border-radius:5px; padding:50px">
            <hr>
            <div id="maquina1r" style="width:30%; height:30%; float:left;text-align:right">
                <p>Resposta - Maquina 1</p>
                <textarea readonly name="comments1" cols="25" rows="5"></textarea>
            </div>
            <div id="maquina2r" style="width:30%; height:30%;float:left;">
                <p>Resposta - Maquina 2</p>
                <textarea readonly name="comments2" cols="25" rows="5"></textarea>
            </div>
            <div id="maquina3r" style="width:30%; height:30%;float:left;text-align:left">
                <p>Resposta - Maquina 3</p>
                <textarea readonly name="comments3" cols="25" rows="5"></textarea>
            </div>
        </div>
    </body>
</html>
'''

form = cgi.FieldStorage()
cmdMaquina1 = form.getlist("cmd1")
cmdMaquina2 = form.getlist("cmd2")
cmdMaquina3 = form.getlist("cmd3")
if cmdMaquina1:
    servidor(cmdMaquina1)
