#InsertionSort
unsorted_list = [10, 8, 5, 6, 4, 2, 4, 2, 1]
def insertionSort(l):
    sorted_list = []
    while(len(l) > 0):
        smallest = l[0]
        smallest_index = 0
        for index, elem in enumerate(l):
            if elem < smallest:
                smallest = elem
                smallest_index = index
        unsorted_list.pop(smallest_index)
        sorted_list.append(smallest)
    return sorted_list
print(insertionSort(unsorted_list))