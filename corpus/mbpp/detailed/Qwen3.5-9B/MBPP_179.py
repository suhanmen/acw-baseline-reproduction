from typing import List, Union

Number = Union[int, float]
# Note: While Keith numbers are conceptually defined for integers,
# we will accept floats, but the logic will treat them effectively as integers
# or validate if they have a fractional part that makes them unsuitable.
# However, the core definition applies to positive integers >= 2 usually.
# Let's handle the integer requirement strictly for the logic flow.

def _validate_input(value: Number) -> None:
    """
    Validates the input to ensure it is suitable for Keith number checking.

    Rules:
    1. Must be an integer (no fractional part).
    2. Must be non-negative. (Keith numbers are typically defined for positive integers,
       but 0 and 1 are edge cases. We will handle them explicitly below.
       Usually, Keith numbers are defined for n >= 2. However, some definitions include 
       trivial cases. We will check the sequence generation logic which naturally fails
       or requires special handling for single digits.
    3. Must not be negative.
    """
    # Check if the value is technically an integer
    if isinstance(value, float) and not value.is_integer():
        raise ValueError(f"Input {value} must be an integer, but has a fractional part.")

    # Convert to int for safe arithmetic operations
    if isinstance(value, float):
        value = int(value)

    n = value

    if n < 0:
        raise ValueError(f"Input {n} must be non-negative. Keith numbers are defined for non-negative integers.")

    if n < 0:
        raise ValueError("Negative numbers are not valid for Keith number checks.")

def _convert_to_digits(n: int) -> List[int]:
    """
    Converts a non-negative integer into a list of its digits in base 10.
    Digits are ordered from most significant to least significant.

    Edge cases handled:
    - n = 0: returns [0]
    """
    if n == 0:
        return [0]

    digits = []
    temp_n = n

    while temp_n > 0:
        current_digit = temp_n % 10
        digits.append(current_digit)
        temp_n = temp_n // 10

    # The digits were extracted in reverse order (least significant first)
    # Reverse them to get most significant first
    digits.reverse()

    return digits

def _generate_keith_sequence(digits: List[int]) -> bool:
    """
    Generates the Keith sequence based on the initial digits of the number.

    Logic:
    1. Start with the list of digits as the initial sequence.
    2. Calculate the next term by summing the last 'k' terms (where k is the number of digits).
    3. Check if this new term equals the original number.
    4. If yes, the number is a Keith number.
    5. If the sequence exceeds the number without matching, return False.

    Special Cases:
    - Single digit numbers: The next term is the digit itself. 
      Strictly speaking, a number is a Keith number if it appears in its own sequence.
      For a single digit 'd', the sequence starts [d]. The next term is d. 
      If d == n, it's found immediately.
      However, standard definition usually requires the sequence to grow and match n at a later step.
      BUT, looking at the examples:
      14 -> digits [1, 4]. Next = 1+4=5. Seq: [1, 4, 5]. Next = 4+5=9. Seq: [1, 4, 5, 9]. Next = 5+9=14. Match!
      12 -> digits [1, 2]. Next = 3. Seq: [1, 2, 3]. Next = 5. Seq: [1, 2, 3, 5]. Next = 8. ...
      197 -> digits [1, 9, 7]. Next = 17. Next = 26. Next = 50. Next = 93. Next = 163. Next = 319... Wait.
      Let's re-calculate 197 manually to ensure logic matches the assertion.
      Digits: 1, 9, 7
      Next = 1+9+7 = 17. Sequence: 1, 9, 7, 17
      Next = 9+7+17 = 33. Sequence: 1, 9, 7, 17, 33
      Next = 7+17+33 = 57. Sequence: 1, 9, 7, 17, 33, 57
      Next = 17+33+57 = 107. Sequence: ..., 107
      Next = 33+57+107 = 197. Match!

      So the logic is:
      sequence = digits
      while last element of sequence < n:
          next_val = sum(last k elements)
          append next_val
          if next_val == n: return True
          if next_val > n: return False
      Return False (or handle equality at start)

      Actually, we need to check if n appears in the generated sequence.
      Since the sequence is strictly increasing for k >= 2 (and n >= 10 usually),
      we can stop once we hit or exceed n.
    """
    k = len(digits)

    # If the number has only 1 digit
    if k == 1:
        # A single digit number is trivially "in" its sequence from the start?
        # Usually Keith numbers are defined for numbers where the sequence generates itself later.
        # However, mathematically, if the sequence starts [n], n is present.
        # But standard lists of Keith numbers (14, 197, 26, 39...) don't include single digits like 1, 2, 3, 4, 5, 6, 7, 8, 9.
        # Why? Because the definition implies the number must be the sum of the previous terms.
        # For n=1, digits=[1]. Previous terms needed? There are none.
        # For n=14, digits=[1, 4]. Previous terms 1, 4 sum to 5 != 14.
        # The number must appear as a sum of previous k terms.
        # If k=1, there are no previous terms to sum to form the current term (which is the first term).
        # So single digit numbers are NOT Keith numbers under the strict summation definition.
        return False

    # Initialize the sequence with the digits
    sequence = list(digits)

    # We need to generate terms until we reach or exceed n
    # The last k terms determine the next term
    current_last_k = sequence[-k:]

    while True:
        # Calculate the next term
        next_term = sum(current_last_k)

        # Check if we found the number
        if next_term == n:
            return True

        if next_term > n:
            return False

        # Update the sequence
        # We need to keep adding terms to the sequence to form the "last k" for the next iteration
        sequence.append(next_term)

        # The window of last k elements shifts by one
        # We can just slice the list or maintain a window. 
        # For clarity and explicit control flow, let's re-slice or manage the window.
        # Since we just appended next_term, the new last k are the last k elements of the new sequence.
        current_last_k = sequence[-k:]

def is_num_keith(n: Number) -> bool:
    """
    Determines if a given number is a Keith number.

    Steps:
    1. Validate input.
    2. Extract digits.
    3. Generate Keith sequence.
    4. Check for equality with original number.
    """

    # Validation
    _validate_input(n)

    # Convert to integer for processing
    num_int = int(n)

    # Handle the specific case of 0 or negative numbers after validation
    # Validation allows 0, but Keith logic typically requires positive integers >= 2.
    # If input is 0: digits = [0]. k=1. Returns False. Correct.
    # If input is negative: Raised in validate_input.

    # Get digits
    digits = _convert_to_digits(num_int)

    # Check if Keith number
    is_keith = _generate_keith_sequence(digits)

    return is_keith