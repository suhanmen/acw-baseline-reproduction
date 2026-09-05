from operator import itemgetter

def index_on_inner_list(list_of_lists, index):
    return sorted(list_of_lists, key=itemgetter(index))