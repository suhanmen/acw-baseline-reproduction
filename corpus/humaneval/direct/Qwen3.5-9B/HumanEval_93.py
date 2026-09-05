def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 

    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result = []
    for char in message:
        if char in vowels:
            if char.islower():
                shifted = chr(ord(char) + 2)
                result.append(shifted.upper())
            else:
                shifted = chr(ord(char) - 32 + 2)
                result.append(shifted)
        else:
            result.append(char.swapcase())
    return ''.join(result)