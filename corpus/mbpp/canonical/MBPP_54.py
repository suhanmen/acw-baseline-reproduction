def counting_sort(my_list):
    max_value = 0
    for i in range(len(my_list)):
        if my_list[i] > max_value:
            max_value = my_list[i]
    buckets = [0] * (max_value + 1)
    for i in my_list:
        buckets[i] += 1
    i = 0
    for j in range(max_value + 1):
         for a in range(buckets[j]):
             my_list[i] = j
             i += 1
    return my_list