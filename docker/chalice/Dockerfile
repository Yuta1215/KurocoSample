FROM python:3.9.13-alpine3.16
WORKDIR /work
COPY ./ /work
RUN apk add --no-cache --virtual build-deps build-base gcc && \
    apk del build-deps && \
    pip install -r requirements-dev.txt && \
    pip install -r requirements.txt
