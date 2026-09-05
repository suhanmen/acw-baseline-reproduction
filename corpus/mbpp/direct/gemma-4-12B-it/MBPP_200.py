def position_max(lst):
    if not lst:
        return []

    max_val = max(lst)
    return [i for i, val in enumerate(lst) if val == max_val]

if __name__ == "__main__":
    assert position_max([12,33,23,10,67,89,45,667,23,12,11,10,54])==[7]
    assert position_max([1,2,2,2,4,4,4,5,5,5,5])==[7,8,9,10]
    assert position_max([2,1,5,6,8,3,4,9,10,11,8,12])==[11]