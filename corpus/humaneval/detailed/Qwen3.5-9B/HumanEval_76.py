from typing import Union

def is_simple_power(x: Union[int, float], n: Union[int, float]) -> bool:
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """

    # Helper function to validate and normalize input to integer
    def _normalize_number(val: Union[int, float]) -> int:
        if not isinstance(val, (int, float)):
            raise TypeError(f"Input must be a number, got {type(val).__name__}")

        # Check for NaN
        if isinstance(val, float) and (val != val):  # NaN check
            raise ValueError("Input cannot be NaN")

        # Check for infinity
        if isinstance(val, float) and (val == float('inf') or val == float('-inf')):
            raise ValueError("Input cannot be infinity")

        # Convert to integer if it is a float with no fractional part
        if isinstance(val, float):
            if abs(val - round(val)) > 1e-9:  # Check for non-integer float
                raise ValueError(f"Input must be an integer value, got {val}")
            val = int(val)

        # Check if the integer is within a reasonable range for this problem context
        # While Python handles large integers, typical power problems assume standard integer ranges.
        # We will proceed with the integer as validated.

        return val

    # Helper function to calculate logarithm base n of x safely
    def _calculate_power_step(x_int: int, n_int: int) -> Union[int, float]:
        """
        Attempts to find integer k such that n_int ** k == x_int.
        Returns k if found, otherwise returns None.
        Uses logarithmic approach for initial estimation and iterative verification.
        """
        # Base case: if x is 1, then n^0 = 1 for any non-zero n.
        if x_int == 1:
            # 0 is a valid integer power: n^0 = 1
            return 0

        # Handle case where n is 1: 1^k is always 1.
        # Since x != 1 (checked above), no integer k exists such that 1^k = x.
        if n_int == 1:
            return None

        # Handle negative bases carefully.
        # If x is negative, n must be negative and the exponent must be an odd integer.
        # If x is positive, n can be negative only if exponent is even.

        # Determine the sign of x
        x_is_negative = (x_int < 0)

        # Determine the sign of n
        n_is_negative = (n_int < 0)

        # If x is negative and n is non-negative, impossible.
        if x_is_negative and not n_is_negative:
            return None

        # If x is positive and n is negative, the exponent MUST be even.
        if not x_is_negative and n_is_negative:
            # We will look for an even solution.
            pass

        # If x is negative and n is negative, the exponent MUST be odd.
        if x_is_negative and n_is_negative:
            pass

        # Calculate the magnitude of x and n
        x_abs = abs(x_int)
        n_abs = abs(n_int)

        # If |n| is 0 or 1, we already handled n=1.
        # If |n| is 0: 0^k = 0 for k>0, undefined or 1 for k=0 (depending on definition), 
        # but typically 0^k = 0 for k>=1. 
        # If x_abs is 0, then n^k = 0 implies k > 0 (since n!=0).
        if n_abs == 0:
            if x_abs == 0:
                # Any positive integer power of 0 is 0.
                # We can return 1 as a representative valid integer power.
                return 1
            else:
                # 0^k cannot be non-zero
                return None

        # If x_abs is 0, then n^k = 0 implies k > 0.
        if x_abs == 0:
            # Since n_abs != 0 (checked above), n^k can be 0 only if k > 0 and n=0.
            # But we are in the block where n_abs != 0.
            # Actually, if n_abs != 0, n^k can never be 0.
            return None

        # For x_abs > 0 and n_abs > 0:
        # We need to find k such that n_abs^k = x_abs.
        # Use logarithms to estimate k.
        # k = log(x_abs) / log(n_abs)
        import math

        try:
            log_x = math.log(x_abs)
            log_n = math.log(n_abs)
            estimated_k = log_x / log_n
        except (ValueError, ZeroDivisionError):
            # log of non-positive numbers or division by zero (log(1)=0 handled separately usually)
            # Note: log(1) = 0, so if n_abs=1, we returned early.
            return None

        # Round the estimated k to the nearest integer to check candidates
        candidate_k = round(estimated_k)

        # Check a small range around the candidate because of floating point inaccuracies
        # Candidates: candidate_k - 1, candidate_k, candidate_k + 1
        for k_test in [candidate_k - 1, candidate_k, candidate_k + 1]:
            if k_test < 0:
                continue

            # Verify by direct multiplication (power calculation)
            # Use pow with integers to avoid float precision issues for exact match
            try:
                calculated_value = pow(n_abs, k_test)
                if calculated_value == x_abs:
                    # Found a match in magnitudes.
                    # Now check the sign constraints again to ensure the original equation holds.

                    # Constraint 1: If n was negative, k_test must satisfy the sign of x.
                    if n_int < 0:
                        # If n is negative, n^k has sign (-1)^k
                        # If x is positive, k must be even.
                        # If x is negative, k must be odd.
                        if (x_int > 0 and k_test % 2 != 0) or (x_int < 0 and k_test % 2 == 0):
                            continue

                    # Constraint 2: If x was negative, n must be negative (already checked above).
                    # Constraint 3: If x was positive, n can be anything (checked above).

                    # If all checks pass, we found a valid integer power.
                    return k_test

            except OverflowError:
                # If the power is too large, it definitely doesn't equal x_abs (assuming x is normal int)
                continue

    try:
        n_normalized = _normalize_number(n)
        x_normalized = _normalize_number(x)
    except (TypeError, ValueError) as e:
        # If normalization fails (e.g., NaN, Inf, non-numeric), we return False 
        # based on the problem context implying valid numeric inputs, 
        # but strictly speaking, invalid inputs shouldn't return True.
        # However, the prompt asks to "return true if... false in other cases".
        # Returning False for invalid types is a safe defensive default.
        return False

    result_k = _calculate_power_step(x_normalized, n_normalized)

    # If _calculate_power_step returns a valid integer k, then x is a simple power of n.
    if result_k is not None:
        return True
    else:
        return False