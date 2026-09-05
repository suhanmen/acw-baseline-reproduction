def subject_marks(marks_list):
    """
    Sorts a list of tuples containing subjects and marks based on the marks
    in ascending order using a lambda function.
    """
    return sorted(marks_list, key=lambda x: x[1])