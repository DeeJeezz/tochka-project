FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/tochka-api

RUN apk update && apk add python3-dev postgresql-dev gcc musl-dev libffi-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh .
ENTRYPOINT [ "sh", "./entrypoint.sh" ]