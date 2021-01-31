#Binary search: RECURSIVE METHOD
#locates the index of a given number inside an array using
arr = [2,4,8,5,6,9,1,8]
k = 9

def BinarySearch(arr,k):
    low = 0
    high = len(arr)-1 # -1 because 0 is already set as low.
    found = False
    while low <= high and not found:
        mid = (low + high) // 2 # use //2 instead of /2 to avoid float error.
        if arr[mid] == k:
            found = True
        else:
            if k < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    print('Lenght of array: ' ,len(arr)-1)
    print('Number' , k , 'is located at index' , mid )

BinarySearch(arr,k)

# Another way of doing it would be using ITERATIVE METHOD.
# This method takes more time than the recursive method. Its time complexity
# is higher.

arr = [10, 20, 80, 30, 60, 50,
                     110, 100, 130, 170]
k = 170
n = len(arr)

def func(arr,k,n):
    for i in range(0,n):
        if arr[i] == k:
            print (i)


#Turns decimal to binary recursively by printing out remainders
def toBinary(n):
    if n > 1:
        toBinary(n //2)
    remainder = n % 2

    print(remainder, end='')

n = 127
toBinary(n)



