def _is_prime(n):
    """
    Determine if a non-negative integer n is a prime number.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    # Check for non-positive integers
    if n <= 1:
        return False

    # 2 and 3 are prime numbers
    if n <= 3:
        return True

    # Check for divisibility by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check for divisibility up to the square root of n
    # We use the form 6k ± 1 because all primes greater than 3 fit this pattern
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def _split_sentence_into_words(sentence):
    """
    Split a sentence string into a list of individual words.

    Words are defined as contiguous sequences of characters separated by one or more spaces.
    Leading and trailing whitespace is ignored.

    Args:
        sentence (str): The input sentence string.

    Returns:
        list[str]: A list of words extracted from the sentence.
    """
    # Using split without arguments handles multiple spaces and strips leading/trailing whitespace
    return sentence.split()


def _filter_words_by_prime_length(words):
    """
    Filter a list of words, keeping only those whose length is a prime number.

    Args:
        words (list[str]): The list of words to filter.

    Returns:
        list[str]: A new list containing only words with prime lengths.
    """
    prime_length_words = []

    for word in words:
        word_length = len(word)

        if _is_prime(word_length):
            prime_length_words.append(word)

    return prime_length_words


def _join_words_into_string(words):
    """
    Join a list of words into a single string separated by spaces.

    Args:
        words (list[str]): The list of words to join.

    Returns:
        str: The resulting string with words separated by spaces.
    """
    return " ".join(words)


def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    # Validate the input type: it must be a string
    if not isinstance(sentence, str):
        raise TypeError(f"Expected string input, but got {type(sentence).__name__}")

    # Validate the input length against the lower bound constraint
    if len(sentence) < 1:
        raise ValueError(f"Input sentence length must be at least 1, but got {len(sentence)}")

    # Validate the input length against the upper bound constraint
    if len(sentence) > 100:
        raise ValueError(f"Input sentence length must not exceed 100, but got {len(sentence)}")

    # Validate that the sentence contains only letters and spaces
    # According to constraints: "sentence contains only letters"
    # However, splitting implies spaces are allowed separators.
    # We will enforce that characters are either alphabetic or whitespace.
    for char in sentence:
        if not (char.isalpha() or char.isspace()):
            raise ValueError(f"Input sentence contains invalid character: '{char}'")

    # Step 1: Split the sentence into individual words
    words_list = _split_sentence_into_words(sentence)

    # Step 2: Filter words to keep only those with prime lengths
    filtered_words_list = _filter_words_by_prime_length(words_list)

    # Step 3: Join the filtered words back into a single string
    result_string = _join_words_into_string(filtered_words_list)

    return result_string