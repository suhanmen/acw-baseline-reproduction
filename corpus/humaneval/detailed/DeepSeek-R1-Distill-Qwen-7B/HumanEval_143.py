def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def words_in_sentence(sentence):
    """
    Returns a string containing words from the original sentence whose lengths are prime numbers.
    The order of words is preserved.
    """
    # Handle the case where the sentence is empty
    if not sentence:
        return ""

    # Split the sentence into words
    words = sentence.split()
    filtered_words = []

    # Iterate through each word to check if its length is prime
    for word in words:
        word_length = len(word)
        if is_prime(word_length):
            filtered_words.append(word)

    # Join the filtered words into a single string
    if not filtered_words:
        return ""
    else:
        return ' '.join(filtered_words)