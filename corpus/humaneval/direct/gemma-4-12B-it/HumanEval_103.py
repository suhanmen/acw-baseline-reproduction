def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m:
        return -1

    # The sum of an arithmetic progression from n to m is (n + m) * (m - n + 1) / 2
    # The average is the sum divided by the number of elements (m - n + 1)
    # Therefore, the average is simply (n + m) / 2
    avg = (n + m) / 2

    # Round to the nearest integer. 
    # In Python, round(0.5) goes to 0 (round to even).
    # Standard mathematical rounding for .5 is usually up. 
    # Let's check the examples:
    # (1+5)/2 = 3.0 -> 3 -> "0b11"
    # (10+20)/2 = 15.0 -> 15 -> "0b1111"
    # (20+33)/2 = 26.5 -> 27 -> "0b11010" (Wait, 27 is 11011 in binary. 
    # Let's re-check 20 to 33: avg = (20+33)/2 = 26.5.
    # 26 is 11010. 27 is 11011.
    # If the example says 20-33 is "0b11010", it means 26.5 was rounded down or 
    # the average was calculated differently.
    # Let's re-calculate: Sum(20...33) = (20+33)*14 / 2 = 53*7 = 371.
    # Average = 371 / 14 = 26.5.
    # Binary "0b11010" is 26.
    # This implies round(26.5) -> 26. This is standard Python 3 round() behavior.

    rounded_val = int(round(avg))

    # However, round(26.5) in Python 3 is 26.
    # round(0.5) is 0, round(1.5) is 2, round(2.5) is 2.
    # Let's check (1+5)/2 = 3.0. round(3.0) = 3. bin(3) = '0b11'. Correct.
    # Let's check (10+20)/2 = 15.0. round(15.0) = 15. bin(15) = '0b1111'. Correct.
    # Let's check (20+33)/2 = 26.5. round(26.5) = 26. bin(26) = '0b11010'. Correct.

    return bin(rounded_val)