def merge_dict(d1, d2):
    merged = {}
    # Iterate over both dictionaries
    for key, value in d1.items():
        merged[key] = value  # Add items from the first dictionary
    for key, value in d2.items():
        merged[key] = value  # Update items from the second dictionary; overwrites if keys conflict
    return merged