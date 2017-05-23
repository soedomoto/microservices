FROM ubuntu:xenial
MAINTAINER "Soedomoto <soedomoto@gmail.com>"

## Base
## --
RUN apt-get update
RUN apt-get install --no-install-recommends -y\
 python python-pip
RUN apt-get clean

## Install requirement
## --
RUN pip install --upgrade --no-cache-dir pip setuptools
RUN pip install --no-cache-dir consulate flask flask-consulate

RUN mkdir -p /app
COPY . /app

EXPOSE 80
