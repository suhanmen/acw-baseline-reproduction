def assign_freq(tuples_list):
    # Dictionary to hold the frequency of each tuple
    freq = {}
    # Count the frequency of each tuple
    for t in tuples_list:
        if t in freq:
            freq[t] += 1
        else:
            freq[t] = 1
    # Create the result list by appending the frequency to each tuple
    result = [ (k + (freq[k],)) for k in tuples_list ]
    return result