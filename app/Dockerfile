# Basic flask container

FROM python:3.10.2-slim-buster

WORKDIR /home/app/
ADD ./ /home/app/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip3 install -r requirements.txt


EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
