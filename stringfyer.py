from table_parser import *
import re

def stringfy(jsonData):
    # Stringfy the json data back to raw original table
    s = json.dumps(jsonData, indent=4)
    # Need additional Stringfy Implementation
    # put all elements in array in one line
    arrayRegex = r'\[\s+([^]]+?)\s+\]'
    s = re.sub(arrayRegex, lambda m: '[' + m.group(1).replace('\n', '').replace('  ', '') + ']', s)
    
    print(s)
    with open('debugOutput/stringfy.txt', 'w') as f:
        f.write(s)

def main():
    # Read the raw original table and parse to json data
    content = read_table("./vanilla_resource/13_australasia.txt")
    jsonData = modify_for_json(content)
    stringfy(jsonData)

if __name__ == "__main__":
    main()