def count_occurance(s: str) -> int:
    """
    Finds the occurrence of the substring 'std' in a given string.
    """
    count = 0
    start = 0
    while True:
        start = s.find('std', start)
        if start == -1:
            break
        count += 1
        start += 3
    return count

if __name__ == "__main__":
    assert count_occurance("letstdlenstdporstd") == 3
    assert count_occurance("truststdsolensporsd") == 1
    assert count_occurance("makestdsostdworthit") == 2