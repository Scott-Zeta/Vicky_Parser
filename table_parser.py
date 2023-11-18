def read_table(filename):
   with open(filename, "r") as f:
       content = f.read()
       print(content)

def main():
    read_table("./vanilla_resource/13_australasia.txt")
        
if __name__ == "__main__":
    main()