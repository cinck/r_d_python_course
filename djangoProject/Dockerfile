FROM python:3.11
LABEL authors="alex"

WORKDIR /django

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
