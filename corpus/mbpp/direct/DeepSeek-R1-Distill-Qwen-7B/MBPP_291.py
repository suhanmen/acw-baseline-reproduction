def count_no_of_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k

    same = [0] * k
    diff = [0] * k

    same[0] = k  # first post with same color
    for i in range(1, k):
        same[i] = 1

    diff[0] = k * (k - 1)
    for i in range(1, k):
        diff[i] = k - 1

    for i in range(2, n):
        new_same = 0
        new_diff = 0

        for j in range(k):
            new_same += diff[j]
            for l in range(k):
                if l != j:
                    new_diff += diff[l] + same[l]

        same = new_same
        diff = new_diff

    return same[0] + same[1] + same[2] + diff[0] + diff[1] + diff[2]