def check_monthnum(month_name):
    """
    Checks whether the given month name contains exactly 28 days (February).
    Note: While February is the only month with 28 days (usually), 
    the requirements specify checking if it 'contains' 28 days. 
    Based on the assertions provided, the function should return True 
    only for "February".
    """
    months_with_28_days = ["February"]
    return month_name in months_with_28_days

if __name__ == "__main__":
    assert check_monthnum("February") == True
    assert check_monthnum("January") == False
    assert check_monthnum("March") == False