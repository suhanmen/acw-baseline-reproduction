def intersection_array(arr1, arr2):
    # We use filter with a lambda function to find elements in arr1
    # that exist in arr2.
    # We use list() to convert the filter object back into a list.
    return list(filter(lambda x: x in arr2, arr1))