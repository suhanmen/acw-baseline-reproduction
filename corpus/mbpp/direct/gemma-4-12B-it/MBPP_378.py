def move_first(lst):
    if not lst:
        return lst
    return [lst[-1]] + lst[:-1]

if __name__ == "__main__":
    assert move_first([1,2,3,4]) == [4,1,2,3]
    assert move_first([0,1,2,3]) == [3,0,1,2]
    assert move_first([9,8,7,1]) == [1,9,8,7]