def convert_list_dictionary(list1, list2, list3):
    result = []
    for i in range(len(list1)):
        dictionary_entry = {}
        key = list1[i]
        sub_dictionary = {}
        value = list3[i]
        for j in range(len(list2[i])):
            sub_key = list2[i][j]
            sub_dictionary[sub_key] = list3[i][j]
        dictionary_entry[key] = sub_dictionary
        result.append(dictionary_entry)
    return result