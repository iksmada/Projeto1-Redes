# Projeto 1
Repositorio destinado para o desenvolvimento do projeto 1

Configuração:
*Testado no ubuntu 14.04*

1) Instalar apache2: sudo apt-get install apache2 (pode ser necessaria a instalação do pacote libapache2-mod-python e python)

2) Configurar o arquivo /etc/apache/sites-available/000-default.conf igual ao da pasta /config deste repositório
	2.1) configurar da mesma maneira o arquivo 	/etc/apache2/conf-enabled/serve-cgi-bin.conf (caso nao 	tenha o arquivo copiar de /etc/apache2/conf-availabled )

3) Criar diretório /var/cgi-bin: sudo mkdir /var/cgi-bin

4) Copiar o arquivo webserver.py para a pasta criada

5) Dar permissões para que o arquivo seja executado: sudo chmod +x /var/cgi-bin/webserver.py && sudo chmod 755 /var/cgi-bin/webserver.py

	Caso ocorra algum erro é recomentado procurar em:

	1) http://perlmaven.com/perl-cgi-script-with-apache2

	2) https://www.linux.com/community/blogs/129-servers/757148-configuring-apache2-to-run-python-scripts

	3)http://askubuntu.com/questions/547391/apache2-4-7-on-ubuntu-14-04-wont-execute-python-cgi-file-the-site-displays-pyt

Execu��o:

1) No browser entrar no endereço localhost/cgi-bin/webserver.py

2) Enviar comando

3) abrir deamon.py