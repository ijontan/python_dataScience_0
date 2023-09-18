def ft_filter(function, list):
    """filter function"""
    if function is None:
        return [i for i in list if i is True]
    return [i for i in list if function(i) is True]
