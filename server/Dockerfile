FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /algorithm_server

WORKDIR /algorithm_server

ADD . /algorithm_server/

RUN pip install -r requirements.txt