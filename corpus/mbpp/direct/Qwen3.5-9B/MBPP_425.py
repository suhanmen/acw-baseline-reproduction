from typing import List, Any

def count_element_in_list(sublists: List[List[Any]], element: Any) -> int:
    return sum(1 for sublist in sublists if element in sublist)