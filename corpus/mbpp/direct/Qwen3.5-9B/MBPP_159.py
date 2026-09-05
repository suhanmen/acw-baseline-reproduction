def month_season(month, day):
    month_days = {
        'January': 31, 'February': 28, 'March': 31, 'April': 30,
        'May': 31, 'June': 30, 'July': 31, 'August': 31,
        'September': 30, 'October': 31, 'November': 30, 'December': 31
    }

    days_range = {
        'winter': (1, 31),       # Jan 1 - Mar 20
        'spring': (21, 31),      # Mar 21 - May 20
        'summer': (1, 31),       # May 21 - Aug 31
        'autumn': (1, 31)        # Sep 1 - Nov 30
    }

    # Normalize to Northern Hemisphere seasons
    month_index = list(month_days.keys()).index(month)
    day_of_year = month_index * 31 + day  # Simplified approximation

    if month_index <= 1:  # Jan, Feb
        return 'winter'
    elif month_index == 2:  # Mar
        if day <= 20:
            return 'winter'
        else:
            return 'spring'
    elif month_index == 3:  # Apr
        return 'spring'
    elif month_index == 4:  # May
        if day <= 20:
            return 'spring'
        else:
            return 'summer'
    elif month_index == 5:  # Jun, Jul, Aug
        return 'summer'
    elif month_index == 6:  # Sep
        return 'autumn'
    elif month_index == 7:  # Oct, Nov
        return 'autumn'
    else:  # Dec
        return 'winter'