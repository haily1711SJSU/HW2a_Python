def reverse_list(array):
    reversed_list = []
    for i in reversed(array):
        reversed_list.append(i)
    return reversed_list

def main():
    arr = []
    print(reverse_list(arr))

main()
