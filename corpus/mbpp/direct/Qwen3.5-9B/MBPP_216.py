def check_subset_list(nested1, nested2):
    def flatten(lst):
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list

    flat1 = set(flatten(nested1))
    flat2 = set(flatten(nested2))

    return flat1.issubset(flat2)