FROM python:3.10.6

ENV PYTHONUNBUFFERED 1 

RUN apt-get update && apt-get install -y \  
    postgresql-client 

RUN mkdir /app 

WORKDIR /app 

COPY requirements.txt /app/ 

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/