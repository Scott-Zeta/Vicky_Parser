def tokenizer(f):
    lines = f.readlines()
    
    def read_tokens(lines):
        tokens = [""]
        quote_flag = False
        
        def parse_quote(tokens, char, quote_flag):
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
                try:
                    # quote case
                    if char == '"':
                        quote_flag = parse_quote(tokens, char, quote_flag)
                    # other char out of the quote
                    elif not quote_flag:
                        # comment case, drop everything include #
                        if char == '#':
                            break
                        # operator case, add as a new token
                        # operators are always as a single token
                        elif char in ('=', '{', '}', ':'):
                            if tokens[-1]:
                                tokens.append(char)
                                tokens.append("")
                            else:
                                tokens[-1] += char
                                tokens.append("")
                        # space, tab, newline case, 
                        # all count as the end of the current token
                        elif char.isspace():
                            if tokens[-1]:
                                tokens.append("")
                        # other char, add to the current token
                        else:
                            tokens[-1] += char
                    # case inside the quote, add them all
                    else:
                        tokens[-1] += char
                except Exception as e:
                    print(f"Error on char {char} in line {line}")
                    print(f"Current tokens: {tokens}")
                    print(f"Current quote flag: {quote_flag}")
                    print(e)
        # drop all duplicate empty token
        while not tokens[-1]:
            tokens.pop()
        return tokens
    return read_tokens(lines)


def main():
    with open("./vanilla_resource/13_australasia.txt", "r", encoding='utf-8-sig') as f:
        token = tokenizer(f)
        print(token)
    # for k, v in token.items():
    #     print(k)
    # print(token["wealth_1"])
if __name__ == "__main__":
    main()