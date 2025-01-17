#Project:
#Create a script that reads a JSON file and prints out specific values based on user input.


import json

def print_json_values(filename, keys):
  """
  Reads a JSON file and prints out the values associated with the given keys.

  Args:
    filename: The path to the JSON file.
    keys: A list of keys to look for in the JSON data.
  """

  try:
    with open(filename, 'r') as f:
      data = json.load(f)

    for key in keys:
      try:
        value = data[key]
        print(f"{key}: {value}")
      except KeyError:
        print(f"{key}: Key not found in the JSON file.")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
  filename = input("Enter the path to the JSON file: ")
  keys = input("Enter the keys to retrieve (comma-separated): ").split(",")
  print_json_values(filename, keys)