FROM alpine:edge

EXPOSE 8000

ENV GUNICORN_WORKERS=2 \
    GUNICORN_BACKLOG=4096 \
    GUNICORN_BIND=0.0.0.0:8000

RUN mkdir /app
WORKDIR /app
ADD requirements.txt manage.py gunicorn.conf.py ./

RUN apk update && apk add --no-cache py3-psycopg2 git
RUN pip3 install -U -r requirements.txt
ADD frigo frigo

CMD gunicorn --config gunicorn.conf.py frigo.wsgi
