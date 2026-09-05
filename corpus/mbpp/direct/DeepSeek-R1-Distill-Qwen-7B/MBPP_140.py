def extract_singly(tuples):
    elements = {}
    for tpl in tuples:
        for elem in tpl:
            if elem in elements:
                elements[elem] = 'double'
            else:
                elements[elem] = 'single'
    singles = [k for k, v in elements.items() if v == 'single']
    return tuple(singles)