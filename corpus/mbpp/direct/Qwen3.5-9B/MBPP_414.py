def overlapping(seq1, seq2):
    return any(x in seq2 for x in seq1)