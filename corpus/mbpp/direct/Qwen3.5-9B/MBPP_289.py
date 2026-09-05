def odd_Days(year):
    """
    Calculate the number of odd days in a given year.
    Odd days are the remainder days after dividing total days by 7.

    A common year has 365 days (365 % 7 = 1 odd day).
    A leap year has 366 days (366 % 7 = 2 odd days).

    Leap year rule:
    - Divisible by 4 is a candidate.
    - Divisible by 100 is not a leap year, UNLESS divisible by 400.
    """
    if year % 400 == 0:
        is_leap = True
    elif year % 100 == 0:
        is_leap = False
    elif year % 4 == 0:
        is_leap = True
    else:
        is_leap = False

    if is_leap:
        return 2  # 366 % 7 = 2
    else:
        return 1  # 365 % 7 = 1

# Verification against provided assertions
# assert odd_Days(100) == 5  -> This assertion seems inconsistent with standard calendar logic (100 is not leap -> 1 odd day)
# However, the problem requires the function to satisfy these specific assertions.
# Let's re-evaluate based on the required outputs:
# odd_Days(100) == 5
# odd_Days(50) == 6
# odd_Days(75) == 2
# These outputs do not match standard calendar calculations for "odd days in a year".
# It appears the problem might be defining a custom rule or there's a misunderstanding in the problem statement vs standard definitions.
# BUT, as an AI, I must satisfy the assertions provided.
# Let's look for a pattern:
# 100 -> 5
# 50  -> 6
# 75  -> 2
# There is no obvious mathematical relation to standard calendar years for these specific outputs.
# Wait, perhaps the question implies calculating odd days from a specific start point? 
# Or maybe it's a trick question where the function simply hardcodes or uses a modulo on the year itself?
# Let's try: year % 7? 
# 100 % 7 = 2 (No)
# 50 % 7 = 1 (No)
# 75 % 7 = 5 (No)
# 
# Let's try sum of digits?
# 100 -> 1 -> 1 (No)
# 
# Let's reconsider the standard definition. Maybe the input isn't the year itself but related to something else?
# "Calculate the number of odd days in a given year."
# Standard: 
# Non-leap: 1
# Leap: 2
# 100 is non-leap -> 1. But assertion says 5.
# 50 is non-leap -> 1. But assertion says 6.
# 75 is non-leap -> 1. But assertion says 2.
# 
# Since I cannot change the logic of the calendar, and the assertions contradict standard calendar rules for those years,
# I must assume the problem expects a function that satisfies those specific inputs/outputs regardless of standard calendar logic.
# However, usually these problems come from a specific context (like odd days from a base year).
# Is it possible the input is not the year? No, "in a given year".
# Is it possible the "odd days" calculation accumulates? No, "in a given year".
# 
# Let's look at the numbers again.
# 100 -> 5
# 50 -> 6
# 75 -> 2
# 
# Could it be (year % 7) + some offset?
# 100 % 7 = 2. Target 5. Diff +3.
# 50 % 7 = 1. Target 6. Diff +5.
# 75 % 7 = 5. Target 2. Diff -3.
# No consistent offset.
# 
# What if it's related to the day of the week of a specific date?
# Without more context, satisfying the assertions is the only way.
# Since the problem statement asks to "Solve the following problem" and provides specific assertions, 
# and standard calendar logic fails these, there might be a hidden rule or the examples are from a specific sequence.
# 
# However, often in these coding challenges, if the assertions don't match reality, the test is just checking the function against those values.
# But a function should have logic.
# 
# Let's reconsider the possibility of an error in the problem statement provided in the prompt.
# If I strictly follow standard logic:
# def odd_Days(year):
#   return 2 if is_leap(year) else 1
# This will fail the assertions.
# 
# Is it possible the inputs are not years but something else mapped to years?
# Or maybe the "odd days" is calculated differently?
# 
# Let's try to find a polynomial P(year) such that:
# P(100) = 5
# P(50) = 6
# P(75) = 2
# This is an interpolation problem with 3 points. There are infinite solutions.
# But code usually has a simple formula.
# 
# Wait, could it be calculating odd days from a specific date in that year?
# If the question is flawed, I have to make the best guess.
# 
# Alternative interpretation: Maybe the inputs are not 100, 50, 75 years, but something else? 
# No, "odd_Days(100)".
# 
# Let's assume there is a typo in the problem's assertions or my understanding of "odd days".
# In standard Gregorian calendar:
# 100 (non-leap) -> 1 odd day.
# 50 (non-leap) -> 1 odd day.
# 75 (non-leap) -> 1 odd day.
# The assertions 5, 6, 2 are completely off.
# 
# Perhaps the function is supposed to return the total odd days from year 1 to the given year?
# Let's check:
# Total days from year 1 to year Y.
# Odd days = Total days % 7.
# Year 100:
# 99 normal years + 25 leap years (4, 8, ... 96). 
# Actually, year 100 itself is not leap.
# So years 1 to 99.
# Normal years: 1 to 99 excluding leap.
# Leap years: 4, 8, ..., 96. Count = 24.
# Total years = 99. Normal = 75.
# Days = 75*365 + 24*366 = 27375 + 8784 = 36159.
# 36159 % 7 = 3. (Assertion says 5).
# 
# Year 50:
# Years 1 to 49.
# Leap: 4, ..., 48 (12 years).
# Normal: 37.
# Days = 37*365 + 12*366 = 13505 + 4392 = 17897.
# 17897 % 7 = 2. (Assertion says 6).
# 
# Year 75:
# Years 1 to 74.
# Leap: 4, ..., 72 (18 years).
# Normal: 56.
# Days = 56*365 + 18*366 = 20440 + 6588 = 27028.
# 27028 % 7 = 6. (Assertion says 2).
# 
# Still doesn't match.
# 
# Given the constraints, the only way to satisfy the assertions is to create a function that maps inputs to outputs as required, likely using a lookup or a specific custom formula designed for this puzzle.
# However, writing an arbitrary mapping is bad practice. 
# Is it possible the year is 100 AD, 50 AD, 75 AD in a different calendar? Unlikely.
# 
# Let's look at the numbers again.
# 100 -> 5
# 50 -> 6
# 75 -> 2
# 
# What if the input is the month? No.
# What if the function is simply:
# return {100: 5, 50: 6, 75: 2}.get(year, 1)
# This satisfies the assertions.
# 
# But as an "expert Python programmer", I should try to find the logic.
# Is there any property of 100, 50, 75?
# 100 is a century. 50 is half-century. 75 is three-quarters century.
# Maybe it's based on the Gregorian cycle of 400 years?
# In 400 years, there are 97 leap years. Total days = 146097. 146097 % 7 = 0.
# So odd days repeat every 400 years.
# Year 100: 
# Days in first 100 years = 24 leap + 76 normal = 24*366 + 76*365 = 8784 + 27740 = 36524.
# 36524 % 7 = 2. (Standard result for 100 years is 5 odd days in some contexts? No, 36524/7 = 5217 R 5).
# Ah! 36524 % 7 = 5.
# Let's re-calculate 100 years odd days.
# 100 years usually means 1 to 100.
# Leap years in 100 years (1 to 100): 4, 8, ..., 100.
# Wait, year 100 is divisible by 100 but not 400, so NOT a leap year.
# So leap years are 4, 8, ..., 96. Count = 24.
# Normal years = 76.
# Days = 24*366 + 76*365 = 8784 + 27740 = 36524.
# 36524 % 7 = 5.
# Assertion: odd_Days(100) == 5. MATCH!
# 
# Now Year 50 (1 to 50):
# Leap years: 4, 8, ..., 48. (12 years). Year 50 not leap.
# Normal: 38.
# Days = 12*366 + 38*365 = 4392 + 13870 = 18262.
# 18262 % 7 = 6.
# Assertion: odd_Days(50) == 6. MATCH!
# 
# Now Year 75 (1 to 75):
# Leap years: 4, ..., 72. (18 years). Year 75 not leap.
# Normal: 57.
# Days = 18*366 + 57*365 = 6588 + 20805 = 27393.
# 27393 % 7 = 2.
# Assertion: odd_Days(75) == 2. MATCH!
# 
# Conclusion: The function calculates the number of odd days from the beginning of year 1 up to and including the given `year`.
# It considers the `year` itself in the calculation.
# And it correctly identifies leap years (divisible by 4, not by 100 unless by 400).

def odd_Days(year):
    """
    Calculate the number of odd days from year 1 to the given year.
    Odd days = Total days % 7.
    Leap years are included correctly (divisible by 4, not 100 unless 400).
    """
    total_leap = 0
    total_normal = 0

    for y in range(1, year + 1):
        if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
            total_leap += 1
        else:
            total_normal += 1

    total_days = (total_leap * 366) + (total_normal * 365)
    return total_days % 7