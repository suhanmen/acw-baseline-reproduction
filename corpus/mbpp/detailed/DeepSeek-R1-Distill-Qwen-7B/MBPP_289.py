Okay, I need to write a Python function called `odd_Days` that calculates the number of odd days in a given year. The function needs to handle various edge cases and return the correct count based on the examples provided.

First, I need to understand what "odd days" means. I recall that in the Gregorian calendar, a regular year has 365 days, which is 52 weeks plus 1 day. A leap year has 366 days, which is 52 weeks plus 2 days. These extra days are called odd days. So, the number of odd days in a year depends on whether it's a leap year or not.

The examples provided are:
- odd_Days(100) should return 5
- odd_Days(50) should return 6
- odd_Days(75) should return 2

Wait, those inputs are all numbers between 50 and 100, but I realize that the actual number of years from 1 AD to year X would be X years. However, the examples might be showing specific cases for years 50, 75, and 100, but their output doesn't align with the simple leap year rules. Let me double-check.

Actually, let's think about the leap year rules:
- A year is a leap year if it is divisible by 4
- Except for end-of-century years, which must be divisible by 400 to be leap years

So, for example:
- 100 is divisible by 100 but not by 400, so it's not a leap year
- 400 would be a leap year

But the examples provided might be based on a different interpretation or perhaps a simplified version of odd days calculation. Let me verify the number of odd days for specific years:

1. Year 50:
   - Leap year calculation: 50 / 4 = 12.5, so not a leap year
   - Odd days: 50 mod 7 = 1 (since 50 / 7 is 7 weeks with 1 day remaining)
   - But the example expects 6, which suggests that perhaps the calculation is cumulative up to that year

Wait, perhaps the function is supposed to calculate the number of odd days from year 1 to the given year inclusive. Let me clarify:

If we consider the cumulative odd days from year 1 to year X, we need to calculate the total number of leap years and regular years up to X and sum their respective odd days.

So, let's define:
- A regular year has 1 odd day
- A leap year has 2 odd days

Therefore, for each year from 1 to X, we add 1 or 2 to the total based on whether it's a regular or leap year.

Let me validate this with the examples:

Example 1: odd_Days(50) should return 6

Let's calculate:
- Number of leap years up to 50: years divisible by 4, but not by 100 if not divisible by 400
- Leap years up to 50: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48 → 12 leap years
- Total regular years: 50 - 12 = 38
- Total odd days: 38 * 1 + 12 * 2 = 38 + 24 = 62
- But the example expects 6, which is much lower. So my initial understanding is incorrect.

Hmm, maybe I'm misunderstanding the problem. Let me try another approach.

Perhaps "odd days" refers to the number of years that have an odd number of days up to a certain point in history. For example, every 4 years, a leap year occurs, which adds an extra day, making that year have 366 days (which is 52 weeks + 2 days). So the odd days accumulate over time.

Wait, but the examples don't make sense with that either. Let me think differently.

I recall that the Gregorian calendar repeats every 400 years, and the number of odd days in 400 years is 0 (since 400 is divisible by 400, so it's a leap year, and 400/4 = 100 leap years, but 100/100 = 1 century year, which is divisible by 400, so total leap years are 97). Thus, 400 years have 400 + 97 = 497 days, which is exactly 71 weeks, 0 days.

But the examples are specific:

- odd_Days(100) → 5
- odd_Days(50) → 6
- odd_Days(75) → 2

Wait, perhaps "odd days" refers to the number of years up to X that have an odd number of letters in their name? No, that doesn't make sense.

Alternatively, maybe "odd days" refers to the number of years where the day of the week advances by an odd number of days. But I'm not sure.

Let me think differently: perhaps "odd days" are the days that fall on odd dates in the month. But that's not consistent with the examples.

Alternatively, maybe "odd days" refer to the number of days in a year that have an odd day of the month, but that also doesn't align with the examples.

Wait, perhaps "odd days" is a specific term in the problem that I'm not familiar with. Let me try to find the correct interpretation.

After some research, I find that in the context of the Gregorian calendar, an "odd day" is often used to refer to the surplus days that accumulate over the leap year rules. Each year contributes 1 day, and leap years contribute an additional day, so each leap year adds one extra odd day.

Thus, the total number of odd days up to a given year is equal to the number of leap years plus the number of regular years.

Wait, but for year X, the total odd days would be X years, each contributing at least 1 day, plus 1 for each leap year.

So, total_odd_days = X + number_of_leap_years_up_to_X

But let's test this with the examples:

Example 1: odd_Days(100) → 5

If X=100:
- Number of leap years up to 100: years divisible by 4, except for century years unless divisible by 400
- Leap years up to 100: 25 (100/4) but exclude 100 since it's a century year not divisible by 400. So 24 leap years.
- Total_odd_days = 100 + 24 = 124 → not matching the example.

This doesn't align. So perhaps my initial understanding is wrong.

Alternatively, maybe "odd days" refer to the number of years where the year number is odd. For example:

- For odd years (1,3,5,...), each contributes 1 odd day
- For even years, they contribute 0 odd days

But let's test this with the examples:

Example 1: odd_Days(100) → 5

Number of odd years up to 100: 50 (years 1,3,5,...,99)
Example expects 5, which doesn't match.

This approach is incorrect.

Another approach: Perhaps "odd days" refers to the number of days in the year that have an odd number of days in their month. For example, months with 31, 30, or 28/29 days. But this is speculative.

However, the examples suggest that odd_Days(50) → 6, which could relate to something like 6 leap years, but this is unclear.

Given the confusion, perhaps the function is intended to calculate something else entirely. Let's try to think differently.

Perhaps "odd days" are the number of days in a year that are odd-numbered days of the month. For example, in a regular year (365 days), there are 31 days in January (all odd-numbered days are 1,3,5,...,31 → 16 days). In February, 28 or 29 days, so 14 or 15 odd-numbered days. Similarly, March has 16 odd-numbered days, etc.

But this seems too complex and wouldn't align with the given examples.

Given the confusion, perhaps the function is intended to calculate the number of years up to X that have an odd number of days, considering leap years. But I need to validate this with the examples.

Let's attempt to find a pattern in the given examples:

- odd_Days(100) = 5
- odd_Days(50) = 6
- odd_Days(75) = 2

This suggests that the number of "odd days" increases very slowly with the year. It's possible that "odd days" refer to the number of leap years, but adjusted in some way.

Alternatively, perhaps "odd days" refer to the number of times the year ends on an odd day of the week. But this is also speculative.

Given the ambiguity, I will assume that "odd days" refer to the number of leap years up to a given year. Let's proceed with this assumption.

Now, I need to write a function that calculates the number of leap years up to and including the given year, and then returns that count.

Wait, but the examples don't align with that assumption. Let me think again.

Perhaps "odd days" refer to the number of days in the year modulo 7, summed up over all years up to X. For example:

For each year from 1 to X:
- If the year is a leap year, add 2 days
- Else, add 1 day

Then, sum all these to get the total number of odd days.

Let's test this with the examples:

Example 1: odd_Days(100) = 5

Calculate total_odd_days = number of leap years * 2 + (100 - number_of_leap_years) * 1

First, find the number of leap years up to 100.

Leap years up to 100:
- Divisible by 4: 25 (100/4)
- Subtract century years not divisible by 400: 100 is a century year and not divisible by 400, so 25 - 1 = 24

So, number_of_leap_years = 24

Then, total_odd_days = 24 * 2 + (100 - 24) * 1 = 48 + 76 = 124 → which doesn't match the example.

This approach is incorrect.

Another approach: perhaps "odd days" are the days of the week that are odd-numbered, assuming each year has 52 weeks.

But this is speculative.

Given the confusion, perhaps the problem is referring to the number of years that are leap years, but the examples provided are incorrect or refer to a different definition.

Alternatively, perhaps "odd days" are the number of years where the year modulo 7 is odd. Let's test this:

For year X, count how many years from 1 to X have year % 7 != 0.

Example 1: X=100

Number of years with year %7 !=0: 100 - floor(100/7) = 100 -14 =86 → no match.

This doesn't align with the examples.

Given that I can't find a logical interpretation that matches the examples, I will assume that the function is supposed to calculate the number of leap years up to a given year, and return that count. This is a standard calculation in Gregorian calendar problems.

So, let's define:

number_of_leap_years = ?

Leap years are years divisible by 4, except for century years not divisible by 400.

So, to calculate the number of leap years up to year X:

1. Count all years divisible by 4 up to X: X // 4
2. Subtract the number of century years (divisible by 100) up to X: X // 100
3. Add back the number of years divisible by 400 up to X: X // 400

So, number_of_leap_years = (X // 4) - (X // 100) + (X // 400)

Then, the total_odd_days is number_of_leap_years * 2 + (X - number_of_leap_years) * 1

Wait, no. If each regular year has 1 odd day and each leap year has 2, then the total odd days would be:

total_odd_days = (X - number_of_leap_years) * 1 + number_of_leap_years * 2 = X + number_of_leap_years

But the examples don't align with this. Let me test with X=100:

number_of_leap_years = (100 //4 ) - (100//100 ) + (100//400 ) = 25 -1 +0 =24

total_odd_days =100 +24=124 → but the example expects 5.

So, this can't be right.

Wait, perhaps the function is supposed to return the number of leap years, but considering some other rule.

Alternatively, perhaps it's the number of leap years that have been "odd" in some way, such as leap years that are odd-numbered.

But I can't see how this would match the examples.

Given the confusion, perhaps the problem statement is incorrect or misinterpreted.

Alternatively, perhaps the function is supposed to return the number of years where the year has an odd number of letters, but that's unlikely.

Given that, perhaps I need to revisit the problem.

Alternative approach: let's look for a pattern in the examples.

Given: