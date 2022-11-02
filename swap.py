def swap_list(array):
    if isinstance(array, list) == False: #test if input is not an array
        return "input is not a list"
    if len(array) == 0: #array must not be empty for func to work
        return array
    temp = array[-1] #last element
    mid = (len(array)-1) // 2
    array[-1] = array[mid]
    array[mid] = temp
    return array