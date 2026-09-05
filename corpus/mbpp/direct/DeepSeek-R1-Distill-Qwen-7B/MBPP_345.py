def diff_consecutivenums(lst):
    return [lst[i+1] - lst[i] for i in range(len(lst)-1)]