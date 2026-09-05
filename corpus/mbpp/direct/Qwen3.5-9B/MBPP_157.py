from typing import List, Any

def encode_list(input_data: List[Any]) -> List[List[Any]]:
    result = []
    if not input_data:
        return result

    current_run = [input_data[0]]
    for item in input_data[1:]:
        if item == current_run[-1]:
            current_run.append(item)
        else:
            result.append([len(current_run), current_run[0]])
            current_run = [item]
    result.append([len(current_run), current_run[0]])
    return result