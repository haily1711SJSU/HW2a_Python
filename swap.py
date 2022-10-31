def swap_list(array):
    if len(array) == 0:
        return array
    temp = array[-1] #last element
    mid = (len(array)-1) // 2
    array[-1] = array[mid]
    array[mid] = temp
    return array

def main():
    arr = [3,35,11]
    print(swap_list(arr))

main()