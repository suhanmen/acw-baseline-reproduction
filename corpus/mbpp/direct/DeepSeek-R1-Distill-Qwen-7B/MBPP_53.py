def check_Equality(s):
    if len(s) < 2:
        return "Not Equal"
    if s[0] == s[-1]:
        return "Equal"
    else:
        return "Not Equal"