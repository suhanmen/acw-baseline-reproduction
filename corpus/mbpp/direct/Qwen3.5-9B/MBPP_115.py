def empty_dit(data):
    if isinstance(data, dict):
        return len(data) == 0
    if isinstance(data, list):
        return all(isinstance(item, dict) and len(item) == 0 for item in data)
    return False

assert empty_dit([{},{},{}])==True
assert empty_dit([{1,2},{},{}])==False
assert empty_dit({})==True