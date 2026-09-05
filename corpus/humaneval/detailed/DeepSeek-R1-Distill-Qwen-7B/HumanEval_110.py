def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """

    # Helper function to check if a number is even
    def is_even(num):
        return num % 2 == 0

    # Helper function to count the number of even and odd elements in a list
    def count_evens_and_odds(lst):
        even_count = 0
        odd_count = 0
        for num in lst:
            if is_even(num):
                even_count += 1
            else:
                odd_count += 1
        return even_count, odd_count

    # Helper function to determine if we can make lst1 all even by exchanging elements
    def can_make_even(lst1, lst2):
        # Count the current even and odd numbers in lst1 and lst2
        even1, odd1 = count_evens_and_odds(lst1)
        even2, odd2 = count_evens_and_odds(lst2)

        # Total even and odd numbers available
        total_evens = even1 + even2
        total_odds = odd1 + odd2

        # Check if we have enough even numbers to cover all elements in lst1 after possible exchanges
        # and that we can replace the odds in lst1 with odds from lst2
        # We need to make sure that after moving the required number of even numbers into lst1,
        # there are enough odds in lst2 to cover the number of odds that remain in lst1

        # The number of evens needed in lst1 is even1_new = total_evens - (evens we can move from lst2)
        # But this is more complex, so we approach it by checking:

        # The number of odds in lst1 must be <= the number of odds in lst2
        # Because to make lst1 all even, we need to replace all odds in lst1 with odds from lst2
        # Similarly, after replacing, the remaining odds in lst2 can't exceed the available evens in lst1

        # So the conditions are:
        # 1. The number of odds in lst1 must be <= the number of odds in lst2
        # 2. After exchanging, the number of odds left in lst2 must be <= the number of evens in lst1 (after exchange)

        # Alternatively, think of it as:
        # - The number of odds in lst1 must be <= the number of odds in lst2 (because we can replace each odd in lst1 with an odd from lst2)
        # - The number of evens required in lst1 can be provided by the total evens available (even1 + even2)
        # - But to make it possible, the total number of evens should be >= the number of elements in lst1

        # However, after exchange, we need to ensure that the number of evens in lst1 is equal to the length of lst1
        # So, another condition is that the total number of evens in both lists must be >= len(lst1)
        # and that the number of odds in lst1 must be <= the number of odds in lst2

        # So, the function returns True if:
        # (even1 + even2) >= len(lst1) and odd1 <= odd2

        return (total_evens >= len(lst1)) and (odd1 <= odd2)

    # Check edge cases: if either list is empty
    if not lst1 or not lst2:
        return "NO"

    # Get the number of even and odd elements in both lists
    even1, odd1 = count_evens_and_odds(lst1)
    even2, odd2 = count_evens_and_odds(lst2)

    # Check if the conditions are met
    if (even1 + even2) >= len(lst1) and odd1 <= odd2:
        return "YES"
    else:
        return "NO"

    # The following line is a fallback, though the code above should handle all cases
    # Return "NO" in case of unexpected input
    return "NO"