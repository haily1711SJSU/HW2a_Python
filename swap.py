def swap_list(array):
    temp = array[-1] #last element
    mid = (len(array)-1) // 2
    array[-1] = array[mid]
    array[mid] = temp
    return array
