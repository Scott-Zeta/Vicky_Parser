from tokenizer import tokenizer
import json

def token_parser(tokens):
    def process_block(token_list, start_index=0):
        block = []
        key = None
        i = start_index

        while i < len(token_list):
            token = token_list[i]
            i += 1

            if token in ('=', ':'):
                continue
            if token == '{':
                nested_block, i = process_block(token_list, i)
                block.append({key: nested_block})
                key = None
            elif token == '}':
                return block, i
            elif key is None:
                # key = token
                # Peek ahead
                if i < len(token_list) and token_list[i] not in ('{', '=', ':', '}'):
                    # values = [token]
                    block.append(token)
                    while i < len(token_list) and token_list[i] not in ('{', '=', ':', '}'):
                        block.append(token_list[i])
                        i += 1
                    # block.append(values)
                    key = None
                else:
                    key = token
            else:
                block.append({key: token})
                key = None
        return block, i

    token_list = tokens  # Convert iterator to list for easier peeking
    parsed_data, _ = process_block(token_list)
    return parsed_data

def convert_str_to_number(obj):
    if isinstance(obj, dict):
        return {k: convert_str_to_number(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_str_to_number(v) for v in obj]
    elif isinstance(obj, str):
        try:
            return int(obj)
        except ValueError:
            try:
                return float(obj)
            except ValueError:
                return obj
    else:
        return obj
    
def main():
    with open("./research/00_buy_packages.txt", "r", encoding='utf-8-sig') as f:
        tokens = tokenizer(f)
        data = token_parser(tokens)
        data = convert_str_to_number(data)
        json_string = json.dumps(data, indent=4)
        print(json_string)
        with open("./out.txt", "w", encoding='utf-8-sig') as f:
            f.write(json_string)
if __name__ == "__main__":
    main()