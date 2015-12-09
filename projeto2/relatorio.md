#### Relatório de Redes :ok_hand:
Nome | RA
---------------------------|-------
Cristian Pendenza | 489115
José Fernando Garcia Junior| 408620
Raphael Adamski| 495913
Vinicius de Paula Pereira | 489468

##### Descrição da Implementacao

###### Nosso cabeçalho é composto por cinco campos:
 - Numero de sequencia: representado pelos 8 primeiros caracteres da mensagem que é enviada pelo socket;
 - Ack: representado pelos 8 caracteres da mensagem depois do número de sequencia;
 - Checksum: representado pelos 4 caracteres da mensagem depois do ack;
 - Sair: representado por 1 caracter depois do checksum, pode ser 0 ou 1, 1 indica sair;
 - Data: É o dado que esta sendo enviado, são os ultimos 20 caracteres.

###### As mensagens
 - Cada mensagem enviada possui 41 bytes, como pode ser observado pela descrição do cabeçalho acima;
 - Quando as mensagens chegam são logo convertidas para o formato de "Pacote", para facilitar o trabalho;
 - Ao ser enviada a mensagem é automaticamente transformada em string.

###### Tempo de espera:
 - O servidor espera 1.1 segundos, pode ser facilmente observado pela constante TIMEOUT;
 - Ao fim desse tempo o servidor reenvia o pacote.

###### Protocolo baseado em janela:
 - Neste projeto foi utilizado o protocole Go-Back-N;
 - Isso significa que as mensagens são enviadas N vezes (neste projeto N = 3, que é o tamanho da janela) sem se preocupar com o envio correto dos pacotes, quando a janela fecha os pacotes perdidos são reenviados.

##### Dificuldades e resoluções:
  - A principal dificuldade neste projeto foi que em determinada parte do projeto o servidor acabava enviando muitos pacotes desnecessarios e os integrantes não conseguiam identificar por que isso estava ocorrendo. Para resolver esse problema foi implementado o tripleNack no servidor;
  - Outra dificuldade foi o calculo do checksum Foi resolvido pesquisando, principalmente no StackOverflow.
