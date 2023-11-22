from tokenizer import tokenizer
def token_parser(tokens):
    def process_block(token_iter):
        block = []
        key = None
        
        for token in token_iter:
            if token == '=' or token == ':':
                continue
            if token == '{':
                value = process_block(token_iter)
                if key is not None:
                    block.append({key: value})
                    key = None
            elif token == '}':
                return block
            elif key is None:
                key = token
                # check the next token is operator or not
                # if not, it is a value inside the list
            else:
                block.append({key:token})
                key = None
        return block 
    return process_block(iter(tokens))
def main():
    with open("./vanilla_resource/13_australasia.txt", "r", encoding='utf-8-sig') as f:
        tokens = tokenizer(f)
        data = token_parser(tokens)
        print(data)
if __name__ == "__main__":
    main()