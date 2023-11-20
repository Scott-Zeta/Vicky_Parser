import json
import re

def stringfy(jsonData):
    # Stringfy the json data back to raw original table
    s:str = json.dumps(jsonData, indent=4)
    # Need additional Stringfy Implementation
    
    # put all elements in array in one line, and replace comma with space
    arrayRegex = r'\[\s+([^]]+?)\s+\]'
    s = re.sub(arrayRegex, lambda m: '[' + m.group(1).replace('\n', '').replace('  ', '') + ']', s)
    s = s.replace('","', '" "')
    
    # restore the duplicate key name
    keyRegex = re.compile(r'("\s*\w+)(_Dup\d+)(\s*"\s*:)')
    s = keyRegex.sub(r'\1\3',s)
    
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
    lines[-1] = '\n'
    s = '\n'.join(lines[2:])
    
    # log out for debug
    with open('debugOutput/stringfy.txt', 'w') as f:
        f.write(s)
    return s
