def extract_nth_element(tuples_list, n):
    return [tpl[n] if isinstance(tpl, tuple) else tpl[n] for tpl in tuples_list]