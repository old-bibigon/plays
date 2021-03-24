#FROM python:3.9-alpine
FROM python:3.9-slim

RUN groupadd -r user && useradd -r -g user -m user

WORKDIR /home/user

ADD requirements.txt /home/user
RUN pip install -r requirements.txt

USER user

COPY src web
WORKDIR /home/user/web
