"""Binary search, Bubble search and Selection serarch"""

L = [3,2,5,8,1,7,9,6,4]

#Binary search
def bsearch(s ,e ,first ,last ,calls):
    print(first ,last)
    if last - first < 2:
        return s[first] == e or s[last] == e
    mid = first + ( first - last) // 2
    if s[mid] == e:
        return True
    if s[mid] > e:
        return bsearch(s ,e ,first ,mid -1 , calls+1)
    return bsearch(s ,e , mid + 1 ,last ,calls+1)


#Selection search
def selSort(L):
    for i in range(len(L )):
        print(L)
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j = j + 1
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp


#Bubble search
"""the problem with the bubble sort algo is that if it has finished ordering the list,
 it will keep on running until it reaches the end of the list"""
def bubbleSort(L):
    for j in range(len(L)):
        print(L)
        for i in range(len(L)-1):
            if L[i] > L[i + 1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
"""to avoid that, break the loop when there are no more swaps left to do"""
def bubbleSortV2(L):
    swapped = True
    while swapped:
        swapped = False
        print(L)
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                swapped = True



print('*'*100)
print('Selection Sort')
print(selSort(L))
print('*'*100)
print('Bubble sort')
print(bubbleSort(L))
print('*'*100)
print('Bubble Sort with stop')
print(bubbleSortV2(L))