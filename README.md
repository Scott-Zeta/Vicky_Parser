# Vicky_Reigons

## Notes

```
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
```

A typical case that a parser start: identify quote or unquote. If its quoted case, anything inside is a single token. If not, they will have different meanings.

Worked, but my patient is near end. Not sure will continue
