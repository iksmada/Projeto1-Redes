# Projeto 1
Repositorio destinado para o desenvolvimento do projeto 1

Configuração:
*Testado no ubuntu 14.04*

1) Instalar apache2: sudo apt-get install apache2 (pode ser necessaria a instalação do pacote libapache2-mod-python)

2) Configurar o arquivo /etc/apache/sites-available/000-default.conf igual ao da pasta /config deste repositório

3) Criar diretório /var/cgi-bin: sudo mkdir /var/cgi-bin

4) Copiar o arquivo webserver.py para a pasta criada

5) Dar permissões para que o arquivo seja executado: sudo chmod +x /var/cgi-bin/webserver.py && sudo chmod 755 /var/cgi-bin/webserver.py

6) No browser entrar no endereço localhost/cgi-bin/webserver.py

Caso ocorra algum erro é recomentado procurar em:

1) http://perlmaven.com/perl-cgi-script-with-apache2

2) https://www.linux.com/community/blogs/129-servers/757148-configuring-apache2-to-run-python-scripts
