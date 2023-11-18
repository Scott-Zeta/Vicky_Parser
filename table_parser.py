def read_table(filename):
   with open(filename, "r") as f:
       content = f.read()
       return content

def modify_for_json(content):
    linesArr = []
    lines = content.splitlines()
    for i in range(len(lines)):
        line = lines[i]
        if line.rstrip() and not line.rstrip().endswith("{") and lines[i+1].rstrip() != '}':
            line += ','
        else:   
            print(lines[i])
        line = line.replace("=",":")
        linesArr.append(line)
    linesArr.insert(0,"{")
    linesArr.append("}")
    newContent = "\n".join(linesArr)
    # print(newContent)
    
def main():
    content = read_table("./vanilla_resource/13_australasia.txt")
    modify_for_json(content)
    
if __name__ == "__main__":
    main()