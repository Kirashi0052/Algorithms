#binarySearchAlgorithm
testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binarySearch(l, s):
    first = 0
    last = len(l) - 1
    found = False
    while(not found and first <= last):
        mid = (first + last) // 2
        if l[mid] == s:
            found = True
            return found
        else:
            if s > l[mid]:
                first = mid + 1
            else:
                last = mid - 1
    return found
