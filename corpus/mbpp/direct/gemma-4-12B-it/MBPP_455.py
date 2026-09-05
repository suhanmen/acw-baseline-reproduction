def check_monthnumb_number(month_num: int) -> bool:
    """
    Checks whether the given month number contains 31 days.

    Args:
        month_num (int): The month number (1-12).

    Returns:
        bool: True if the month has 31 days, False otherwise.
    """
    # Months with 31 days are January (1), March (3), May (5), 
    # July (7), August (8), October (10), and December (12).
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    return month_num in months_with_31_days

if __name__ == "__main__":
    assert check_monthnumb_number(5) == True
    assert check_monthnumb_number(2) == False
    assert check_monthnumb_number(6) == False