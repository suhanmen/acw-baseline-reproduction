def check_greater(arr, num):
    for x in arr:
        if x > num:
            return 'No, entered number is less than those in the array'
    return 'Yes, the entered number is greater than those in the array'