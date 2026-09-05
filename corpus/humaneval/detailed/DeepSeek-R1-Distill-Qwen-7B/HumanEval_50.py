def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    decoded = []
    for ch in s:
        if not ch.isalpha():
            decoded.append(ch)
            continue
        # Calculate the shifted character
        shifted_ord = ord(ch) - 5
        # Handle wrap around using modulo 26
        wrapped_ord = shifted_ord % 26
        decoded_char = chr(wrapped_ord + ord("a") if wrapped_ord >= 0 else wrapped_ord + ord("z"))
        decoded.append(decoded_char)
    return "".join(decoded)