# Frigo

[![Build Status](https://travis-ci.org/nim65s/frigo.svg?branch=master)](https://travis-ci.org/nim65s/frigo)
[![Coverage Status](https://coveralls.io/repos/github/nim65s/frigo/badge.svg?branch=master)](https://coveralls.io/github/nim65s/frigo?branch=master)

An App for your fridge !

## Run

### Configuration

```bash
echo POSTGRES_PASSWORD=$(openssl rand -base64 32) >> .env
echo SECRET_KEY=$(openssl rand -base64 32) >> .env
echo NAMESPACE=$YOUR_FQDN> >> .env
echo EMAIL_USER=$YOUR_SMTP_USERNAME >> .env
echo EMAIL_HOST_PASSWORD=$YOUR_SMTP_PASSWORD >> .env
```

### Launch

```bash
docker-compose pull
docker-compose build
docker-compose up -d
docker exec frigo_app_1 python3 manage.py migrate
docker exec frigo_app_1 python3 manage.py collectstatic --no-input
```

### Devel

```bash
docker build -t nim65s/frigo .
docker-compose up -d
```

### Test

```bash
source .env
coverage run manage.py test
```

### Use

Go to [http://localhost:6500](http://localhost:6500)
