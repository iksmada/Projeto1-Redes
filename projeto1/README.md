# Projeto 1
Repositorio destinado para o desenvolvimento do projeto 1

Configuracao:
*Testado no ubuntu 14.04*

1) Instalar apache2: sudo apt-get install apache2 (pode ser necessaria a instalacao do pacote libapache2-mod-python e python)

2) Configurar o arquivo /etc/apache2/sites-available/000-default.conf igual ao da pasta /config deste repositorio.
	2.1) configurar da mesma maneira o arquivo /etc/apache2/conf-enabled/serve-cgi-bin.conf (caso nao tenha o arquivo copiar de /etc/apache2/conf-availabled).

3) Criar diretorio /var/cgi-bin: sudo mkdir /var/cgi-bin

4) Copiar o arquivo webserver.py para a pasta criada

5) Dar permissoes para que o arquivo seja executado: sudo chmod +x /var/cgi-bin/webserver.py && sudo chmod 755 /var/cgi-bin/webserver.py

6) Recarregue o apache: sudo /etc/init.d/apache2 reload

7) Se tudo parecer Ok, vá para a execução. Caso no passo 1 da execução o browser exiba o codigo ao inves de executa-lo use os seguintes comandos e em seguida recarregue o apache: 
	sudo a2enmod cgi
	sudo a2disconf serve-cgi-bin
	
	Caso ocorra algum erro é recomentado procurar em:

	1) http://perlmaven.com/perl-cgi-script-with-apache2

	2) https://www.linux.com/community/blogs/129-servers/757148-configuring-apache2-to-run-python-scripts

	3)http://askubuntu.com/questions/547391/apache2-4-7-on-ubuntu-14-04-wont-execute-python-cgi-file-the-site-displays-pyt

	4) http://askubuntu.com/questions/547391/apache2-4-7-on-ubuntu-14-04-wont-execute-python-cgi-file-the-site-displays-pyt

[PADRÃO] Execução na mesma maquina:

1) No browser entrar no endereço localhost/cgi-bin/webserver.py

1) Executar python daemon.py

2) Enviar comando pela web

OBS: neste modo o host padrao é 127.0.0.1, assim todas as maquinas executarao no mesmo daemon, para ter acesso remoto siga o proximo topico

Execução remota:

1) altere o codigo do backend.py na atribuicao da variavel host:
	A)troque o código 
		#host = "192.168.0." + str(nroMaq)
		host = '127.0.0.1'
	B)por
		host = "192.168.0." + str(nroMaq)
		#host = '127.0.0.1'

2)Crie uma rede interna e defina o ip das maquinas que rodarão o deamon.py com os IP's 192.168.0.x , X=1,2,3

3)Conecte a maquina que ira rodar a pagina web (webserver) na rede interna e siga os passos da Execução na mesma maquina
