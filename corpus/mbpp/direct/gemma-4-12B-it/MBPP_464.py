def check_value(data_dict: dict, value: any) -> bool:
    """
    Checks if all values in the dictionary are equal to the provided value.
    """
    if not data_dict:
        return True

    return all(v == value for v in data_dict.values())

if __name__ == "__main__":
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10) == False
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 12) == True
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 5) == False