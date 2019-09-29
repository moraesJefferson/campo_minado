# CAMPO MINADO

# SISTEMAS DISTRIBUÍDOS 2019.2 

# 1) INSTALL PIP3

    # WINDOWS

 - Faça o download do arquivo https://drive.google.com/open?id=1Jhe2SHQmLOyEU7ESxef0Ff41pZmgShbh
 - Abra o prompt na pasta onde o arquivo foi baixado
 - Rode o comando:  python get-pip.py

    # LINUX

 - rode o comando no terminal linux: sudo apt-get install python3-pip

 # 2) INSTALL PYGAME 

    # WINDOWS

    - No prompt de comando rode o o seguinte trecho: pip3 install pygame
    
    # LINUX

    - No terminal linux rode o seguinte comando: sudo apt install python3-pygame

# 3) JOGAR

    # CAMPO MINADO MONOLITICO

    - Abra o terminal na pasta campo_minado_monolitico
    Caso a pasta esteja em documentos rode o seguinte comando no terminal/prompt: 
    
    cd documents/campo_minado_monolitico

    - Estando dentro da pasta, para rodar o jogo, basta executar o comando:
        Python campo_minado_view.py

    Selecione 1 para jogar

    Selecione 2 para continuar um jogo(Essa opção so aparecerá caso exista um jogo salvo)

    Selecione 3 para sair

    Ao selecionar a opçao 1 sera pedido o número de linhas e colunas do campo minado,
    passe o valor desejado. Após isso, será exibido o campo minaod e solicitado ao jogador a linha e coluna para começar a partida. O processo será repetido até o jogador descobrir todos os campos sem bombas ou até o número de jogadas chegar ao fim. Caso o jogador encontre uma bomba o jogo acaba.

    # Campo Minado com socket

    - Abra o terminal na pasta campo_minado_socket
    Caso a pasta esteja em documentos rode o seguinte comando no terminal/prompt: 
    
    cd documents/campo_minado_socket

    - Estando dentro da pasta, para rodar o jogo, basta executar o comando:
        Python campo_minado_servidor.py
    
    - Abra outro terminal e vá até pasta do jogo. Estando com terminal rodando dentro da pasta,
    execute o seguinte comando: Python campo_minado_cliente.py

    Nesse outro modelo de campo minado o cliente passa as informações para o servidor. O servidor executa as opereções necessárias e repassa uma resposta ao cliente. O cliente atualiza o campo minado e fica a espera do proximo comando do jogador.

    Selecione 1 para jogar

    Selecione 2 para continuar um jogo(Essa opção so aparecerá caso exista um jogo salvo)

    Selecione 3 para sair

    Ao selecionar a opçao 1 sera pedido o número de linhas e colunas do campo minado,
    passe o valor desejado. Após isso, será exibido o campo minaod e solicitado ao jogador a linha e coluna para começar a partida. O processo será repetido até o jogador descobrir todos os campos sem bombas ou até o número de jogadas chegar ao fim. Caso o jogador encontre uma bomba o jogo acaba.

 
