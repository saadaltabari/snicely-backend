FROM python:3.7-alpine

MAINTAINER Saad Altabari

RUN apk --update add \
    build-base \
    mariadb-dev

ENV PYTHONUNBUFFERED 1

ENV FLASK_APP=app.py

ARG FLASK_ENV_ARG=development
ENV FLASK_ENV=$FLASK_ENV_ARG

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app

COPY ./app /app
WORKDIR /app
