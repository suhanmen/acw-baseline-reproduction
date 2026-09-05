from typing import List, Optional


def _validate_inputs(prices: list, k: int) -> None:
    """
    Validate the inputs to the max_profit function.

    Raises:
        TypeError: If 'prices' is not a list or 'k' is not an integer.
        ValueError: If 'prices' is empty, 'k' is negative, or 'k' is non-integer-like.
    """
    # Validate 'prices' type
    if not isinstance(prices, list):
        raise TypeError(f"Expected 'prices' to be a list, got {type(prices).__name__}")

    # Validate 'prices' content type (each element should be a number)
    for index, price in enumerate(prices):
        if not isinstance(price, (int, float)):
            raise TypeError(
                f"Expected all elements in 'prices' to be numbers, "
                f"but element at index {index} is {type(price).__name__}"
            )

    # Validate 'k' type
    if not isinstance(k, int):
        raise TypeError(f"Expected 'k' to be an integer, got {type(k).__name__}")

    # Validate 'k' value (must be non-negative)
    if k < 0:
        raise ValueError(f"Expected 'k' to be a non-negative integer, got {k}")

    # Handle the special case where prices is empty
    if len(prices) == 0:
        return  # We allow empty lists; the logic below will handle them gracefully


def _get_max_price_after_index(prices: List[float], index: int) -> float:
    """
    Helper function to find the maximum price in the array after a given index.

    Args:
        prices: The list of stock prices.
        index: The index up to which (exclusive) we search for the maximum.

    Returns:
        The maximum price found after the given index.
    """
    if index >= len(prices) - 1:
        return 0.0  # No future days to trade on

    max_price = prices[index + 1]
    for current_index in range(index + 1, len(prices)):
        if prices[current_index] > max_price:
            max_price = prices[current_index]

    return max_price


def _get_min_price_before_index(prices: List[float], index: int) -> float:
    """
    Helper function to find the minimum price in the array before a given index.

    Args:
        prices: The list of stock prices.
        index: The index from which (exclusive) we search for the minimum.

    Returns:
        The minimum price found before the given index.
    """
    if index <= 0:
        return 0.0  # No past days to buy from

    min_price = prices[index - 1]
    for current_index in range(1, index):
        if prices[current_index] < min_price:
            min_price = prices[current_index]

    return min_price


def _single_transaction_max_profit(prices: List[float]) -> float:
    """
    Helper function to calculate the maximum profit with exactly one transaction.

    Args:
        prices: The list of stock prices.

    Returns:
        The maximum profit possible with one transaction, or 0 if no profit is possible.
    """
    if len(prices) < 2:
        return 0.0

    min_price = prices[0]
    max_profit = 0.0

    for price in prices[1:]:
        # Calculate potential profit if we sold today
        potential_profit = price - min_price

        # Update max profit if this is better than what we've seen
        if potential_profit > max_profit:
            max_profit = potential_profit

        # Update minimum price seen so far
        if price < min_price:
            min_price = price

    return max_profit


def _k_transactions_max_profit(prices: List[float], k: int) -> float:
    """
    Helper function to calculate maximum profit with exactly k transactions.
    This function uses a simplified approach suitable for small k values,
    but note that for very large k (larger than n/2), it behaves like infinite transactions.

    Args:
        prices: The list of stock prices.
        k: The maximum number of transactions allowed.

    Returns:
        The maximum profit possible with at most k transactions.
    """
    n = len(prices)

    # If k is large enough, we can essentially buy and sell every time there's an increase
    if k >= n:
        total_profit = 0.0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]
        return total_profit

    # If k is 0, no transactions can be made
    if k == 0:
        return 0.0

    # Dynamic programming approach for limited k transactions
    # buy[i][j] = maximum profit on day j with at most i transactions remaining and holding a stock
    # sell[i][j] = maximum profit on day j with at most i transactions remaining and not holding a stock

    # However, for clarity and explicit steps, we'll use a simpler iterative approach for small k
    # We will track the best profit after each transaction

    # Initialize profits for 0 transactions
    current_max_profits = [0.0] * (k + 1)

    for current_price in prices:
        # We iterate backwards to avoid using the same transaction twice in one step
        for transaction_count in range(k, 0, -1):
            # To start a new transaction (buy), we need the max profit from previous transactions
            # and subtract the current price (cost of buying)
            # buy_profit = current_max_profits[transaction_count - 1] - current_price

            # To complete a transaction (sell), we add the current price to the profit from buying
            # sell_profit = buy_profit + current_price

            # Since we don't explicitly store buy/sell states separately in this simplified version,
            # we'll use a different approach for clarity:
            # Track the best buying point for the current transaction count

            pass

    # Let's use the standard DP approach for clarity and correctness:
    # buy[j] = max profit after j transactions, ending with a purchase (holding stock)
    # sell[j] = max profit after j transactions, ending with a sale (not holding stock)

    # Initialize arrays
    # buy[j] represents the max profit with j transactions completed and currently holding stock
    # sell[j] represents the max profit with j transactions completed and not holding stock

    # Actually, let's redefine for clarity:
    # buy[i] = max profit with i transactions done, currently holding a stock (after buying)
    # sell[i] = max profit with i transactions done, not holding stock (after selling)

    # Initialize with negative infinity for holding state (cannot hold without buying first)
    # and 0 for not holding state with 0 transactions

    # For i transactions:
    # buy[i] = max(sell[i-1] - price, buy[i])
    # sell[i] = max(buy[i] + price, sell[i])

    # But since we want to handle up to k transactions, we need k+1 states (0 to k)

    # Initialize
    # buy[i] for i in 0..k: max profit with i transactions completed and holding stock
    # sell[i] for i in 0..k: max profit with i transactions completed and not holding stock

    # For i=0 transactions:
    # buy[0] = -infinity (can't hold stock with 0 transactions completed if we count buying as start of transaction)
    # sell[0] = 0 (0 profit with 0 transactions)

    # Actually, let's align with the problem: k transactions means k buy-sell pairs.
    # State: dp[i][j] where i is transactions completed (0 to k), j is current day
    # dp[i][j][0] = max profit with i transactions, day j, not holding stock
    # dp[i][j][1] = max profit with i transactions, day j, holding stock

    # To save space, we can use two arrays: hold and sold
    # hold[i] = max profit with i transactions completed, currently holding stock
    # sold[i] = max profit with i transactions completed, not holding stock

    # Initialize
    hold = [-float('inf')] * (k + 1)
    sold = [0.0] * (k + 1)

    for price in prices:
        # Iterate backwards to avoid using updated values from the current price iteration
        for i in range(k, 0, -1):
            # Update sold[i]: max of either keeping previous sold[i] or selling from hold[i-1]
            # Actually, to complete the i-th transaction, we must have held stock from i-1 transactions
            # sold[i] = max(sold[i], hold[i-1] + price)

            # Update hold[i]: max of either keeping previous hold[i] or buying after i-1 transactions
            # hold[i] = max(hold[i], sold[i-1] - price)

            # However, we need to be careful about the order and dependencies
            # Let's do it step by step explicitly

            # First, calculate new_sold based on old_hold
            new_sold = max(sold[i], hold[i - 1] + price)

            # Then, calculate new_hold based on new_sold (or should it be old_sold? Should be old_sold)
            # Actually, we should use the values before any updates for the current price
            # So we need temporary variables or iterate backwards carefully

            # Since we iterate backwards, sold[i-1] is still from the previous day
            # But hold[i-1] might have been updated if we're not careful? 
            # No, we iterate i from k down to 1, so when we update hold[i], hold[i-1] hasn't been updated yet
            # So we can use the old values

            # Let's redo the logic with explicit old/new separation for clarity

            pass

        # After the loop above, we need to actually perform the updates
        # Let's rewrite the inner loop with clear old/new values

        for i in range(k, 0, -1):
            # Calculate the potential new sold value using the old hold[i-1]
            potential_sold = hold[i - 1] + price
            if potential_sold > sold[i]:
                sold[i] = potential_sold

            # Calculate the potential new hold value using the old sold[i-1]
            potential_hold = sold[i - 1] - price
            if potential_hold > hold[i]:
                hold[i] = potential_hold

    # The answer is the maximum value in sold array (since we end with no stock held)
    return max(sold)


def max_profit(prices: list, k: int) -> float:
    """
    Calculate the maximum profit from at most k stock transactions.

    Args:
        prices: A list of stock prices where prices[i] is the price on day i.
        k: The maximum number of transactions allowed.

    Returns:
        The maximum profit achievable with at most k transactions.

    Raises:
        TypeError: If inputs are of incorrect types.
        ValueError: If k is negative.
    """
    # Step 1: Validate inputs
    _validate_inputs(prices, k)

    # Step 2: Handle edge cases explicitly
    n = len(prices)

    # If there are no prices, no transactions can be made
    if n == 0:
        return 0.0

    # If k is 0, no transactions can be made
    if k == 0:
        return 0.0

    # If k is very large (larger than n/2), we can make as many transactions as we want
    # This is equivalent to capturing every upward movement
    if k >= n:
        total_profit = 0.0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                total_profit += float(prices[i] - prices[i - 1])
        return total_profit

    # Step 3: Use dynamic programming for the general case
    # Initialize arrays to track max profit
    # hold[i] represents the max profit with i transactions completed, currently holding a stock
    # sold[i] represents the max profit with i transactions completed, not holding a stock
    # We use k + 1 because we can have 0 to k transactions completed

    hold = [-float('inf')] * (k + 1)
    sold = [0.0] * (k + 1)

    # Step 4: Iterate through each day's price
    for current_price in prices:
        # Step 5: Iterate through transaction counts in reverse order
        # We go from k down to 1 to avoid using updated values from the same day
        for transaction_count in range(k, 0, -1):
            # Calculate the best way to complete the transaction_count-th transaction (sell)
            # We can either keep the previous sold state or sell from the hold state of (transaction_count - 1)
            potential_sell_profit = hold[transaction_count - 1] + current_price

            if potential_sell_profit > sold[transaction_count]:
                sold[transaction_count] = potential_sell_profit

            # Calculate the best way to start the transaction_count-th transaction (buy)
            # We can either