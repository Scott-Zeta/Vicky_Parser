from table_parser import *

def main():
    # Read the raw original table and parse to json data
    content = read_table("./vanilla_resource/13_australasia.txt")
    jsonData = modify_for_json(content)
    print(jsonData)

    # Stringfy the json data back to raw original table
    s = json.dumps(jsonData, indent=4)
    # Need additional Stringfy Implementation
    print(s)
    with open('stringfy.txt', 'w') as f:
        f.write(s)
if __name__ == "__main__":
    main()