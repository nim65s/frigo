FROM alpine:edge

EXPOSE 8000
ENV WORKERS=3

RUN mkdir /app
WORKDIR /app
ADD requirements.txt manage.py ./

RUN apk update && \
    apk add --no-cache py3-psycopg2 && \
    apk add --no-cache --virtual .build-deps git && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

ADD frigo frigo

CMD gunicorn \
    --bind 0.0.0.0:8000 \
    --workers ${WORKERS} \
    frigo.wsgi
