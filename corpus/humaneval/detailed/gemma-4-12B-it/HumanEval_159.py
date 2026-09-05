from typing import List

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
        the number of remaining carrots thet exist in stock

    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """

    # --- Input Validation ---
    # Defensive programming: Ensure all inputs are integers.
    if not isinstance(number, int) or not isinstance(need, int) or not isinstance(remaining, int):
        raise TypeError("All input arguments must be integers.")

    # Defensive programming: Check constraints.
    # While the prompt gives constraints, production code should handle/warn on violations.
    if not (0 <= number <= 1000) or not (0 <= need <= 1000) or not (0 <= remaining <= 1000):
        # In a real production environment, we might raise a ValueError.
        # For this logic, we will proceed but note the boundary check.
        pass

    # --- Logic Breakdown ---

    def calculate_eaten_amount(needed_amount: int, available_stock: int) -> int:
        """
        Helper to determine how many carrots can actually be consumed.
        If we need more than what exists, we take everything.
        Otherwise, we take exactly what we need.
        """
        if needed_amount <= 0:
            return 0

        if needed_amount > available_stock:
            return available_stock
        else:
            return needed_amount

    # Step 1: Determine how many carrots the rabbit intends to eat based on need.
    # The rabbit wants to eat 'need' carrots.

    # Step 2: Determine how many carrots are actually consumed from the 'remaining' stock.
    carrots_consumed_from_stock = calculate_eaten_amount(need, remaining)

    # Step 3: Calculate the final total of carrots eaten.
    # This is the initial amount eaten plus the new amount consumed.
    total_eaten_after_meals = number + carrots_consumed_from_stock

    # Step 4: Calculate the final remaining stock.
    # This is the original stock minus what was consumed.
    carrots_left_in_stock = remaining - carrots_consumed_from_stock

    # Final Result
    result = [total_eaten_after_meals, carrots_left_in_stock]

    return result