def check_monthnumb_number(month: int) -> bool:
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    return month in months_with_31_days