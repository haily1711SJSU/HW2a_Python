def swap_list(array):
    if len(array) < 2:
        print('Size of array is less than two. No swapping can be done')
        return array
    temp = array[-1] #last element
    mid = (len(array)-1) // 2
    array[-1] = array[mid]
    array[mid] = temp
    return array