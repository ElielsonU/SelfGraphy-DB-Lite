import psycopg2

DB_NAME = "selfgraphy"
USER = "postgres"
PASSWORD = ""
HOST = "localhost"
PORT = "5432"

# coloquem as tabela aqui dentro, dentro de string.
# aqui está um exemplo de como criar a tabela
tables = [
  """
    create table User (
      serial int not null primary key,
      username varchar(100) not null,
      fullname varchar(360) not null,
      email varchar(120),
      password text not null,
      photo varchar(500)
    );
  """,
  
]

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
