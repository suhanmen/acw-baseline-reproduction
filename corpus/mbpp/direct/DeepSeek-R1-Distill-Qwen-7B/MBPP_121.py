import itertools

def check_triplet(arr, target, a, b, c):
    for triplet in itertools.combinations(arr, 3):
        if triplet[0] == a and triplet[1] == b and triplet[2] == c and sum(triplet) == target:
            return True
    return False