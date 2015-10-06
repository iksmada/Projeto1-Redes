#!/usr/bin/python
# coding=UTF-8

from backend import enviarMsg
import cgi, cgitb
import Queue
from threading import Thread

class Th(Thread):
    def __init__ (self,comando,nroMaq,fila):
        Thread.__init__(self)
        self.cmd = comando
        self.nro =nroMaq
        self.q = fila
        

    def run(self):
        self.q.put(enviarMsg(self.cmd,self.nro)) #coloca na filao retorno da msg enviada ao servidor
        

cmdMaquina1 = "REQUEST "
cmdMaquina2 = "REQUEST "
cmdMaquina3 = "REQUEST "
fila1=Queue.Queue()
fila2=Queue.Queue()
fila3=Queue.Queue()
saidaMaquina1 = ""
saidaMaquina2 = ""
saidaMaquina3 = ""

threads= []

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
	    	<div>
		        <div id="maquina1" style="width:13%; height:30%; float:left; text-align:left;margin-left:18%">
		            <p>Comando - Maquina 1</p>
		            
		                <input type="radio" name="cmd1" value="1">ps<br>
		                <input type="radio" name="cmd1" value="2">df<br>
		                <input type="radio" name="cmd1" value="3">finger<br>
		                <input type="radio" name="cmd1" value="4">uptime<br>
		                <input type="text" name="cmd1" placeholder="Argumentos">
		            
		        </div>
		        <div id="maquina2" style="width:13%; height:30%; float:left; text-align:left;margin-left:10%">
		            <p>Comando - Maquina 2</p>
		            
		                <input type="radio" name="cmd2" value="1">ps<br>
		                <input type="radio" name="cmd2" value="2">df<br>
		                <input type="radio" name="cmd2" value="3">finger<br>
		                <input type="radio" name="cmd2" value="4">uptime<br>
		                <input type="text" name="cmd2" placeholder="Argumentos">
		            
		        </div>
		        <div id="maquina3" style="width:13%; height:30%; float:left; text-align:left;margin-left:10%">
		               <p>Comando - Maquina 3</p>
		               <input type="radio" name="cmd3" value="1">ps<br>
		                <input type="radio" name="cmd3" value="2">df<br>
		                <input type="radio" name="cmd3" value="3">finger<br>
		                <input type="radio" name="cmd3" value="4">uptime<br>
		                <input type="text" name="cmd3" placeholder="Argumentos">
				        <br></br>
		               <input type="submit" value="Enviar" />
                        <input type="reset" value="Clean" />
		        </div>
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
    thread1= Th(cmdMaquina1,1,fila1)
    thread1.start()
    threads.append(thread1)
    cmdMaquina1 =="REQUEST "
#Envia os comandos para a maquina 2
if cmdMaquina2 !="REQUEST ":
    thread2= Th(cmdMaquina2,2,fila2)
    thread2.start()
    threads.append(thread2)
    cmdMaquina2 =="REQUEST "
#Envia os comandos para a maquina 3
if cmdMaquina3 !="REQUEST ":
    thread3= Th(cmdMaquina3,3,fila3)
    thread3.start()
    threads.append(thread3)
    cmdMaquina2 =="REQUEST "

#espera terminar todas
for t in threads:
    t.join()
threads=[]
#pega respostas nas filas criadas
if not fila1.empty():
    saidaMaquina1=fila1.get()
    fila1.task_done()

if not fila2.empty():
    saidaMaquina2=fila2.get()
    fila2.task_done()

if not fila3.empty():
    saidaMaquina3=fila3.get()
    fila3.task_done()
print ''' <div>
        	<div id="containterCmd" style="width:90%; height :30%; text-align:center;margin:0 auto; border-radius:5px; padding:50px">
            	<br><hr>

            	    <div id="maquina1r" style="width:13%; height:30%; float:left;text-align:left";>
                	<p>Resposta - Maquina 1</p>
	 	    </div>
	
'''
            #Escreve os comandos na caixa de texto da maquina 1
print "     	    <div><textarea readonly name=\"comments1\" cols=\"110\" rows=\"10\">%s</textarea>" %saidaMaquina1
print '''\
            	    </div>
		    </br>
                    <div id="maquina2r" style="width:13%; height:30%;float:left;text-align:left;">
                         <p>Resposta - Maquina 2</p>
	            </div>
'''
            #Escreve os comandos na caixa de texto da maquina 2
print "             <div> <textarea readonly name=\"comments2\" cols=\"110\" rows=\"10\">%s</textarea>" %saidaMaquina2
print '''\
                    </div>
		    </br>
                    <div id="maquina3r" style="width:13%; height:30%;float:left;text-align:left">
                        <p>Resposta - Maquina 3</p>
	            </div>
'''
            #Escreve os comandos na caixa de texto da maquina 3
print "             <textarea readonly name=\"comments3\" cols=\"110\" rows=\"10\">%s</textarea>" %saidaMaquina3
print '''\
                </div>
        </div>
    </body>
</html>
'''
