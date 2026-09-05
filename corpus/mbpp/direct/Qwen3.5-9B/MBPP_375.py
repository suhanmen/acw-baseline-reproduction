def round_num(n, base):
    return (int(n / base) + (0.5 if (n / base) - int(n / base) >= 0.5 else 0)) * base

# Correction: The logic above is flawed for negative numbers and edge cases. Let's use a cleaner approach.
def round_num(n, base):
    return round(n / base) * base

# However, Python's round() rounds to even for .5 cases (banker's rounding), which might fail strict mathematical rounding tests if the problem expects standard rounding (round half up).
# Let's re-read the requirements: "round to the nearest multiple".
# Example: 4722 / 10 = 472.2 -> 472 -> 4720. Correct.
# Example: 1111 / 5 = 222.2 -> 222 -> 1110. Correct.
# Example: 219 / 2 = 109.5 -> 109 or 110? 
# Standard rounding (round half up) for 219/2=109.5 should be 110 * 2 = 220? 
# But the assertion says round_num(219,2)==218.
# 218 is 219 rounded down to nearest even multiple? Or is it floor?
# 219 / 2 = 109.5. If result is 218, that means 109 * 2. So it rounded down (truncated) or to even?
# 109 is odd. 108 is even. 216 is even. 218 is not a multiple of 2? Wait. 218 % 2 == 0. Yes.
# 109 * 2 = 218.
# So 219 -> 218 means it went to 109 * 2.
# 219 / 2 = 109.5. 
# If we use standard round half up: 110 * 2 = 220.
# If we use banker's rounding (round to even): 110 (even) -> 220. Or 109 (odd)? No, 109.5 rounds to 110.
# Wait, 109.5. The digit before 5 is 9. 9+1 = 10. Carry over. 110.
# Why is the expected output 218?
# 218 = 109 * 2.
# So 109.5 was rounded to 109. That is rounding half down or floor?
# Or maybe the problem implies "round to nearest, but if exactly halfway, round to the even multiple"? 
# 218 is an even multiple of 2? 218/2 = 109. 109 is odd. 
# 220/2 = 110. 110 is even.
# So if it was "round to even multiple", 220 would be the answer (multiple 110 is even).
# But the assertion says 218.
# This implies the behavior is: Round half to the *left* (down)? Or is there a specific logic?
# Let's check: 4722/10 = 472.2 -> 472 (closest).
# 1111/5 = 222.2 -> 222 (closest).
# 219/2 = 109.5. 
# Nearest integers to 109.5 are 109 and 110. Distance is equal.
# If the result is 218 (109*2), it chose 109.
# Why? Maybe it's rounding half towards negative infinity? No, inputs are positive.
# Maybe the "nearest multiple" logic prioritizes the lower one on a tie?
# Let's implement a "round half down" behavior for ties.
# Or simply: if n/base - floor(n/base) == 0.5, take floor.
# Let's try that logic.

def round_num(n, base):
    val = n / base
    floor_val = int(val)
    ceil_val = floor_val + 1
    diff_down = val - floor_val
    diff_up = ceil_val - val

    if diff_down < diff_up:
        return floor_val * base
    elif diff_up < diff_down:
        return ceil_val * base
    else: # Equal (0.5)
        # Based on 219->218, we choose floor_val (109)
        return floor_val * base