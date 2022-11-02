def reverse_list(array):
    if len(array) < 2:
        print('Size of array is less than two. No reversing can be done')
        return array
    reversed_list = []
    n = len(array)-1
    while n > -1:
        reversed_list.append(array[n])
        n -=1
    return reversed_list
