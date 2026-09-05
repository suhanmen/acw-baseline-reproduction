from typing import List, Tuple, Union

def _validate_integer(value: object, name: str, min_val: int, max_val: int) -> None:
    """
    Helper function to validate that a given value is an integer within a specific range.

    Args:
        value: The value to validate.
        name: A descriptive name for the value (used in error messages).
        min_val: The minimum allowed value (inclusive).
        max_val: The maximum allowed value (inclusive).

    Raises:
        TypeError: If the value is not an integer (excluding booleans).
        ValueError: If the value is outside the allowed range.
    """
    # Booleans are a subclass of int in Python, but often we want to reject them explicitly
    # for clarity in function signatures unless specifically allowed.
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"Argument '{name}' must be an integer, got {type(value).__name__}.")

    if value < min_val:
        raise ValueError(f"Argument '{name}' must be >= {min_val}, got {value}.")

    if value > max_val:
        raise ValueError(f"Argument '{name}' must be <= {max_val}, got {value}.")

def _calculate_meal_count(number: int, need: int, remaining: int) -> int:
    """
    Calculates how many carrots the rabbit actually eats from the stock.

    The rabbit wants to eat 'need' carrots, but only 'remaining' are available.
    The rabbit will eat all 'remaining' if they are fewer than 'need'.

    Args:
        number: Irrelevant for this calculation (historical eaten amount).
        need: The desired number of carrots to eat.
        remaining: The number of carrots currently in stock.

    Returns:
        The actual number of carrots eaten from the stock.
    """
    # Determine the amount to eat: limited by what is available
    actual_eaten_from_stock = min(need, remaining)
    return actual_eaten_from_stock

def _calculate_final_state(
    initial_eaten: int, 
    eaten_from_stock: int, 
    remaining_stock: int
) -> Tuple[int, int]:
    """
    Calculates the final state after the meal.

    Args:
        initial_eaten: Carrots eaten before this meal.
        eaten_from_stock: Carrots taken from the current stock.
        remaining_stock: Carrots available in stock before eating.

    Returns:
        A tuple containing:
            1. Total carrots eaten after the meal.
            2. Carrots remaining in stock after the meal.
    """
    total_eaten = initial_eaten + eaten_from_stock
    final_remaining = remaining_stock - eaten_from_stock

    return total_eaten, final_remaining

def eat(number: int, need: int, remaining: int) -> List[int]:
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.

    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]

    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of carrots thet exist in stock

    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    # Define the constraint boundaries as per the problem description
    MIN_BOUNDARY = 0
    MAX_BOUNDARY = 1000

    # Step 1: Validate the 'number' argument (carrots already eaten)
    _validate_integer(number, "number", MIN_BOUNDARY, MAX_BOUNDARY)

    # Step 2: Validate the 'need' argument (carrots to eat)
    _validate_integer(need, "need", MIN_BOUNDARY, MAX_BOUNDARY)

    # Step 3: Validate the 'remaining' argument (carrots in stock)
    _validate_integer(remaining, "remaining", MIN_BOUNDARY, MAX_BOUNDARY)

    # Step 4: Calculate how many carrots are actually consumed from the stock.
    # Logic: The rabbit tries to eat 'need', but cannot eat more than 'remaining'.
    actual_consumption = _calculate_meal_count(number, need, remaining)

    # Step 5: Calculate the final totals based on the consumption.
    # Total eaten = Previous eaten + What was just eaten.
    # Remaining left = Stock had - What was just eaten.
    final_total_eaten, final_stock_left = _calculate_final_state(
        initial_eaten=number,
        eaten_from_stock=actual_consumption,
        remaining_stock=remaining
    )

    # Step 6: Return the result as a list of integers as specified by the docstring.
    return [final_total_eaten, final_stock_left]