def cal_electbill(kwh):
    """
    Calculate the electricity bill based on the given KWh usage.

    Args:
        kwh (float): The amount of electricity used in KWh.

    Returns:
        float: The calculated electricity bill.

    Raises:
        ValueError: If the input is not a valid number or if it's negative.
    """
    # Validate the input
    try:
        kwh = float(kwh)
    except ValueError:
        raise ValueError("Invalid input. Please provide a valid number.")

    if kwh < 0:
        raise ValueError("Electricity usage cannot be negative.")

    # Calculate the base cost
    base = kwh * 0.12

    # Calculate the peak cost
    if kwh >= 200:
        peak = 0.15 * (kwh - 200)
    else:
        peak = 0.0

    # Calculate the additional cost for high usage
    if kwh >= 500:
        additional = 0.25 * (kwh - 500)
    else:
        additional = 0.0

    # Sum all the costs and add a 5% tax on the total
    total = base + peak + additional
    total_with_tax = total * 1.05

    return total_with_tax