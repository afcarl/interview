FROM nginx:latest
MAINTAINER AJ Bowen <aj@soulshake.net>
RUN apt-get update && apt-get install -y \
    nginx \
    vim \
    curl
RUN rm /etc/nginx/conf.d/default.conf
COPY 2.conf /etc/nginx/conf.d/django.conf
