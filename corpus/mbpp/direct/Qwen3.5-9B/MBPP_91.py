def find_substring(lst, substring):
    for item in lst:
        if substring in item:
            return True
    return False