FROM python:3.9.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
RUN apt-get upgrade && apt-get update
RUN apt-get install -y libgdal-dev g++ --no-install-recommends && \
    apt-get clean -y
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000