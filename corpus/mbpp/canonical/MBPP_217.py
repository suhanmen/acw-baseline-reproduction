def first_Repeated_Char(str): 
    h = {}
    for ch in str:
        if ch in h: 
            return ch;
        else: 
            h[ch] = 0
    return '\0'