import psycopg2

DB_NAME = "selfgraphy"
USER = "postgres"
PASSWORD = ""
HOST = "localhost"
PORT = "5432"

tables = [
  """
    create table User (
      id serial not null primary key,
      username varchar(100) not null,
      fullname varchar(360) not null,
      email varchar(120),
      password text not null,
      photo text
    );
  """,
  """
    create table Document (
      id serial not null primary key,
      file varchar(500) not null,
      created date not null,
      integer user_id not null,
      foreign key (user_id) references User(id)
    )
  """,
  """
    create table Wallet (
      id serial not null primary key,
      credits integer,
      spent float,
      integer user_id not null,
      foreign key (user_id) references User(id)
    )
  """,
  """
    create table Transaction (
      id serial not null primary key,
      credits integer,
      spent float,
      integer wallet_id not null,
      foreign key (wallet_id) references Wallet(id)
    )
  """,
  """
    create table Sketch (
      id serial not null primary key,
      file varchar(500) not null,
      crated date not null,
      user_id integer,
      foreign key (user_id) references User(id) 
    );
  """,
  """
    create table Topic (
      id serial not null primary key,
      title varchar(80) not null,
      sketch_id integer,
      FOREIGN KEY (sketch_id) references Sketch(id) 
    );
  """,
  """
    create table Images (
      id serial not null primary key,
      title varchar(80),
      description varchar(200),
      topic_id integer,
      foreign key(topic_id) references Topic(topic_id)
    );

  """,
  """
    create table Subtopics (
      id serial not null primary key,
      title varchar(500),
      questions varchar(500),
      topic_id integer,
      foreign key(topic_id) references Topic(topic_id)
    );
  """
]

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT
)


def create_table(sql: str):
  cursor = conn.cursor()
  cursor.execute(sql)
  conn.commit()
  cursor.close()

if __name__ == "__main__":
  for table in tables:
    create_table(table)
