def odd_Days(year: int) -> int:
    """
    Calculates the number of odd days in a given year.
    A year is a leap year if it is divisible by 400 or 
    (divisible by 4 and not divisible by 100).
    Ordinary years have 1 odd day (365 % 7 = 1).
    Leap years have 2 odd days (366 % 7 = 2).
    """
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return 2
    else:
        return 1

# The provided assertions are actually inconsistent with the standard 
# definition of "odd days in a year" (where odd days are 1 or 2).
# Looking at the provided test cases:
# odd_Days(100) == 5
# odd_Days(50) == 6
# odd_Days(75) == 2
# These values appear to relate to the calculation of "Odd Days" 
# from year 0 to the given year, but specifically they match 
# a logic where we calculate (Number of years) + (Number of leap years).
# However, the values given in the prompt:
# 100 -> 5, 50 -> 6, 75 -> 2 don't follow a standard linear pattern.
# Wait, looking at the numbers:
# 100 / 20 = 5
# 50 / ??
# Let's re-examine the prompt's assertions. 
# Actually, the numbers 5, 6, 2 for 100, 50, 75 are very specific.
# They correspond to: (Year // 20) if we ignore some rules? No.
# Let's try: (Year % 100) // 10? No.
# Let's try: (Year // 25) + (Year // 4) ... No.
# Re-evaluating the prompt's logic: 
# 100 -> 5 is (100/20)
# 50 -> 6? No.
# 75 -> 2? No.
# Actually, looking at the problem again, it might be a trick or specific 
# sequence. Let's check: (Year // 20) for 100 is 5. 
# (Year // 8) for 50 is 6. (Year // 37) for 75 is 2. 
# This is not a standard formula.

# Let's try another approach. Is it "Odd Days" in the sense of 
# (Total Days % 7) from Year 1 to Year X?
# Year 1 to 100: 100 years. 25 leaps (100 is not leap). 100 + 24 = 124. 124 % 7 = 5.
# Year 1 to 50: 50 years. 12 leaps. 50 + 12 = 62. 62 % 7 = 6.
# Year 1 to 75: 75 years. 18 leaps. 75 + 18 = 93. 93 % 7 = 2.
# This matches perfectly! 

def odd_Days(year: int) -> int:
    # Number of leap years from 1 to 'year'
    # A year is leap if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    # The formula for leap years up to year N is:
    # count = (N // 4) - (N // 100) + (N // 400)

    # However, the standard "odd days" calculation for a range of years
    # counts the leap years strictly before the current year or includes the year.
    # For the assertions to work:
    # Year 100: 100 + (100//4 - 100//100 + 100//400) = 100 + (25 - 1 + 0) = 124. 124 % 7 = 5.
    # Year 50: 50 + (50//4 - 50//100 + 50//400) = 50 + (12 - 0 + 0) = 62. 62 % 7 = 6.
    # Year 75: 75 + (75//4 - 75//100 + 75//400) = 75 + (18 - 0 + 0) = 93. 93 % 7 = 2.

    leap_years = (year // 4) - (year // 100) + (year // 400)
    total_days = year + leap_years
    return total_days % 7