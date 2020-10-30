# ALGORITHM-SERVER
servidor HTTP que, para cada requisição GET, retorna um JSON cuja chave extenso é a versão por extenso do número inteiro enviado no path. Os números podem estar no intervalo [-99999, 99999].

## Exemplos de usos:

 Exemplos de URL possíveis, com suas respectivas respostas esperadas:

- λ curl [http://0.0.0.0:8000/1/) 

```

{ "extenso": "um" }

```

- λ curl [http://0.0.0.0:8000/-1042/)

```

{ "extenso": "menos mil e quarenta e dois" }

```

- λ curl [http://0.0.0.0:8000/94587/)

```

{ "extenso": "noventa e quatro mil e quinhentos e oitenta e sete" }

```



# Construindo o servidor


## Usando Docker

É possível construir o servidor usando Docker. Para [baixar essa ferramenta vá para o site do Docker](https://docs.docker.com/compose/install/). Para construir e rodar o servidor usando essa ferramenta, basta usar os comandos:



```
git clone https://github.com/viniciusnau/ALGORITHM-SERVER.git
cd ALGORITHM-SERVER
cd server
docker-compose up

```

O servidor construido irá estar atendendo pela porta 8000. Nesse caso você conseguirá acessar a API pela URl: 127.0.0.1:8000/ 



# Python 3.6

É possível construir e ligar o servidor apenas usando o Python 3.6. Para instalar as dependências é necessário ter o Python 3.6 instalado no seu computador. Baixe a versão no site do [Python](https://www.python.org/downloads/release/python-369/). Após instalar o Python é necessário instalar as dependências do projeto. Para isso abra um terminal na pasta clonada e digite o comando:

```

python -m pip install -r requirements.txt

```

Após a instalação das bibliotecas necessárias ao projeto é possivel ligar o servidor utilizando o comando, no terminal, digitando:

```

python manage.py runserver

```

O servidor construido irá estar atendendo pela porta 8000. Nesse caso você conseguirá acessar a API pela URl: 127.0.0.1:8000/ 





# Ferramentas usadas no projeto.



O projeto foi testado e construído no Windows 10 e foi escrito através do ambiente de desenvolvimento do Visual Studio Code (VS Code). Esse ambiente de desenvolvimento é mantido pela Microsoft e pode ser usado gratuitamente. O VSCode instalado na minha maquina tinha o [problema](https://stackoverflow.com/questions/52462599/visual-studio-code-python-timeout-waiting-for-debugger-connection). Para isolar a aplicação, gerar um arquivo contendo todas as bibliotecas necessárias ao projeto foi usado a ferramenta [gerador de arquivo pipreqs](https://github.com/bndr/pipreqs). Essa ferramente permitiu gerar o arquivo: "requirements.txt"; necessário para usar o instalador de pacotes do Python (do ingles Package Intaller Python,pip). Para manter o fluxo continuo de atualizações foi desenvolvido testes unitários com a biblioteca Pytest e configurado o ambiente de desenvolvimento do [Travis](httpss://docs.travis-ci.com/user/languages/python/). Uma versão do serviço construído esta hospedado na plataforma [Heroku](www.heroku.com). Dcomentação seguindo estilo do google

[1](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) [2](http://google.github.io/styleguide/pyguide.html).





# Termos e documentação



O projeto tem algumas estruturas de dados que possuem nomes. O:

- vetor explodido é um vetor de números inteiros que contem uma sequência de números que ao realizar a soma dos elementos geram um número Inteiro. Por exemplo, o número 119 é explodido no vetor "[100,10,9]". 



- vetor tratado de números é um vetor que, também em sua soma gera o número inteiro originário, porém, o vetor é organizado para atender as exeções de nomeclatura dos numeros (e.g., numero dezenove). Um vetor trato do número 119 é o vetor: "[100,19]".



O resto da documentação pode ser vista nos módulos, [nas propostas de alterações aprovadas](https://github.com/jmarcolan/desafio_certi/pulls?q=is%3Apr+is%3Aclosed), nas [propostas de melhorias](https://github.com/jmarcolan/desafio_certi/issues) e nos [releases do projeto dentro desse github](https://github.com/jmarcolan/desafio_certi/releases).
