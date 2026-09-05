def check_monthnumber(month: str) -> bool:
    """
    Checks whether the given month name contains 30 days or not.
    Returns True if the month has exactly 30 days.
    """
    # Months with 30 days: April, June, September, November
    months_with_30_days = ["April", "June", "September", "November"]

    # Handle case-insensitivity just in case, though assertions use Capitalized
    return month.capitalize() in months_with_30_days

if __name__ == "__main__":
    assert check_monthnumber("February") == False
    assert check_monthnumber("June") == True
    assert check_monthnumber("April") == True