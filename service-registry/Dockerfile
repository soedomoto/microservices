# Viadeo - Consul Server mimic
#
#
FROM ubuntu:xenial
MAINTAINER "Soedomoto <soedomoto@gmail.com>"


## Base
## --
RUN apt-get update
RUN apt-get install -y\
 unzip \
 curl \
 supervisor

COPY supervisor/supervisord.conf /etc/supervisor/supervisord.conf

EXPOSE 9001


## Consul
## --
## Dir Layout
ENV CONSUL_HOME /opt/consul
RUN mkdir -p ${CONSUL_HOME}/conf \
  && mkdir -p ${CONSUL_HOME}/data \
  && mkdir -p ${CONSUL_HOME}/logs

## Binary
ENV CONSUL_VERSION 0.8.3
ENV CONSUL_SHA256 171cf4074bfca3b1e46112105738985783f19c47f4408377241b868affa9d445

RUN curl \
  --insecure \
  --location \
  https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip \
  > /tmp/consul.zip

RUN cd /bin \
 && unzip /tmp/consul.zip \
 && chmod +x /bin/consul \
 && rm /tmp/consul.zip

EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp

## Consul - Conf
COPY consul/* ${CONSUL_HOME}/conf/
COPY supervisor/conf.d/* /etc/supervisor/conf.d/


## Service
## --
# CMD ["supervisord", "-n"]


