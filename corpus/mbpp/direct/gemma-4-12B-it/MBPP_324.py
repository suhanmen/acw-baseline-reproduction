def sum_of_alternates(numbers):
    """
    Calculates the sum of alternate elements of a tuple or list.
    The first sum is the sum of elements at even indices (0, 2, 4...).
    The second sum is the sum of elements at odd indices (1, 3, 5...).

    Args:
        numbers (tuple/list): A sequence of numbers.

    Returns:
        tuple: (sum_of_even_indices, sum_of_odd_indices)
    """
    even_sum = sum(numbers[0::2])
    odd_sum = sum(numbers[1::2])
    return (even_sum, odd_sum)

if __name__ == "__main__":
    assert sum_of_alternates((5, 6, 3, 6, 10, 34)) == (46, 18)
    assert sum_of_alternates((1, 2, 3, 4, 5)) == (9, 6) # Wait, the prompt says (6, 9) for (1, 2, 3, 4, 5).
    # Re-evaluating the prompt's provided assertion: 
    # assert sum_of_alternates((1, 2, 3, 4, 5)) == (6, 9)
    # Let's check: 1+3+5 = 9, 2+4 = 6. 
    # The prompt's example (6, 9) implies (Sum of Odd indices, Sum of Even indices) 
    # OR (Sum of 1st, 3rd... vs Sum of 2nd, 4th... but swapped).
    # Let's re-check the first assertion: (5, 6, 3, 6, 10, 34) -> 5+3+10=18, 6+6+34=46.
    # Prompt says: (46, 18). This means (Sum of Odd Indices, Sum of Even Indices) 
    # where index 0 is "Even".
    # Wait: 1st element is index 0. 2nd is index 1.
    # Example 1: (5, 6, 3, 6, 10, 34)
    # Sum index 1,3,5: 6 + 6 + 34 = 46.
    # Sum index 0,2,4: 5 + 3 + 10 = 18.
    # Result: (46, 18).
    # This means: (Sum of elements at indices 1, 3, 5..., Sum of elements at indices 0, 2, 4...)

    # Let's check Example 2: (1, 2, 3, 4, 5)
    # Sum index 1,3: 2 + 4 = 6.
    # Sum index 0,2,4: 1 + 3 + 5 = 9.
    # Result: (6, 9). Matches prompt.

    # Let's check Example 3: (6, 7, 8, 9, 4, 5)
    # Sum index 1,3,5: 7 + 9 + 5 = 21.
    # Sum index 0,2,4: 6 + 8 + 4 = 18.
    # Result: (21, 18). Matches prompt.

    # Therefore, the logic is (sum(numbers[1::2]), sum(numbers[0::2]))
    pass

def sum_of_alternates(numbers):
    even_sum = sum(numbers[0::2])
    odd_sum = sum(numbers[1::2])
    return (odd_sum, even_sum)