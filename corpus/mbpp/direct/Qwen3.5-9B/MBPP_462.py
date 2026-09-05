from typing import List, Any

def combinations_list(arr: List[Any]) -> List[List[Any]]:
    result = [[]]
    for item in arr:
        n = len(result)
        for i in range(n):
            result.append(result[i] + [item])
    return result