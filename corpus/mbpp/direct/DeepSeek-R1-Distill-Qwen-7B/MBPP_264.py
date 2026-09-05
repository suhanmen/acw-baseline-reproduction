def dog_age(dog_years):
    if dog_years <= 0:
        return 0
    elif dog_years == 1:
        return 15
    else:
        return 15 + (dog_years - 1) * 4