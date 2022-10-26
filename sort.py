from operator import itemgetter
def sort_dictionary(dict):
    tuples = []
    for key,value in dict.items():
        tuples.append((key,value[0],value[1]))  
    sortedTuples = sorted(tuples, key=lambda items: items[2])
    sorted_list = []
    for item in sortedTuples:
        sorted_list.append((item[0],item[1]))
    
    return sorted_list

def main():
    dict =  {'tom' : (5464512, 24) ,
     'Sara' : (5446987, 32) , 'Mary' : (1557896, 20)}
    print(sort_dictionary(dict))

main()