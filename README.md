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



