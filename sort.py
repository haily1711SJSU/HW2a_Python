def sort_dictionary(dict):
    if len(dict.keys()) < 2:
        print('Size of dictionary is less than two. No sorting can be done')
        return dict
    tuples = []
    # create a list of tuples ("name", phone num, age)
    for key,value in dict.items():
        tuples.append((key,value[0],value[1]))  
    # sort these tuples based on age, bubble sort
    sortedTuples = sortTuples(tuples)
    sorted_list = []
    # cannot remove age from a tuple
    # so create another list to exclude it
    for item in sortedTuples:
        sorted_list.append((item[0],item[1]))
    
    return sorted_list

def sortTuples(tuple): #bubble sort
    for i in range(len(tuple)):
        for n in range(i,len(tuple)):
            left = i
            right = n
            if tuple[left][2] > tuple[right][2]:
                tmp = tuple[left]
                tuple[left] = tuple[right]
                tuple[right] = tmp
            left += 1
    return tuple