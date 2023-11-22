def tokenizer(f):
    lines = f.readlines()
    
    def read_tokens(lines):
        tokens = [""]
        quote_flag = False
        
        def parse_quto(tokens, char, quote_flag):
            # if no quote flag, and tokens[-1] is not empty,
            # start a new token
            if not quote_flag and tokens[-1]:
                tokens.append("")
            # if this is the start quote, flag on, add it
            # if this is the end quote, flag off, add it
            quote_flag = not quote_flag
            tokens[-1] += char
            return quote_flag
            
        for line in lines:
            for char in line:
                # quote case
                if char == '"':
                    quote_flag = parse_quto(tokens, char, quote_flag)
                # other char out of the quote
                elif not quote_flag:
                    pass
                # case inside the quote, add them all
                else:
                    tokens[-1] += char
                pass
        return tokens
    return


def main():
    with open("./13_australasia.txt", "r", encoding='utf-8-sig') as f:
        token = tokenizer(f)
    # for k, v in token.items():
    #     print(k)
    # print(token["wealth_1"])
if __name__ == "__main__":
    main()