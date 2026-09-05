def get_max_triples(n):
    """
    Calculate the number of valid triples (i, j, k) where i < j < k and a[i] + a[j] + a[k] is divisible by 3.

    Parameters:
        n (int): The length of the array.

    Returns:
        int: The count of valid triples.
    """
    if n < 3:
        return 0

    a = [(i * i - i + 1) % 3 for i in range(1, n + 1)]
    counts = [0, 0, 0]  # Indexes correspond to mod 0, 1, 2

    for num in a:
        counts[num] += 1

    mod_counts = counts.copy()

    # Remove all zeros to avoid forming triples with a zero
    mod_counts[0] = 0
    triple_zero = (mod_counts[0] * (mod_counts[0] - 1) * (mod_counts[0] - 2)) // 6
    if mod_counts[0] < 3:
        triple_zero = 0
    else:
        mod_counts[0] += 3  # Reset to original for further calculations

    # Calculate triples where all are mod 1
    triple_one = (mod_counts[1] * (mod_counts[1] - 1) * (mod_counts[1] - 2)) // 6

    # Calculate triples where all are mod 2
    triple_two = (mod_counts[2] * (mod_counts[2] - 1) * (mod_counts[2] - 2)) // 6

    # Calculate triples where mods are 0,1,2 respectively
    triple_zero_one_two = mod_counts[0] * mod_counts[1] * mod_counts[2]

    total_triples = triple_zero + triple_one + triple_two + triple_zero_one_two

    return total_triples

def mod_count(elements, mod):
    """
    Helper function to count the number of elements in 'elements' that have a remainder of 'mod' when divided by 3.

    Parameters:
        elements (list): The list of numbers.
        mod (int): The target modulo value (0, 1, or 2).

    Returns:
        int: The count of elements with the given modulo.
    """
    count = 0
    for num in elements:
        if num % 3 == mod:
            count += 1
    return count

def count_triples(a):
    """
    Count the number of valid triples (i, j, k) where i < j < k and a[i] + a[j] + a[k] is divisible by 3.

    Parameters:
        a (list): The list of numbers.

    Returns:
        int: The count of valid triples.
    """
    count_mod = [0, 0, 0]
    for num in a:
        count_mod[num % 3] += 1

    # Calculate all zero case
    c0, c1, c2 = count_mod
    total = 0
    if c0 >= 3:
        total += c0 * (c0 - 1) * (c0 - 2) // 6

    # All one case
    if c1 >= 3:
        total += c1 * (c1 - 1) * (c1 - 2) // 6

    # All two case
    if c2 >= 3:
        total += c2 * (c2 - 1) * (c2 - 2) // 6

    # 0,1,2 case
    total += c0 * c1 * c2

    return total

def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    if n < 3:
        return 0

    a = [i * i - i + 1 for i in range(1, n + 1)]
    mod_counts = [0, 0, 0]

    for num in a:
        mod_counts[num % 3] += 1

    return count_triples(mod_counts)