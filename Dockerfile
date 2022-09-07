FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt
RUN pip3 install psycopg2==2.7.6
RUN mkdir app
COPY replica.py app/replica.py

WORKDIR app

ENTRYPOINT ["python3", "replica.py"]
