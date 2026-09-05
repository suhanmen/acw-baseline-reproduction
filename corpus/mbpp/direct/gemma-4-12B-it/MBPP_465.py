def drop_empty(data: dict) -> dict:
    """
    Drops items from a dictionary if their values are None.
    """
    return {k: v for k, v in data.items() if v is not None}

if __name__ == "__main__":
    assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}) == {'c1': 'Red', 'c2': 'Green'}
    assert drop_empty({'c1': 'Red', 'c2': None, 'c3': None}) == {'c1': 'Red'}
    assert drop_empty({'c1': None, 'c2': 'Green', 'c3': None}) == {'c2': 'Green'}