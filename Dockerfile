FROM python:3.9

# Instala gettext
RUN apt-get update && apt-get install -y gettext

WORKDIR /app
COPY requirements.txt /app
RUN pip install pip --upgrade && \
    pip install -r requirements.txt
COPY . .
