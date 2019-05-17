FROM python:3.6-alpine as builder

RUN apk --no-cache --update-cache add \
    gcc \
    gfortran \
    py-pip \
    build-base \
    wget \
    freetype-dev \
    libpng-dev \
    openblas-dev \
    libffi-dev \
    openssl-dev

COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt && rm -rf /root/.cache

COPY . /app
WORKDIR /app

CMD python3 app.py