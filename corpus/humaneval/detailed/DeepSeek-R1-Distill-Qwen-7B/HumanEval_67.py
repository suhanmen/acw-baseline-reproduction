def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Args:
        s (str): A string representing the count of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.

    Raises:
        ValueError: If the input string is not in the expected format, 
                  or if the calculated number of mango fruits is negative,
                  or if the total fruits count is less than the sum of apples and oranges.

    Observed behaviour on valid inputs must be exactly what the problem asks for.
    """
    # Parse the input string to extract the counts of apples and oranges
    def parse_fruit_count(s):
        fruits = s.split(' and ')
        if len(fruits) != 2:
            raise ValueError("Invalid format for fruit counts")

        for fruit in fruits:
            if 'apple' not in fruit.lower() and 'orange' not in fruit.lower():
                raise ValueError("Each fruit count must specify apples or oranges")
            count_part = fruit.split()[0]
            if not count_part.isdigit():
                raise ValueError(f"Invalid number format in {fruit}")
            count = int(count_part)
            yield count

    # Get the counts of apples and oranges
    try:
        apples, oranges = next(parse_fruit_count(s)), next(parse_fruit_count(s))
    except StopIteration:
        raise ValueError("String does not contain exactly two fruit counts")
    except ValueError as e:
        raise ValueError(f"Invalid input string: {e}")

    # Calculate the number of mango fruits
    mango = n - apples - oranges

    # Validate the result
    if mango < 0:
        raise ValueError("Number of mango fruits cannot be negative")
    if apples + oranges > n:
        raise ValueError("Total apples and oranges exceeds total fruits")

    return mango