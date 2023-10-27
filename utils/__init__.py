from datetime import date

def get_table_fields(it: int, value, length: int, insertion: bool = False):
  if insertion: value = f"'{value}'" if type(value) == str else value
  if (it == 0): return f"( {value}, "
  if (it < (length - 1)): return f"{value}, "
  return f"{value} )"

def iterate_table_fields(params: dict):
  fields_tuple = ["", ""]
  for [it, values, keys] in zip(range(len(params)), params.values(), params.keys()): 
    fields_tuple[0] += get_table_fields(it, keys, len(params))
    fields_tuple[1] += get_table_fields(it, values, len(params), True)
  return fields_tuple

def get_typed_input(row: str, table: dict):
  input_type = type(table[row])
  required = table[row]
  input_text = row + f"{'*' if required else ''}: "
  try: table[row] = input_type(input(input_text))
  except: raise ValueError()
  if (not table[row] and required): raise ValueError()
  if input_type == str: return f"'{table[row]}'"
  return table[row]