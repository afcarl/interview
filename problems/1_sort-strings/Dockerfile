FROM python:latest
MAINTAINER AJ Bowen <aj@soulshake.net>

COPY . /src

# Place input.txt in the same directory as this Dockerfile, then re-build
copy input.txt /input.txt

ENTRYPOINT ["python", "/src/sort.py", "/input.txt"]
