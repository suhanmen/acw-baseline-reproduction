def count_Substrings(s: str, k: int) -> int:
    count = 0
    n = len(s)
    if k <= 0 or n < k:
        return 0

    # Map digits to integers
    digits = [int(c) for c in s]

    # We need to count substrings of length k where sum(digits) == k
    # This means sum(digits) == k, so sum of digits must equal the length k
    # We can use a sliding window of size k

    current_sum = sum(digits[:k])
    if current_sum == k:
        count += 1

    for i in range(1, n - k + 1):
        # Remove the element going out of the window
        current_sum = current_sum - digits[i-1] + digits[i+k-1]
        if current_sum == k:
            count += 1

    return count