FROM python:3.8-slim

# Install apt dependencies
RUN apt update

# Install requirements

# RUN pip install socket

COPY . /home


WORKDIR /
ENTRYPOINT python /home/wordHelper.py