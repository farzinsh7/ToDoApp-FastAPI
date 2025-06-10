FROM python:3.13-slim-bullseye

LABEL maintainer="farzinnater@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY ./requirements.txt .


RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./core .