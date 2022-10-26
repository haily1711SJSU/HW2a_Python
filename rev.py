
def reverse_list(array):
    reversed_list = []
    for i in reversed(array):
        reversed_list.append(i)
    return reversed_list

#for testing 
def main():
    nums = [1, True, 9, 'Hi', 3]
    print(reverse_list(nums))

main()

