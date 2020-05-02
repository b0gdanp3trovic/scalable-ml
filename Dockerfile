FROM ubuntu

COPY . /app

WORKDIR /app

RUN apt-get update -y && \
apt-get -y install python3-pip && \
pip3 install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn","-b", "0.0.0.0:8000", "server:app"]
