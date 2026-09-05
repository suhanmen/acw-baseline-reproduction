def remove(lst):
    return [re.sub(r'\d+', '', s) for s in lst]