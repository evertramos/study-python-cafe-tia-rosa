# Dockerfile
FROM python:3.13-alpine3.22

# Evita interação nos pacotes
ENV DEBIAN_FRONTEND=noninteractive

# Fixa a pasta de trabalho
WORKDIR /usr/src/app

# Copia os arquivos de requisitos
COPY ./src/requirements.txt ./

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY ./src .

# Define o comando padrão para executar a aplicação
CMD ["python", "./main.py"]