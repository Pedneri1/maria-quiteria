FROM python:3.8-buster

WORKDIR /mnt/scraper

COPY dev_requirements.txt dev_requirements.txt
COPY requirements.txt requirements.txt

RUN adduser --system -u ${LOCAL_USER_ID:-1000} scraper \
    && apt-get update \
	&& apt-get -y install poppler-utils postgresql-client wait-for-it default-jre \
	&& pip install --no-cache-dir -r dev_requirements.txt

USER scraper
