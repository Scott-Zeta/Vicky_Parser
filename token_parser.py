from tokenizer import tokenizer
def token_parser(tokens):
    print(tokens)
    return
def main():
    with open("./vanilla_resource/13_australasia.txt", "r", encoding='utf-8-sig') as f:
        tokens = tokenizer(f)
        token_parser(tokens)
if __name__ == "__main__":
    main()