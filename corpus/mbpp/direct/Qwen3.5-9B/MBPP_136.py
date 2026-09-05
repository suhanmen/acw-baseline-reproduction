def cal_electbill(kwh):
    if kwh <= 50:
        rate = 2.50
    elif kwh <= 150:
        rate = 2.80
    elif kwh <= 300:
        rate = 3.20
    else:
        rate = 3.50

    base = kwh * rate
    surcharge = max(0, kwh - 300) * 0.5 if kwh > 300 else 0

    return base + surcharge

assert cal_electbill(75) == 246.25
assert cal_electbill(265) == 1442.75
assert cal_electbill(100) == 327.5