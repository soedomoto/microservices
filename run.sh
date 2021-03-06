#! /bin/bash

cd $(dirname $(readlink -f $0))

# Build consul cluster
docker build -t soedomoto/consul-cluster:local service-registry

#Build load balancer
docker build -t soedomoto/load-balancer:local load-balancer

# Build flask app
docker build -t soedomoto/service-account:local app

# Build spring app
mvn -f app-java package
docker build -t soedomoto/service-susenas:local app-java


docker-compose up
