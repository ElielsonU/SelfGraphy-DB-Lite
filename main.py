import psycopg2

DB_NAME = "selfgraphy"
USER = "postgres"
PASSWORD = ""
HOST = "localhost"
PORT = "5432"

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT
)

cursor = conn.cursor()

def create_table(sql: str):
  cursor.execute(sql)
  conn.commit()

if __name__ == "__main__":
  create_table()
  pass
