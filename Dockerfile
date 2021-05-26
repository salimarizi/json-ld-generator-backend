# syntax=docker/dockerfile:1

FROM python:3.7-slim-buster

ENV LISTEN_PORT=5000
EXPOSE 5000

WORKDIR /app
ADD . /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]
