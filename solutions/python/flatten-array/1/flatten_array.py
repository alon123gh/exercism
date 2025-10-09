def flatten(iterable):
    stack = []
    flat_list = []
    stack.insert(0,iterable)
    while len(stack) > 0:
        element = stack.pop(0)
        if element is None:
            continue
        if isinstance(element, list):
           stack = element + stack
        else:
            flat_list.append(element)
    return flat_list