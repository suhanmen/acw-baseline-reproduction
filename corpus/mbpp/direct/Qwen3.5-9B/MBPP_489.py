from typing import List, Any

def frequency_Of_Largest(n: int, arr: List[Any]) -> int:
    if not arr:
        return 0
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    count = 0
    for num in arr:
        if num == max_value:
            count += 1
    return count