FROM python:alpine3.7

EXPOSE 8000

RUN mkdir /app
WORKDIR /app

ADD requirements.txt manage.py ./

ENV PYTHONPATH=/usr/lib/python3.6/site-packages
RUN apk update -q && apk add -q py3-psycopg2 && pip3 install --no-cache-dir -r requirements.txt

ADD frigo frigo

CMD ./manage.py runserver 0.0.0.0:8000
