def first_even(nums):
    first_even = next((el for el in nums if el%2==0),-1)
    return first_even