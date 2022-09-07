FROM ubuntu:latest

RUN apt install pip3
RUN pip3 install psycopg2
RUN mkdir app
COPY replica.py app/replica.py

WORKDIR app

ENTRYPOINT ["python3", "replica.py"]
