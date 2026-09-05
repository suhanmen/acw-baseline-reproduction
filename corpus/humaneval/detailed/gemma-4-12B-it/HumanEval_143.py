import math

def is_prime(n: int) -> bool:
    """
    Determines if a non-negative integer is a prime number.
    A prime number is a natural number greater than 1 that has no 
    positive divisors other than 1 and itself.
    """
    # Prime numbers must be greater than 1
    if n <= 1:
        return False

    # 2 and 3 are prime numbers
    if n <= 3:
        return True

    # Eliminate even numbers and multiples of 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check for factors from 5 up to the square root of n
    # We use the 6k +/- 1 rule for optimization
    limit = int(math.isqrt(n))
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def words_in_sentence(sentence: str) -> str:
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
    # Validate input types and basic constraints
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string.")

    if len(sentence) == 0:
        return ""

    # Split the sentence into individual words based on whitespace
    # Using .split() without arguments handles multiple spaces and 
    # leading/trailing whitespace correctly.
    raw_words = sentence.split()

    # List to store words that meet the prime length criteria
    filtered_words = []

    for word in raw_words:
        # Calculate the length of the current word
        word_length = len(word)

        # Check if the length of the word is a prime number
        if is_prime(word_length):
            filtered_words.append(word)

    # Join the filtered words back into a single string separated by spaces
    result_sentence = " ".join(filtered_words)

    return result_sentence