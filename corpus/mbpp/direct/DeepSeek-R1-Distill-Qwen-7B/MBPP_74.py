def is_samepatterns(patterns, given):
    if len(patterns) != len(given):
        return False
    for p, g in zip(patterns, given):
        if isinstance(p, str) != isinstance(g, str):
            return False
        if isinstance(p, str):
            if len(p) != len(g):
                return False
        else:
            if p != g:
                return False
    return True

# Example usage:
assert is_samepatterns(["red","green","green"], ["a", "b", "b"]) == True 
assert is_samepatterns(["red","green","greenn"], ["a","b","b"]) == False 
assert is_samepatterns(["red","green","greenn"], ["a","b"]) == False