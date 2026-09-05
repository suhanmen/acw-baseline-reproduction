def sum_of_alternates(t):
    sum_even = 0
    sum_odd = 0
    for i, num in enumerate(t):
        if i % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    return (sum_odd, sum_even)