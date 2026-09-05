def string_to_list(s: str) -> list:
    """
    Converts a string into a list of words separated by whitespace.
    """
    return s.split()

if __name__ == "__main__":
    assert string_to_list("python programming") == ['python', 'programming']
    assert string_to_list("lists tuples strings") == ['lists', 'tuples', 'strings']
    assert string_to_list("write a program") == ['write', 'a', 'program']