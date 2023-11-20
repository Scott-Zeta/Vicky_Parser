import re
import json

# this custmized jsonDecoder will handle the duplicate key, typically is resource
def rename_duplicates(ordered_pairs):
    d = {}
    for k, v in ordered_pairs:
        if k in d:
            # Rename key if duplicate
            count = 1
            new_key = f"{k}_Dup{count}"
            while new_key in d:
                count += 1
                new_key = f"{k}_Dup{count}"
            k = new_key
        # Recursively process nested dictionaries
        if isinstance(v, dict):
            v = rename_duplicates(v.items())
        d[k] = v
    return d

class CustomJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, object_pairs_hook=rename_duplicates, **kwargs)


def read_table(filename):
   with open(filename, "r",encoding='utf-8-sig') as f:
       content:str = f.read()
       return content

def modify_for_json(content:str):
    linesArr = []
    lines = content.splitlines()
    arrayRegex = re.compile(r'\{.*?\}')
    keyRegex = re.compile(r'^\s*([\w]+)\s*=', re.MULTILINE)
    for i in range(len(lines)):
        line = lines[i].rstrip()
        
        # convert array to json array
        if arrayRegex.search(line):
            # this line deal with some customized array
            line = line.replace('state_trait_new_world','"state_trait_new_world"')
            line = line.replace("{","[").replace("}","]")
            line = line.replace('" "', '", "')
        
        # convert key to json key
        key = keyRegex.findall(line)
        if key:
            line = line.replace(key[0],'"' + key[0] + '"')
        
        # add comma to the end of element except the last one
        is_last_in_block = i + 1 < len(lines) and i + 2 < len(lines) and lines[i + 1].strip() != '}'
        if line and not line.endswith("{") and is_last_in_block:
            line += ','
        
        # replace = with :
        line = line.replace("=",":")
        linesArr.append(line)
    linesArr.insert(0,"{")
    linesArr.append("}")
    jsonfiedString = "\n".join(linesArr)
    
    # log out the jsonfiedString for debug
    with open('debugOutput/jsonfy.txt', 'w') as f:
        f.write(jsonfiedString)
        
    jsonData = json.loads(jsonfiedString,cls=CustomJSONDecoder)    
    return jsonData

def getJsonData(filepath:str):
    content = read_table(filepath)
    jsonData = modify_for_json(content)
    return jsonData