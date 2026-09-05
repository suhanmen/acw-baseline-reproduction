def month_season(month, day):
    month = month.lower()
    if month in ['january', 'february', 'march', 'april']:
        return 'spring'
    elif month in ['april', 'may', 'june', 'july', 'august', 'september']:
        return 'summer'
    elif month in ['september', 'october', 'november', 'december']:
        return 'fall'  # Another name for autumn
    else:
        return 'winter'