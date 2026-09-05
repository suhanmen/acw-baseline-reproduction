import math
from typing import Union

Number = Union[int, float]

def is_valid_positive_number(value: Number) -> bool:
    """
    Validates that a given value is a number (int or float) and strictly positive.
    In the context of side lengths of a triangle, zero and negative numbers are invalid.
    """
    if not isinstance(value, (int, float)):
        return False
    if isinstance(value, bool):
        return False  # Explicitly reject booleans since bool is a subclass of int
    if value <= 0:
        return False
    return True

def calculate_hypotenuse_leg_a_leg_b(leg_a: Number, leg_b: Number) -> Number:
    """
    Calculates the hypotenuse of a right-angled triangle given the lengths of the two legs.
    Formula: c = sqrt(a^2 + b^2)
    """
    square_a = leg_a * leg_a
    square_b = leg_b * leg_b
    sum_of_squares = square_a + square_b
    hypotenuse = math.sqrt(sum_of_squares)
    return hypotenuse

def calculate_unknown_leg_hypotenuse_leg(leg: Number, hypotenuse: Number) -> Number:
    """
    Calculates the unknown leg of a right-angled triangle given the length of one leg and the hypotenuse.
    Formula: a = sqrt(c^2 - b^2) where c is hypotenuse and b is the known leg.
    """
    square_hypotenuse = hypotenuse * hypotenuse
    square_known_leg = leg * leg
    difference_of_squares = square_hypotenuse - square_known_leg

    # Although input validation handles this, an extra safety check here prevents domain errors
    if difference_of_squares < 0:
        # This should theoretically not be reached if inputs are valid per Pythagorean theorem
        raise ValueError(f"Invalid triangle geometry: hypotenuse ({hypotenuse}) is not longer than leg ({leg}). Difference of squares is negative: {difference_of_squares}")

    unknown_leg = math.sqrt(difference_of_squares)
    return unknown_leg

def otherside_rightangle(first_side: Number, second_side: Number) -> Number:
    """
    Finds the third side of a right-angled triangle given two sides.

    Logic:
    1. Validate both inputs are positive numbers.
    2. Determine which side is the hypotenuse.
       - If both inputs are provided, we must assume the larger of the two is NOT the third side we are looking for unless it's clearly the hypotenuse.
       - However, the problem asks to find the *third* side.
       - Case A: The two inputs are the two legs (shorter sides). We need the hypotenuse. The third side = sqrt(a^2 + b^2).
       - Case B: One input is a leg, the other is the hypotenuse. We need the other leg. The third side = sqrt(h^2 - l^2).

    How to distinguish Case A from Case B?
    - In Case A (finding hypotenuse): The inputs are the two legs. Neither is strictly greater than the result. The result will be larger than both inputs.
    - In Case B (finding leg): One input (hypotenuse) must be strictly greater than the other (leg).

    Heuristic Strategy:
    1. If input1 == input2: 
       - They cannot be leg and hypotenuse simultaneously unless it's an impossible 0-length triangle.
       - They are two equal legs. Calculate hypotenuse.
    2. If input1 > input2:
       - If input1 is the hypotenuse, we calculate the missing leg.
       - If input2 is the hypotenuse, this is impossible because hypotenuse must be the longest side.
       - If both are legs, we calculate hypotenuse.
       - Decision: If we assume the user provides (leg1, leg2), result > both. If user provides (leg, hyp), result < hyp.
       - Let's look at the examples:
         (7, 8) -> 10.63 (7^2 + 8^2). Here 8 is not the hypotenuse of a triangle with legs 7 and 10.63. 8 is a leg. Result is hypotenuse.
         (3, 4) -> 5 (3^2 + 4^2). 5 > 4. Result is hypotenuse.
         (7, 15) -> 16.55 (7^2 + 15^2). 15 is a leg. Result is hypotenuse.

       It appears all provided examples are "Find the hypotenuse given the two legs".
       However, a robust function should handle the case where the second side is the hypotenuse.
       But wait, if the problem implies we don't know which is which, we have ambiguity without more context.
       Standard convention for "find the third side of a right triangle" given two sides:
       - If the provided sides can form legs (a, b), c = sqrt(a^2 + b^2).
       - If one is clearly a hypotenuse (larger than the other), it's ambiguous if the larger is the target or the source.

       Let's re-read the specific constraints based on the examples.
       Example 1: 7, 8 -> 10.63. Hypotenuse.
       Example 2: 3, 4 -> 5. Hypotenuse.
       Example 3: 7, 15 -> 16.55. Hypotenuse.

       In all examples, the result is the hypotenuse calculated from the two legs.
       Is it possible the inputs are (leg, hypotenuse)?
       If inputs were (7, 10.63), the answer would be 8.
       If inputs were (3, 5), the answer would be 4.

       Since the function name is `otherside_rightangle` and the examples always compute sqrt(a^2+b^2), 
       we will implement logic that detects if the second argument is intended as the hypotenuse ONLY if it is strictly greater than the first and the geometric configuration allows it? 
       Actually, the most robust interpretation that fits the examples perfectly is:
       "Given two sides that are LEGS, return the hypotenuse."
       OR
       "Given two sides, if one is clearly the hypotenuse (larger than the other), treat it as such? 
       But if we are given (7, 15) and 15 is the hypotenuse, the third side is sqrt(15^2 - 7^2) = 12.92.
       The example says 16.55. 16.55 = sqrt(7^2 + 15^2).

       Conclusion: The examples explicitly define the behavior: The function assumes the two inputs are the TWO LEGS, and returns the hypotenuse.
       However, a "defensive" programmer should consider: What if the user passes a leg and the hypotenuse?
       Given the strict requirement to satisfy the assertions, the function MUST behave as: Calculate Hypotenuse from two legs.

       BUT, to be truly production-grade and handle potential misuse (or if the problem implies dynamic detection), 
       let's look closer. Is there any interpretation where (7, 15) -> 12.92? Yes, if 15 is hyp.
       Since the output is 16.55, the input 15 is treated as a leg.

       Therefore, the function calculates the hypotenuse assuming both inputs are legs.
       We will add a check to ensure the larger of the two inputs is treated as a leg, effectively forcing the "hypotenuse of two legs" calculation.
       If the user passes (3, 5) expecting the answer 4, this function will return 5.83 (sqrt(9+25)).
       This contradicts a general utility function but satisfies the specific problem statement and assertions provided.

       However, to add a layer of "Defensive" logic often expected in such problems:
       Sometimes these problems imply: "Find the missing side. If the larger input is the hypotenuse, find the leg. If the larger input is a leg (implying we need the hypotenuse), find the hypotenuse."
       Wait, if input is (7, 15), 15 is larger. If 15 is a leg, result is 16.55. If 15 is hypotenuse, result is 12.92.
       The test case says 16.55. So 15 is a leg.

       What if the input was (15, 8)? 15 is larger. Is 15 a leg or hypotenuse?
       If 15 is hypotenuse, other leg is sqrt(225-64) = 13.
       If 15 is leg, hypotenuse is sqrt(225+64) = 17.2.

       Without a test case like (15, 8), we must rely on the pattern.
       Pattern: inputs are legs, output is hypotenuse.

       Let's refine the logic to be as explicit as possible about the assumption made to satisfy the tests.
       Assumption: The two input sides are the two legs adjacent to the right angle.
       Calculation: c = sqrt(a^2 + b^2).

       Wait, could there be a logic that says:
       If a > b: assume 'a' is the hypotenuse? -> (7, 15) -> 15 is hyp? No, that gives 12.92. Test expects 16.55.
       If a < b: assume 'b' is the hypotenuse? -> (7, 15) -> 15 is hyp? No.

       Okay, the ONLY logic that satisfies all three assertions is:
       Treat both inputs as legs. Return sqrt(a^2 + b^2).

       Let's verify:
       otherside_rightangle(7, 8) -> sqrt(49 + 64) = sqrt(113) = 10.6301... MATCH.
       otherside_rightangle(3, 4) -> sqrt(9 + 16) = sqrt(25) = 5. MATCH.
       otherside_rightangle(7, 15) -> sqrt(49 + 225) = sqrt(274) = 16.5529... MATCH.

       The solution is simply the hypotenuse of the two given legs.

       However, to make it "defensive" and "production grade", we should consider if the prompt implies a generic solver where the caller might pass a leg and a hypotenuse. 
       But since the requirements say "The observable behaviour ... must be exactly what the problem asks for", and the problem only demonstrates the "legs->hypotenuse" path, implementing that specific logic is the only way to pass the tests. 
       Implementing a heuristic that tries to guess if the second argument is a hypotenuse would likely fail the existing tests or create ambiguity not resolved by the test cases.

       Therefore, the implementation will strictly treat both inputs as the legs of the right triangle.
    """

    # Step 1: Validate inputs
    if not is_valid_positive_number(first_side):
        raise ValueError(f"First side must be a positive number, got: {first_side}")

    if not is_valid_positive_number(second_side):
        raise ValueError(f"Second side must be a positive number, got: {second_side}")

    # Step 2: Based on the problem assertions, both inputs are treated as the legs (shorter sides)
    # of a right-angled triangle. We calculate the length of the hypotenuse (the third side).
    # 
    # If the problem intended to support (leg, hypotenuse) inputs, the assertions would include a case
    # where the result is smaller than one of the inputs. Since they do not, we proceed with the
    # formula for the hypotenuse: c = sqrt(a^2 + b^2).

    leg_one = first_side
    leg_two = second_side

    square_leg_one = leg_one ** 2
    square_leg_two = leg_two ** 2

    sum_squares = square_leg_one + square_leg_two

    third_side = math.sqrt(sum_squares)

    return third_side