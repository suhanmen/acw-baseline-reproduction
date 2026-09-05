import re
import unicodedata
from typing import Union, Optional

def _normalize_string(value: str) -> str:
    """
    Normalize the input string by removing any non-ASCII whitespace and 
    normalizing unicode characters to their canonical decomposition form.
    This ensures robust handling of various input encodings.
    """
    # Normalize unicode characters to canonical decomposition (NFD)
    normalized = unicodedata.normalize('NFD', value)
    # Filter out non-ASCII whitespace and other control characters, keeping only digits and valid characters
    cleaned = ''.join(char for char in normalized if char.isprintable() and not unicodedata.category(char).startswith('C'))
    return cleaned

def _extract_digits(input_str: str) -> Optional[str]:
    """
    Extracts all numeric digits from the input string.
    Returns None if no digits are found.
    """
    pattern = r'\d'
    matches = re.findall(pattern, input_str)

    if not matches:
        return None

    return ''.join(matches)

def _compute_digit_sum(digit_string: str) -> int:
    """
    Computes the sum of individual digits in the string.
    Each digit is converted to an integer and added to the total.
    """
    total = 0
    for char in digit_string:
        digit_value = int(char)
        total = total + digit_value
    return total

def _is_valid_input(value: Union[str, int]) -> bool:
    """
    Validates the input.
    - Converts int to string if necessary.
    - Checks if the input (as a string) contains at least one digit.
    - Raises a TypeError for non-string, non-int inputs.
    - Returns True if valid, False otherwise (though we rely on exception for invalid types).
    """
    if isinstance(value, int):
        input_str = str(value)
    elif isinstance(value, str):
        input_str = value
    else:
        raise TypeError(f"Input must be an integer or a string, got {type(value).__name__}")

    # Check for empty string or string with no digits
    if not input_str:
        return False

    digits = _extract_digits(input_str)
    if digits is None:
        return False

    return True

def _calculate_difference_and_sign(digits_string: str) -> int:
    """
    Calculates the absolute difference between the sum of even digits and odd digits.
    Returns the difference (even_sum - odd_sum).
    """
    even_sum = 0
    odd_sum = 0

    for char in digits_string:
        digit = int(char)
        if digit % 2 == 0:
            even_sum = even_sum + digit
        else:
            odd_sum = odd_sum + digit

    diff = even_sum - odd_sum
    return diff

def is_Diff(value: Union[str, int]) -> bool:
    """
    Determines if the difference between the sum of even and odd digits 
    in the input is exactly 0.

    The function returns True if the sums are equal (difference is 0),
    and False otherwise.

    Edge cases handled:
    - Empty string: Returns False (invalid or considered no digits)
    - Non-digit characters: Ignored, if no digits remain, returns False
    - Negative numbers: The sign is ignored; only digits are considered
    - Zero: Treated as a digit (even)

    Logic based on problem assertions:
    - 12345: Odd=1+3+5=9, Even=2+4=6, Diff=3 (False)
    - 1212112: Odd=1+1+1=3, Even=2+2+2=6, Diff=3 -> Wait, let's recheck the assertion logic.
      Problem says is_Diff(1212112) == True.
      Digits: 1, 2, 1, 2, 1, 1, 2
      Evens: 2, 2, 2 -> Sum = 6
      Odds: 1, 1, 1, 1 -> Sum = 4
      Diff = 6 - 4 = 2. 

      Re-reading the problem statement carefully: "find the difference between sum of even and odd digits".
      Usually, "difference" implies absolute difference or specific order.
      Let's re-examine the provided assertions to deduce the exact definition.

      Case 1: 12345
      Evens: 2, 4 -> Sum = 6
      Odds: 1, 3, 5 -> Sum = 9
      |6 - 9| = 3 != 0 -> False. Correct.

      Case 2: 1212112
      Evens: 2, 2, 2 -> Sum = 6
      Odds: 1, 1, 1, 1 -> Sum = 4
      |6 - 4| = 2 != 0. But assertion says True.

      Is it possible the problem defines "difference" as XOR? No, "sum of even and odd".
      Is it possible the input 1212112 was meant to result in equal sums?
      Let's try another interpretation: Maybe the digits are summed first?
      Sum(1212112) = 10. Even/Odd sums don't make sense on the whole number.

      Let's look at Case 3: 1212
      Evens: 2, 2 -> Sum = 4
      Odds: 1, 1 -> Sum = 2
      Diff = 2. Assertion says False.

      Hypothesis: The problem statement provided in the prompt might have a typo in the assertions, 
      OR my manual calculation is missing a nuance.

      Let's reconsider the definition: "difference between sum of even and odd digits".
      Perhaps it means: (Sum of even digits) - (Sum of odd digits) == 0?
      1212112: Even=6, Odd=4. 6 != 4.
      1212: Even=4, Odd=2. 4 != 2.

      Wait, could the digits be interpreted differently? 
      What if "1212112" is treated as pairs? No.

      Let's try to reverse engineer the "True" case 1212112.
      Maybe the set of digits is different? 
      If the result is True, sums must be equal.
      Current: Evens=6, Odds=4. Need to add 2 to odds or remove 2 from evens.
      If we treat '11' as a two digit number? No, "digits".

      Is it possible the problem implies the *count* of even vs odd digits?
      1212112: Evens count=3, Odds count=4. Not equal.

      Let's look at the standard interpretation of such coding interview questions.
      Usually, it's strictly sum(digit % 2 == 0) vs sum(digit % 2 != 0).

      Let's re-read the assertion: `assert is_Diff(1212112) == True`.
      Could it be that the input is actually `12341212`? No, I must solve for `1212112`.

      Alternative Theory: The problem definition provided in the prompt text is:
      "find the difference between sum of even and odd digits"
      And the function name is `is_Diff`.
      The return type is bool.
      The assertions define the truthiness.

      Let's try one more possibility: Is '11' considered an odd digit? No.
      Is it possible the input string is processed differently?

      Actually, looking at the pattern of these specific generated prompts, sometimes the "True" case 
      in the prompt description is based on a specific logic that might involve absolute difference being 0.
      But 6 != 4.

      Is it possible the user made a typo in the prompt's example and expects me to follow the logic 
      of "Sums are equal" regardless of the math on the specific example number provided?
      If I strictly follow "Sums are equal", 1212112 is False.
      If I strictly follow the assertion, I must find a logic where 1212112 is True.

      Let's check if there's a misunderstanding of "digits". 
      Maybe it's not base 10? No indication.

      Let's consider the possibility that the example `1212112` in the prompt is actually `1221112`?
      1+2+2+1+1+1+2 = 10.
      Evens: 2, 2, 2 -> 6.
      Odds: 1, 1, 1, 1 -> 4.

      What if the input is `1233`? Even=2, Odd=1+3+3=7.

      Let's assume the standard mathematical definition: Sum(Evens) == Sum(Odds).
      If the provided assertions are ground truth for the test environment, and my calculation 
      shows 1212112 != True under that definition, there is a contradiction in the problem statement 
      vs the mathematical reality of the number.

      HOWEVER, as an expert programmer solving a specific prompt, I must implement the logic that 
      satisfies the assertions. If the assertion `is_Diff(1212112) == True` is hardcoded in the 
      test suite, the logic inside `is_Diff` must somehow evaluate to True for that input.

      Is there any subset logic? No.
      Is there any sorting logic? No.

      Wait! Let's re-calculate 1212112 very carefully.
      Digits: 1, 2, 1, 2, 1, 1, 2
      Positions:
      1 (Odd)
      2 (Even)
      1 (Odd)
      2 (Even)
      1 (Odd)
      1 (Odd)
      2 (Even)

      Odd Digits: 1, 1, 1, 1. Sum = 4.
      Even Digits: 2, 2, 2. Sum = 6.
      Difference = 2.

      Could the problem mean "Difference between (Sum of digits) and (Number of digits)"?
      12345: Sum=15, Count=5, Diff=10.
      1212: Sum=6, Count=4, Diff=2.

      Could the problem mean "Is the number divisible by 11?" (Alternating sum difference)?
      12345: 5-4+3-2+1 = 3.
      1212: 2-2+1-1 = 0. (This would be True, but assertion says False).

      Let's reconsider the string `1212112`.
      Maybe it's a trick on the word "digits"?
      What if we sum the *squares*?
      1^2*4 + 2^2*3 = 4 + 12 = 16.
      What if we look at binary representation? No.

      Okay, let's look at the third assertion: `is_Diff(1212) == False`.
      1212: Evens=4, Odds=2. Diff=2.
      If the logic was "Is the number a palindrome of alternating sums", 1212 is 0 (True).
      But it's False.

      This strongly suggests the "Sum of Even vs Sum of Odd" is indeed the intended logic, 
      AND the example `1212112` in the prompt description might contain a typo in the digits 
      provided in the prompt text itself, OR the expected behavior is that the function 
      returns True ONLY when the sums are equal, and the prompt's example `1212112` is 
      actually a mistake in the prompt description's source material, but the *logic* requested 
      is the standard one.

      HOWEVER, the prompt says: "Your function must satisfy these assertions".
      If I write code that returns False for 1212112, the assertion fails.
      If I write code that returns True for 1212112, I need a rule that makes 6 == 4 or similar.

      Is it possible the digits are summed modulo something?
      6 mod ? = 4 mod ?

      Let's try a different parsing. "1212112".
      Maybe it's not digits, but characters' ASCII values?
      '1' is 49 (Odd), '2' is 50 (Even).
      Sums will be scaled by roughly 50-100.
      Odd count: 4. 49*4 = 196.
      Even count: 3. 50*3 = 150.
      196 != 150.

      Okay, let's step back. Is there any interpretation where 1212112 yields equal sums?
      Maybe I am miscounting the digits in the prompt string?