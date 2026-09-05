from typing import List

def tri(n: int) -> List[int]:
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    # Validate input type and value
    if not isinstance(n, int):
        raise TypeError("Input n must be an integer.")
    if n < 0:
        raise ValueError("Input n must be a non-negative integer.")

    # Handle base case: n = 0
    # The sequence is requested as the "first n + 1 numbers".
    # Since the example tri(3) yields [1, 3, 2, 8], the sequence starts at index 0.
    # Note: The logic for tri(1) is given as 3. The index mapping seems to be 0-based
    # but the rules are described using 1-based logic for the formulas.
    # Looking at example tri(3) = [1, 3, 2, 8]:
    # Index 0: 1
    # Index 1: 3  (Matches tri(1) = 3)
    # Index 2: 2  (Matches tri(2) = 1 + 2/2 = 2)
    # Index 3: 8  (Matches tri(3) = tri(2) + tri(1) + tri(4))
    # Looking at tri(4) = 3 (even formula: 1 + 4/2 = 3).

    if n == 0:
        return [1]

    # We need to construct a sequence of length n + 1.
    # Because tri(n) for odd n depends on tri(n + 1), 
    # and tri(n + 1) for even n+1 is independent, 
    # we can compute the values iteratively.

    # Initialize result list with None to reserve space
    # sequence[i] will correspond to tri(i)
    sequence = [None] * (n + 1)

    # Explicit assignment for index 0
    # The problem doesn't define tri(0) explicitly, but tri(3) starts with 1.
    sequence[0] = 1

    # Fill the sequence
    # We must handle indices carefully because tri(odd) depends on tri(even_next).
    # For any even k, tri(k) = 1 + k // 2.
    # For any odd k, tri(k) = tri(k-1) + tri(k-2) + tri(k+1).
    # This means for an odd k, we need k+1 to be calculated first.
    # Since k+1 is even, tri(k+1) can always be calculated independently.

    for i in range(1, n + 1):
        if i % 2 == 0:
            # Rule: tri(n) = 1 + n / 2, if n is even.
            # Note: Using integer division since results are integers.
            sequence[i] = 1 + (i // 2)
        else:
            # Rule: tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
            # For i = n, if n is odd, we need tri(n + 1).
            # If n is the last index, we need to handle tri(n+1) conceptually.
            # However, the problem asks for the first n+1 numbers (indices 0 to n).
            # If n is odd, sequence[n] requires sequence[n+1].
            # But the sequence requested only goes up to n.
            # Let's re-examine tri(3) example:
            # tri(3) = tri(2) + tri(1) + tri(4).
            # tri(4) = 1 + 4/2 = 3.
            # So sequence[3] = sequence[2] + sequence[1] + (1 + (4//2))
            # This means if i is odd and i == n, we calculate tri(i+1) on the fly.

            prev_val = sequence[i - 1]
            prev_prev_val = sequence[i - 2]

            # Calculate tri(i + 1)
            # If i+1 > n, it's still a defined number by the "even" rule.
            next_idx = i + 1
            if next_idx % 2 == 0:
                next_val = 1 + (next_idx // 2)
            else:
                # This part is recursive. But since tri(odd) depends on tri(even),
                # and tri(even) is direct, we only ever need the "even" rule 
                # to resolve any "odd" rule.
                # Wait, tri(even) = 1 + n/2.
                # tri(odd) = tri(odd-1) + tri(odd-2) + tri(odd+1).
                # All terms on the right are even (except potentially tri(odd-2)).
                # This confirms we only need the "even" rule to resolve any "odd" step.
                # But what if i+1 is odd? That would require i+2.
                # Let's trace: tri(3) = tri(2) + tri(1) + tri(4).
                # Here, 2 is even, 1 is odd, 4 is even.
                # tri(1) = tri(0) + tri(-1) + tri(2).
                # This suggests the sequence is built such that even indices are 
                # anchor points.

                # Let's re-calculate tri(1) using the formulas provided:
                # tri(1) is odd. tri(1) = tri(0) + tri(-1) + tri(2).
                # But the problem explicitly states tri(1) = 3.
                # This is a special base case.
                pass # Handled by explicit check below

            # Let's refine the logic:
            # 1. tri(1) = 3 (Given)
            # 2. tri(even n) = 1 + n/2
            # 3. tri(odd n > 1) = tri(n-1) + tri(n-2) + tri(n+1)
            # Let's check tri(3) again: tri(3) = tri(2) + tri(1) + tri(4)
            # tri(2) = 1 + 2/2 = 2
            # tri(1) = 3
            # tri(4) = 1 + 4/2 = 3
            # tri(3) = 2 + 3 + 3 = 8. Correct.

            # To compute sequence[i] where i is odd and i > 1:
            # we need sequence[i-1], sequence[i-2], and tri(i+1).
            # tri(i+1) is always even because i is odd.

            # Special case for i = 1
            if i == 1:
                sequence[i] = 3
            else:
                next_val_at_i_plus_1 = 1 + ((i + 1) // 2)
                sequence[i] = prev_val + prev_prev_val + next_val_at_i_plus_1

    return sequence

# The function is already defined with the required signature and logic.