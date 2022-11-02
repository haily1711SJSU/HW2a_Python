def swap_list(array):
    if isinstance(array, list) == False: #test if input is not an array
        return "input is not a list"
    if len(array) < 2:
        print('Size of array is less than two. No swapping can be done')
        return array
    temp = array[-1] #last element
    mid = (len(array)-1) // 2
    array[-1] = array[mid]
    array[mid] = temp
    return array

arr = [1,2,3,4,5,6]
print(swap_list(arr))