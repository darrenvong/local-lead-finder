# Base image for flask REST api tutorial

FROM python:3.10.2-alpine3.14

ADD requirements.txt /home/app/
WORKDIR /home/app/


RUN apk add postgresql-dev gcc musl-dev && \
    pip3 install -r requirements.txt
