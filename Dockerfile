# Usando a imagem do Python 3.10 slim
FROM python:3.10-slim

# Instalando dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    wget \
    curl \
  && rm -rf /var/lib/apt/lists/*

# Instalando o dockerize
RUN curl -sSL https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz | tar -xz -C /usr/local/bin

# Configuração do diretório de trabalho
WORKDIR /code

# Copiando os arquivos de requisitos
COPY requirements.txt /code/

# Instalando as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código-fonte
COPY . /code/

# Comando para iniciar a aplicação
CMD ["bash", "-c", "dockerize -wait tcp://db:3306 -timeout 30s python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
