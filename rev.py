def reverse_list(array):
    if isinstance(array, list) == False:
        return "input is not a list"
    reversed_list = []
    for i in reversed(array):
        reversed_list.append(i)
    return reversed_list