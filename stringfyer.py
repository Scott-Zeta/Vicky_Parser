from table_parser import *
import re

def stringfy(jsonData):
    # Stringfy the json data back to raw original table
    s = json.dumps(jsonData, indent=4)
    # Need additional Stringfy Implementation
    
    # put all elements in array in one line, and replace comma with space
    arrayRegex = r'\[\s+([^]]+?)\s+\]'
    s = re.sub(arrayRegex, lambda m: '[' + m.group(1).replace('\n', '').replace('  ', '') + ']', s)
    s = s.replace('","', '" "')
    
    # unquote the key
    keyRegex = re.compile(r'"\s*([\w]+)\s*"\s*:')
    s = keyRegex.sub(r'\1 :',s)
    
    # replace [] with {}
    s = s.replace('[','{ ').replace(']',' }')
    
    # replace all : with =
    s = s.replace(':','=')
    
    # remove all , 
    s = s.replace(',','')
    

    
    # indentation move left
    s = re.sub(r'^\s{4}', '', s, flags=re.MULTILINE)

    # add a new line each element
    s = re.sub(r'^(?!\s|\}$|\{$)', '\n', s, flags=re.MULTILINE)
    
    # remove root level {}, re construct the string
    lines = s.strip().split('\n')
    s = '\n'.join(lines[2:-1])
    
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