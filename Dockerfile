# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev \
    && apk add jpeg-dev zlib-dev  freetype-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev \
    && apk add build-base

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

RUN addgroup -S app && adduser -S app -G app

# run entrypoint.sh
RUN mkdir -p /usr/src/app/static
RUN mkdir -p /usr/src/app/media
RUN chown -R app:app /usr/src/app/

USER app
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]