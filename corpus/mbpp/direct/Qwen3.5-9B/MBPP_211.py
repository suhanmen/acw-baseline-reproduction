def count_Num(n):
    """
    Count numbers from 1 to n (inclusive) whose 0th and nth bits are set.
    A number has both its 0th bit and nth bit set if:
      (num & 1) == 1  AND  (num & (1 << n)) != 0
    For n=0, the 0th and nth bits are the same bit, so we count numbers with 0th bit set.
    """
    if n < 0:
        return 0

    # Minimum number that has both 0th and nth bits set is (1 << n) + 1
    min_num = (1 << n) + 1

    # The pattern of numbers with both bits set repeats every (1 << (n + 1))
    cycle = 1 << (n + 1)

    # Count full cycles in range [1, n]
    full_cycles = n // cycle
    count = full_cycles * (1 << n)  # In each cycle, exactly (1 << n) numbers satisfy the condition

    # Remaining part
    remainder = n % cycle
    # The first valid number in a cycle is min_num
    # We need to count how many valid numbers are <= remainder
    if remainder >= min_num:
        # Last possible number in this partial cycle that satisfies condition
        # It must be of form: min_num + k * (1 << n) but within remainder
        # Actually, in one cycle [0, cycle-1], valid numbers are:
        # (1<<n) + 1, (1<<n) + 1 + (1<<n), ... up to less than cycle
        # The step between valid numbers is (1 << n)
        # Number of valid values in [0, remainder] is:
        # floor((remainder - min_num) / (1 << n)) + 1, if remainder >= min_num
        count += (remainder - min_num) // (1 << n) + 1

    return count