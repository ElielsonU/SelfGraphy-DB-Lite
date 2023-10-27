from datetime import datetime
from . import get_cursor
from utils import iterate_table_fields, get_typed_input

tables = {
  "Users": {
    "id": 1, 
    "username": "required", 
    "fullname": "required",
    "email": "",
    "password": "required",
    "photo": ""
  },
  "Documents": {
    "id": 1, 
    "file": "required", 
    "created": "",
    "user_id": 1,
  },
  "Wallets": {
    "id": 1, 
    "credits": 0, 
    "spent": float(0),
    "user_id": 1,
  },
  "Transactions": {
    "id": 1, 
    "credits": 0, 
    "spent": float(0),
    "wallet_id": 1
  },
  "Sketchs": {
    "id": 1, 
    "file": "required", 
    "created": "",
    "user_id": 1
  },
  "Topics": {
    "id": 1, 
    "title": "required", 
    "stetch_id": 1
  },
  "Images": {
    "id": 1, 
    "title": "required", 
    "decription": "",
    "topic_id": 1,
  },
  "Subtopics": {
    "id": 1, 
    "title": "required", 
    "questions": "", 
    "topic_id": 1,
  },
}

def insert_values(table_copy: dict):
  for row in table_copy.keys(): get_typed_input(row, table_copy)

def insert_into_table():
  tablename = input("Table name: ")
  if (not tables.get(tablename)): return print("This table does not exists")
  with get_cursor() as cursor:
    table_copy = tables[tablename]
    query: str = f"insert into {tablename} "
    try: insert_values(table_copy)
    except: 
      print("Review the types or type something!")
      return
    fields_list: list = iterate_table_fields(table_copy)
    query += fields_list[0] + " values " + fields_list[1]
    cursor.execute(query)
    return query
  
def remove_row_by_id():
  tablename = input("Table name: ")
  if (not tables.get(tablename)): return print("This table does not exists")
  with get_cursor() as cursor:
    id = int(input(f"the {tablename} instace: "))
    query = f"delete from {tablename} where id = {id}"
    cursor.execute(query)

def get_all_tables():
  for [tablename, table] in tables.items():
    print(tablename + ": ")
    for [key, value] in table.items(): print(f"  {key}{'*' if bool(value) else ''}: {type(value).__name__}\n")

def get_all_table_instances():
  tablename = input("\nTable name: ")
  if (not tables.get(tablename)): return print("This table does not exists")
  with get_cursor() as cursor:
    query = f"select * from {tablename}"

    cursor.execute(query)
    for rows in cursor.fetchall():
      for [row, value] in zip(tables[tablename], rows): print(f"   {row}: {value}")
      print()

def update_table_row_by_id():
  with get_cursor() as cursor:
    tablename = input("Table name: ")
    if (not tables.get(tablename)): return print("This table does not exists")
    
    rowname = input("Row name: ")
    if (tables.get(tablename).get(rowname) == None): return print("This row does not exists")
    if (rowname == "id"): return print("Id is constant!")
    
    table_copy = tables[tablename]
    new_value: str
    try: 
      new_value = get_typed_input(rowname, table_copy)
      id = int(input(f"{tablename} entity id: "))
    except: 
      print("Review the types or type something!")
      return
    
    query = f"update {tablename} set {rowname} = {new_value} where id = {id}"
    cursor.execute(query)

def get_tablenames():
  tablenames = []
  for table in tables.keys(): tablenames.append(table)
  return tablenames