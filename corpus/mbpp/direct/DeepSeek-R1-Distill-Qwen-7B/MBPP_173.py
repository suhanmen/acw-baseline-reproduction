def remove_splchar(s):
    import re
    return re.sub(r'[^a-zA-Z0-9]', '', s)