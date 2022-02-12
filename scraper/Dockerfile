FROM python:3.10.2-slim-buster

# WORKDIR /home/app/
# ADD ./ /home/app/
ADD ./scraper/ /home/scraper/
ADD ./app/ /home/app/

WORKDIR /home/scraper/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip3 install -r requirements.txt

WORKDIR /home/
ENTRYPOINT ["python3", "scraper/app.py"]
