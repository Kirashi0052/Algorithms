import random
import time
def selection_sort(liste):
    for index in range(len(liste)):
        minimum_index = index
        for i in range(minimum_index+1, len(liste)):
            if liste[minimum_index] > liste[i]:
                minimum_index = i
        cache = liste[index]
        liste[index] = liste[minimum_index]
        liste[minimum_index] = cache
    return liste

if __name__ == "__main__":
    l = []
    for i in range(9999):
        l.append(random.randint(0,999))
    start = time.time() #is to track how long it takes to finish the algorithm
    print(selection_sort(l))
    end = time.time()
    print(end-start)
    