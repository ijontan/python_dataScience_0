def ft_filter(function, list):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return [i for i in list if i is True]
    return [i for i in list if function(i) is True]
