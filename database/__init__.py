import psycopg2
from .config import config

env = config()

connection = psycopg2.connect(
    dbname=env["db_name"],
    user=env["user"],
    password=env["password"],
    host=env["host"],
    port=env["port"]
)

def get_cursor(): return connection.cursor()

def save(): connection.commit()

def exit():
  save()
  connection.close()