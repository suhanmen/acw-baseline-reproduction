def find_even_Pair(lst):
    # Count the number of even and odd numbers
    even_count = 0
    odd_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Calculate the number of even pairs and odd pairs
    even_pairs = (even_count * (even_count - 1)) // 2
    odd_pairs = (odd_count * (odd_count - 1)) // 2

    # Total pairs is the sum of even_pairs and odd_pairs
    total_pairs = even_pairs + odd_pairs

    return total_pairs