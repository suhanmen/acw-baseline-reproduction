def all_unique(lst):
    seen = set()
    for num in lst:
        if num in seen:
            return False
        seen.add(num)
    return True

# Example usage:
# assert all_unique([1,2,3]) == True
# assert all_unique([1,2,1,2]) == False
# assert all_unique([1,2,3,4,5]) == True