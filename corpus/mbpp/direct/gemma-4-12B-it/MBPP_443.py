def largest_neg(numbers):
    negatives = [x for x in numbers if x < 0]
    return min(negatives) if negatives else None