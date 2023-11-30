from pathlib import Path
from dirIterator import FileIterator
from token_parser import getData
import json
import re

historical_path = Path('./historical_resource')
vanilla_path = Path('./vanilla_resource')
output_path = Path('./Output/map_data/state_regions')


def stringfy(s):
    # put all elements in array in one line, and replace comma with space
    arrayRegex = r'\[\s+([^]]+?)\s+\]'
    s = re.sub(arrayRegex, lambda m: '[' + m.group(1).replace('\n', '').replace('  ', '') + ']', s)
    
    #unquote the key
    s = s.replace('"','')
    s = s.replace("'",'"')
    
    # replace [] with {}
    s = s.replace('[','{ ').replace(']',' }')
    
    # replace all : with =
    s = s.replace(':',' =')
    
    # remove all , 
    s = s.replace('","', '" "')
    s = s.replace(',','')
    
    # indentation move left
    s = re.sub(r'^\s{4}', '', s, flags=re.MULTILINE)

    # add a new line each element
    s = re.sub(r'^(?!\s|\}$|\{$)', '\n', s, flags=re.MULTILINE)
    
    # remove root level {}, re construct the string
    lines = s.strip().split('\n')
    lines[-1] = ''
    s = '\n'.join(lines[2:])
    
    return s

def main():
    vanilla_Iterator = FileIterator(vanilla_path, ['.txt'])
    historical_Iterator = FileIterator(historical_path, ['.txt'])
    vanilla_data = vanilla_Iterator.iterate_files(getData)
    historical_data = historical_Iterator.iterate_files(getData)
    for k,v in vanilla_data.items():
        file_path = output_path / f"{k}"
        with file_path.open('w') as file:
            s = stringfy(json.dumps(v, indent=4))
            file.write(s)
          
if __name__ == "__main__":
    main()