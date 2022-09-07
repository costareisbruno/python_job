from multiprocessing.connection import Connection
import re
import psycopg2
import csv

import psycopg2 as db

class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                    "user": "repassa",
                    "password": "[5Xl%lbw[M@C.jK}2wgd",
                    "host": "10.174.2.7",
                    "port": "5432",
                    "database": "repassa"


                }
            }   

class Connection(Config):
        def __init__(self):
             Config.__init__(self)
             try:
                self.conn = db.connect(**self.config["postgres"])
                self.cur = self.conn.cursor()
             except Exception as e:
                print("Error na conexão", e)
                exit(1)

        def __enter__(self):
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.commit()
            self.connection.close()
            

        @property
        def connection(self):
            return self.conn

        @property
        def cursor(self):
            return self.cur
        
        def commit(self):
            self.connection.commit()

        def fetchall(self):
            return self.cursor.fetchall()

        def execute(self, sql, params=None):
            self.cursor.execute(sql, params or ())

        def query(self, sql, params=None):
            self.cursor.execute(sql, params or ())
            return self.fetchall()
        

class Person(Connection):
    def __init__(self):
        Connection.__init__(self)
    
    def insert(self, *args):
        try: 
            sql = "INSERT INTO table1 (name,email) VALUES (%s,%s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Error ao inserir", e)

if __name__ == "__main__":
        person = Person()
        person.insert("REPASSA","teste@repassa.com.br")
        person.insert("REPASSA","teste@repassa.com.br")
        person.insert("REPASSA","teste@repassa.com.br")
        person.insert("REPASSA","teste@repassa.com.br")

        