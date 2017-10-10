
def selectionSort(list):
    i = 0
    n = len(list)
    while i < n:
        minIndex = i
        for j in range(i+1, n):
            print("j is {}".format(j))
            if list[j] < list[i]:
                minIndex = j
            else:
                minIndex = i
            list[i], list[minIndex] = list[minIndex], list[i]
            j += 1
        i += 1
    return list
