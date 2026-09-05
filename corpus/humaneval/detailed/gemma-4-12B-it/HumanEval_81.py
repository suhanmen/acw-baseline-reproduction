from typing import List, Union

def get_single_grade(gpa: Union[int, float]) -> str:
    """
    Determines the letter grade for a single numerical GPA based on 
    specific threshold rules.

    The rules are interpreted as follows:
    - Exactly 4.0 -> A+
    - Greater than 3.7 -> A
    - Greater than 3.3 -> A-
    - Greater than 3.0 -> B+
    - Greater than 2.7 -> B
    - Greater than 2.3 -> B-
    - Greater than 2.0 -> C+
    - Greater than 1.7 -> C
    - Greater than 1.3 -> C-
    - Greater than 1.0 -> D+
    - Greater than 0.7 -> D
    - Greater than 0.0 -> D-
    - Exactly 0.0 -> E
    - Values < 0.0 are treated as 0.0 (E) or handled by validation.
    """
    # Ensure we are working with a float for consistent comparison
    score = float(gpa)

    # Rule: Exactly 4.0
    if score == 4.0:
        return "A+"

    # Rule: > 3.7
    if score > 3.7:
        return "A"

    # Rule: > 3.3
    if score > 3.3:
        return "A-"

    # Rule: > 3.0
    if score > 3.0:
        return "B+"

    # Rule: > 2.7
    if score > 2.7:
        return "B"

    # Rule: > 2.3
    if score > 2.3:
        return "B-"

    # Rule: > 2.0
    if score > 2.0:
        return "C+"

    # Rule: > 1.7
    if score > 1.7:
        return "C"

    # Rule: > 1.3
    if score > 1.3:
        return "C-"

    # Rule: > 1.0
    if score > 1.0:
        return "D+"

    # Rule: > 0.7
    if score > 0.7:
        return "D"

    # Rule: > 0.0
    if score > 0.0:
        return "D-"

    # Rule: 0.0 or effectively anything <= 0.0
    # Based on the table, 0.0 is E. 
    # If the input is negative, it falls into the lowest tier.
    return "E"

def numerical_letter_grade(grades: List[Union[int, float]]) -> List[str]:
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E


    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """
    # Defensive check: handle non-list inputs
    if not isinstance(grades, list):
        raise ValueError("Input must be a list of numerical grades.")

    # Handle empty list input
    if not grades:
        return []

    results = []

    for item in grades:
        # Validate that each item is a number (int or float)
        if not isinstance(item, (int, float)):
            raise TypeError(f"Found invalid grade type: {type(item)}. All grades must be numbers.")

        # Calculate the letter grade for the individual student
        letter_grade = get_single_grade(item)

        # Append to the resulting list
        results.append(letter_grade)

    return results