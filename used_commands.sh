#!/bin/bash

sudo docker run --name redis --rm -d -p6379:6379 -v /redis_data:/data redis
sudo dodcker images
sudo docker ps -a
sudo docker rm flask_app
sudo docker rmi flask_redis_api
sudo docker build . -t my_app:v1

sudo docker-compose -f flask_redis_compose_file.yaml up
