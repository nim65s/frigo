# Frigo

[![Build Status](https://travis-ci.org/nim65s/frigo.svg?branch=master)](https://travis-ci.org/nim65s/frigo)
[![Coverage Status](https://coveralls.io/repos/github/nim65s/frigo/badge.svg?branch=master)](https://coveralls.io/github/nim65s/frigo?branch=master)

An App for your fridge !

## Reverse Proxy

Look at my Traefik easy setup for [dev](https://github.com/nim65s/traefik-dev) and
[prod](https://github.com/nim65s/traefik-prod)

## Configuration example

```bash
echo POSTGRES_PASSWORD=$(openssl rand -base64 32) >> .env
echo SECRET_KEY=$(openssl rand -base64 32) >> .env
echo EMAIL_USER=$YOUR_SMTP_USERNAME >> .env
echo EMAIL_HOST_PASSWORD=$YOUR_SMTP_PASSWORD >> .env
echo DOMAIN_NAME=$YOUR_FQDN> >> .env  # if prod
```

## Launch

### Dev

`docker-compose up -d --build`

###  Prod

`docker-compose up -d --pull`

## Create super user

`docker-compose exec app ./manage.py createsuperuser`
