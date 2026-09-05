def max_aggregate(tuples):
    max_name = None
    max_value = -1
    for name, value in tuples:
        if value > max_value:
            max_value = value
            max_name = name
    return (max_name, max_value)

# Example usage and assertions
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]) == ('Juan Whelan', 212)
assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)]) == ('Juan Wheland', 72)
assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)]) == ('Sabah Colley', 70)