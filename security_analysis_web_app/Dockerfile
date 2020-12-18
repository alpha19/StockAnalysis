FROM python:3.7-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /security_analysis_web_app
WORKDIR /security_analysis_web_app

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev libxslt-dev libxml2-dev linux-headers g++

RUN pip install --upgrade pip
COPY requirements.txt /security_analysis_web_app/
RUN pip install -r requirements.txt

COPY entrypoint.sh /security_analysis_web_app/
COPY . .

ENTRYPOINT ["/security_analysis_web_app/entrypoint.sh"]