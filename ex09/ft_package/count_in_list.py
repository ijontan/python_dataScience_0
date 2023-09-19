def count_in_list(lst: list, item: object):
    """count in list"""
    count = 0
    for i in lst:
        if i == item:
            count += 1
    return count
