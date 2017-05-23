FROM nginx
MAINTAINER "Soedomoto <soedomoto@gmail.com>"

RUN apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y wget unzip

ENV CONSUL_TEMPLATE_VERSION 0.18.3

ADD http://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /tmp/

RUN cd /tmp && \ 
    unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \ 
    mv consul-template /bin/consul-template


RUN mkdir -p /tpl
ADD default.conf.tpl /tpl/

CMD /bin/sh -c "/bin/consul-template -consul-addr=consul:8500 -wait=10s -template=\"/tpl/default.conf.tpl:/etc/nginx/conf.d/default.conf:service nginx restart\""

