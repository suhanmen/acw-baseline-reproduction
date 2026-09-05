from typing import List, Optional, Tuple, Union

Number = Union[int, float]


def _validate_input(array: List[Number], length: int) -> None:
    """
    Validate the input arguments to ensure they meet the problem constraints.

    Raises:
        ValueError: If the input list is None, length is invalid, or length exceeds list bounds.
        TypeError: If the input list contains non-numeric elements.
    """
    if array is None:
        raise ValueError("Input list cannot be None.")

    if not isinstance(array, list):
        raise TypeError(f"Input must be a list, but got {type(array).__name__}.")

    if length <= 0:
        raise ValueError("The subsequence length must be a positive integer.")

    actual_length = len(array)

    if actual_length == 0:
        raise ValueError("Input list cannot be empty if length is required.")

    if length > actual_length:
        raise ValueError(
            f"Requested subsequence length ({length}) exceeds array length ({actual_length})."
        )

    if not all(isinstance(x, (int, float)) for x in array):
        raise TypeError("All elements in the array must be numeric (int or float).")


def _find_max_product_increasing_subsequence(
    array: List[Number], length: int
) -> float:
    """
    Finds the maximum product formed by multiplying numbers of an increasing subsequence
    of the specified length from the given array.

    The subsequence must be strictly increasing based on index and value.
    Since we need the maximum product of a subsequence of a FIXED length, we must check
    all valid contiguous or non-contiguous subsequences of that specific length.

    However, re-reading the problem examples:
    1. [3, 100, 4, 5, 150, 6] length 6 -> 45000. 
       Product: 3 * 100 * 4 * 5 * 150 * 6 = 540,000? No.
       Let's check the example values again.
       3 * 100 * 4 * 5 * 150 * 6 = 540000.
       Wait, the example says 45000.
       45000 / 150 = 300.
       300 / (3*100*4*5*6) -> doesn't make sense.

       Let's re-calculate the example provided in the prompt manually to understand the logic.
       Example 1: [3, 100, 4, 5, 150, 6], length 6.
       The only subsequence of length 6 is the whole array.
       Product: 3 * 100 * 4 * 5 * 150 * 6 = 540,000.
       The expected output is 45,000.
       540,000 / 45,000 = 12.
       Where could a factor of 12 come from? Or maybe the logic is different.

       Is it possible the problem implies a contiguous subarray?
       If contiguous, the only subarray of length 6 is the whole array.

       Let's look at Example 2: [4, 42, 55, 68, 80], length 5.
       Whole array product: 4 * 42 * 55 * 68 * 80 = 50,265,600.
       Matches the expected output exactly.

       Let's look at Example 3: [10, 22, 9, 33, 21, 50, 41, 60], length 8.
       Whole array product: 10 * 22 * 9 * 33 * 21 * 50 * 41 * 60 = 217,800,000?
       Calculation:
       10*22 = 220
       220*9 = 1980
       1980*33 = 65340
       65340*21 = 1372140
       1372140*50 = 68607000
       68607000*41 = 2812887000
       2812887000*60 = 168,773,220,000.
       This is way bigger than 21,780,000.

       Let's re-read the prompt carefully: "maximum product formed by multiplying numbers of an increasing subsequence".
       Usually, "increasing subsequence" implies the values must be strictly increasing (value[i] < value[j] for i < j).
       If the requirement is that the subsequence itself must be increasing in value:

       Example 1: [3, 100, 4, 5, 150, 6], length 6.
       We need a subsequence of length 6 where values are increasing.
       Indices: 0, 1, 2, 3, 4, 5 -> Values: 3, 100, 4, 5, 150, 6.
       Is 3 < 100? Yes.
       Is 100 < 4? No.
       So the whole array is NOT an increasing subsequence.
       Therefore, we cannot take the whole array.
       But the problem asks for a subsequence of length 6.
       If the array has length 6, the only subsequence of length 6 is the array itself.
       If the array itself is not increasing, then there is NO increasing subsequence of length 6.
       In this case, what should the function return?

       Maybe the parameter 'length' in the function signature `max_product(array, length)` refers to the length of the input array, and we are finding the max product of *any* increasing subsequence within it?
       Let's check the assertions again.
       assert max_product([3, 100, 4, 5, 150, 6], 6) == 45000
       Here length=6 matches the array length.

       Let's reconsider the calculation for Example 1 yielding 45000.
       Possible increasing subsequences in [3, 100, 4, 5, 150, 6]:
       - [3, 100] (prod 300)
       - [3, 4, 5, 150] (prod 9000)
       - [3, 4, 5, 6] (prod 360)
       - [4, 5, 150] (prod 3000)
       - [3, 4, 5] (60)
       ...
       Is there a combination yielding 45000?
       45000 = 3 * 5 * 5 * 5 * 100? No.
       45000 = 3 * 5 * 150 * 20? No.
       Let's factor 45000: 45 * 1000 = (9*5) * (10*10*10) = 3^2 * 5 * 2 * 2^3 * 5^3 = 2^3 * 3^2 * 5^4.
       Available numbers: 3, 100 (2^2*5^2), 4 (2^2), 5, 150 (2*3*5^2), 6 (2*3).

       Try: 4 * 5 * 150 * 15? No 15.
       Try: 3 * 5 * 100 * ? -> 1500 * 30 = 45000. Is there a 30? No.
       Try: 4 * 150 * 5 * 15? No.

       Wait, let's look at the numbers again: 3, 100, 4, 5, 150, 6.
       Maybe the subsequence doesn't need to be contiguous, but the VALUES must be increasing? Yes, that's standard.
       And maybe the length parameter is NOT the length of the subsequence to find, but something else?
       "Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array."
       "Your function must satisfy these assertions: ... length 6 ... length 5 ... length 8"

       Hypothesis A: The second argument `length` specifies the EXACT length of the increasing subsequence we must find.
       If Example 1 has no increasing subsequence of length 6, it's an invalid input case or I am missing a subsequence.
       Let's list ALL increasing subsequences of length 4 in Ex 1:
       [3, 4, 5, 6] -> 360
       [3, 4, 5, 150] -> 9000
       [3, 4, 150] -> 1800 (len 3)
       [3, 5, 150] -> 2250
       [3, 5, 6] -> 90
       [4, 5, 150] -> 3000
       [4, 5, 6] -> 120
       [3, 4, 5] -> 60

       Is it possible the problem allows non-increasing? "increasing subsequence" usually means strictly increasing.
       What if "increasing" means non-decreasing (<=)?
       [3, 100, 4, 5, 150, 6] -> No duplicates, so same as strict.

       Let's re-calculate 3 * 100 * 4 * 5 * 150 * 6 = 540,000.
       Target: 45,000.
       Ratio: 12.
       Which numbers multiplied by 12 give 540,000?
       540000 / 12 = 45000.
       So we are missing a factor of 12, or multiplying by 1/12? No, we are taking a subset.
       If we take a subset, the product must be a divisor of the total product (if integers).
       45000 must be a divisor of 540000. Yes.
       540000 / 45000 = 12.
       This means the excluded numbers must have a product of 12.
       The excluded numbers would be a subset of {3, 100, 4, 5, 150, 6}.
       Can we find a subset of these numbers whose product is 12?
       3 * 4 = 12.
       So if we exclude {3, 4}, the remaining set is {100, 5, 150, 6}.
       Product: 100 * 5 * 150 * 6 = 450,000. Still too high.
       Wait, 540000 / (3*4) = 45000.
       So if we exclude 3 and 4, the product of the rest is 45000.
       Rest: 100, 5, 150, 6.
       Are they an increasing subsequence?
       Indices: 1 (100), 3 (5), 4 (150), 5 (6).
       Values: 100, 5, 150, 6.
       100 < 5? False. Not increasing.

       Let's try excluding 3 and 5. Product 15. 540000/15 = 36000. No.
       Let's try excluding 6 and 2? No 2.
       Let's try excluding 4 and 3? Product 12.
       Subset {100, 5, 150, 6}. Not increasing.

       Is it possible the problem is "Find the maximum product of a contiguous subarray of length `length` that is strictly increasing in values?"
       Ex 1: Length 6. Contiguous subarray of length 6 is the whole array. Not increasing. Fail.

       Let's reconsider the wording "increasing subsequence of that array".
       Could it be that the second parameter is NOT the length of the subsequence, but the length of the array?
       And the task is simply "Find the max product of ANY increasing subsequence"?
       Let's test this hypothesis.
       Ex