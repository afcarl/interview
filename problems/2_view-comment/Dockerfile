FROM django:latest
MAINTAINER AJ Bowen <aj@soulshake.net>

RUN pip install \
    Django \
    django-bootstrap-themes \
    django-bootstrap3 \
    djangorestframework \
    django_extensions \
    arrow \
    requests

RUN apt-get update && apt-get install -y \
    curl

COPY . /src
WORKDIR /src/restest

EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
