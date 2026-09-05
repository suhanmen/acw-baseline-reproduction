def convert_list_dictionary(list1, list2, list3):
    return [
        {key1: {key2: key3}}
        for key1, key2, key3 in zip(list1, list2, list3)
    ]