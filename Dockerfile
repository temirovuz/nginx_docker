FROM python:3.11-slim-bullseye

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .