import json
from token_parser import getData

def main():
        s = json.dumps(getData('./vanilla_resource/10_india.txt'), indent=4)
        # print(s)
        with open("./out.txt", "w", encoding='utf-8-sig') as f:
            f.write(s)
if __name__ == "__main__":
    main()