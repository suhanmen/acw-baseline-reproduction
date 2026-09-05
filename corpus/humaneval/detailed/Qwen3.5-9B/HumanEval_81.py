from typing import List, Union

Number = Union[int, float]

def _is_valid_grade_value(value: Number) -> bool:
    """
    Validates if a single grade value is numeric and within the expected range (0.0 to 4.0).
    While the problem statement implies a range starting at 0.0, real-world grading 
    systems typically cap at 4.0. Values above 4.0 are treated as invalid for this 
    specific grading scale interpretation, though strictly >0.0 is the lower bound 
    for D grades. We will enforce [0.0, 4.0] as the valid domain for this GPA table.
    """
    if not isinstance(value, (int, float)):
        return False

    # GPA is generally capped at 4.0 in most systems. 
    # If a value exceeds 4.0, it doesn't map to any grade in the provided table 
    # (the highest is A+ at exactly 4.0, and '> 3.7' covers A). 
    # We treat anything > 4.0 as invalid for this specific mapping logic 
    # to prevent undefined behavior (e.g., treating 5.0 as an infinite 'A').
    if value > 4.0:
        return False

    # The lowest grade is E for 0.0. Anything strictly less than 0.0 is invalid.
    if value < 0.0:
        return False

    return True

def _convert_gpa_to_letter(gpa: Number) -> str:
    """
    Converts a specific GPA number into its corresponding letter grade based on the provided table.
    Uses explicit conditional checks to ensure precision and readability.
    """
    # Exact match for A+
    if gpa == 4.0:
        return "A+"

    # Range checks: use '>' to match the problem description
    # Note: The problem uses '>' for lower bounds, implying the lower bound is exclusive 
    # for that specific grade, except for the base cases.
    # Let's trace: 
    # > 3.7 is A. Since 4.0 is caught above, values between 3.7 and 4.0 (exclusive of 4.0) become A.

    if gpa > 3.7:
        return "A"

    if gpa > 3.3:
        return "A-"

    if gpa > 3.0:
        return "B+"

    if gpa > 2.7:
        return "B"

    if gpa > 2.3:
        return "B-"

    if gpa > 2.0:
        return "C+"

    if gpa > 1.7:
        return "C"

    if gpa > 1.3:
        return "C-"

    if gpa > 1.0:
        return "D+"

    if gpa > 0.7:
        return "D"

    if gpa > 0.0:
        return "D-"

    # Exact match for E
    if gpa == 0.0:
        return "E"

    # This line should theoretically be unreachable if _is_valid_grade_value is used first
    raise ValueError(f"Unexpected GPA value: {gpa}. Did not map to any grade.")

def _validate_input_list(grades: List) -> List:
    """
    Validates the input list structure and individual elements.
    Raises specific exceptions for invalid structures or types.
    """
    # Check if the input is a list
    if not isinstance(grades, list):
        raise TypeError(f"Expected a list of grades, but received {type(grades).__name__}.")

    # Check for empty input
    if len(grades) == 0:
        return grades # Return empty list as valid output

    # Check each element
    for i, grade in enumerate(grades):
        if not _is_valid_grade_value(grade):
            raise ValueError(f"Invalid grade value at index {i}: {grade}. "
                             f"Grade must be a number between 0.0 and 4.0 inclusive.")

    return grades

def numerical_letter_grade(grades: List) -> List[str]:
    """
    Converts a list of numerical GPA grades into a list of letter grades.

    Args:
        grades: A list of numerical GPA values (int or float).

    Returns:
        A list of strings representing the letter grades corresponding to the input GPAs.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
        ValueError: If the input list is empty (handled gracefully as return of []) 
                     or if a grade value is out of the valid range (e.g., < 0 or > 4).
    """
    # Step 1: Validate the input list structure and contents
    validated_grades = _validate_input_list(grades)

    # Step 2: Initialize a list to store the resulting letter grades
    letter_grades: List[str] = []

    # Step 3: Iterate through each validated grade
    for gpa_value in validated_grades:
        # Step 4: Convert the individual GPA to a letter grade
        letter_grade = _convert_gpa_to_letter(gpa_value)

        # Step 5: Append the resulting letter grade to our list
        letter_grades.append(letter_grade)

    # Step 6: Return the final list of letter grades
    return letter_grades