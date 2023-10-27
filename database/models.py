from . import get_cursor

tables = [
  """
    create table if not exists Users (
      id serial not null primary key,
      username varchar(100) not null,
      fullname varchar(360) not null,
      email varchar(120),
      password text not null,
      photo text
    );
  """,
  """
    create table if not exists Documents (
      id serial not null primary key,
      file varchar(500) not null,
      created date not null,
      user_id integer not null,
      foreign key (user_id) references Users(id)
    )
  """,
  """
    create table if not exists Wallets (
      id serial not null primary key,
      credits integer,
      spent float,
      user_id integer not null,
      foreign key (user_id) references Users(id)
    )
  """,
  """
    create table if not exists Transactions (
      id serial not null primary key,
      credits integer,
      spent float,
      wallet_id integer not null,
      foreign key (wallet_id) references Wallets(id)
    )
  """,
  """
    create table if not exists Sketchs (
      id serial not null primary key,
      file varchar(500) not null,
      created date not null,
      user_id integer not null,
      foreign key (user_id) references Users(id) 
    );
  """,
  """
    create table if not exists Topics (
      id serial not null primary key,
      title varchar(80) not null,
      sketch_id integer not null,
      FOREIGN KEY (sketch_id) references Sketchs(id) 
    );
  """,
  """
    create table if not exists Images (
      id serial not null primary key,
      title varchar(80),
      description varchar(200),
      topic_id integer not null,
      foreign key (topic_id) references Topics(id)
    );

  """,
  """
    create table if not exists Subtopics (
      id serial not null primary key,
      title varchar(500),
      questions varchar(500),
      topic_id integer not null,
      foreign key(topic_id) references Topics(id)
    );
  """
]

def create_tables():
  with get_cursor() as cursor:
    for table in tables:
      cursor.execute(table)