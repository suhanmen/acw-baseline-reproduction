def index_on_inner_list(lst, index):
    return sorted(lst, key=lambda x: x[index])