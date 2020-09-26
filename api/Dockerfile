###########
# BUILDER #
###########

FROM python:3.8-alpine as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

FROM python:3.8-alpine

ENV HOME=/opt/tochka-api
RUN mkdir -p $HOME

WORKDIR $HOME

RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY . $HOME

ENTRYPOINT ["sh", "entrypoint.sh"]
