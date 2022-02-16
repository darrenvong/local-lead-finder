FROM python:3.10.2-slim-buster

WORKDIR /home/app/
ADD ./app /home/app/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip3 install -r requirements.txt

CMD ["python3", "scraper.py"]