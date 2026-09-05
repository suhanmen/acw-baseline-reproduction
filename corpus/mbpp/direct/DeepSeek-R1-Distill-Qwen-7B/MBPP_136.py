def cal_electbill(usage):
    if usage <= 50:
        cost = usage * 0.25
    elif usage <= 100:
        cost = 50 * 0.25 + (usage - 50) * 0.5
    else:
        cost = 50 * 0.25 + 50 * 0.5 + (usage - 100) * 0.75
    return round(cost * 100) / 100