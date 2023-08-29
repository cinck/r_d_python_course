FROM python:3.11

WORKDIR /flask

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4200
