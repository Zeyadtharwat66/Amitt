def is_vow(inp):
    for i in range(len(inp)):
        if chr(inp[i]).lower() in 'aeiou':
            inp[i]=chr(inp[i]).lower()
    return inp
print(is_vow([118,120,121,98,122,120,106,104,116,113,114,113,120,106]))
