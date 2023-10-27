from database import save, exit
from database.models import create_tables
from database.queries import insert_into_table, get_all_tables, update_table_row_by_id, remove_row_by_id, get_all_table_instances

if __name__ == "__main__":
  create_tables()
  choiced = 1
  options = [get_all_tables, get_all_table_instances, insert_into_table, update_table_row_by_id, remove_row_by_id, save]

  print("Wellcome!\n\nLet's start managing your database!")
  while choiced >= 0 and choiced < len(options):
    print("Choice an option:\n1- get all tables name\n2- get all table instances\n3- add row into a table\n4- update a table value by id\n5- remove and table by id\n6- save your changes\nanything else - exit")
    try: 
      choiced = (int(input("R: ")) - 1)
      options[choiced]()
    except: break
    if (choiced == -1): break
  print("\nGoodbye! :D")
  exit()
  pass