FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# RUN apk add --no-cache --virtual .tmp gcc libc-dev linux-headers 

RUN pip install pip --upgrade
RUN pip install -r /requirements.txt

# RUN apk del .tmp

RUN mkdir /src
COPY ./src /src
WORKDIR /src

# RUN adduser -D user
# USER user





