"""Example of different types of algorithms and their order of growth"""
"""Complexity: Log , Linear , Quadratic , Exponential"""

# Iterative algorithm with an order of growth O (b) linear
def exp1 (a ,b):
    ans = 1
    while b > 0:
        ans *= a
        b -= 1
    return ans



# Recursive algorithm with an order of growth O(b) linear
def exp2 (a, b):
    if b == 1:
        return a
    else: return a * exp2(a ,b-1)



# Logarithmic algorithm with an order of growth O(log b)
def exp3(a ,b):
    if b == 1:
        return a
    if (b % 2) * 2 == b:
        return exp3(a * a , b/2)
    else: return a * exp3(a ,b-1)



# Quadratic algorithm with an order of growth of O(n**2)
def g(n ,m):
    x = 0
    for i in range (n):
        for j in range(m):
            x += 1
    return x


# Exponential algorithm with an order of growth O(2**n)
def Towers_of_hanoi(size ,fromStack ,toStack ,spareStack):
    if size == 1:
        print('move disk from' , fromStack , 'to' , toStack)
    else:
        Towers_of_hanoi(size-1 ,fromStack ,spareStack, toStack)
        Towers_of_hanoi(1 ,fromStack ,toStack ,spareStack)
        Towers_of_hanoi(size-1, spareStack ,toStack ,fromStack)



# Liner algorithm with order of growth O(len(s))
def serach(s ,e):
    answer = None
    i = 0
    numCompares = 0
    while i < len(s):
        numCompares += 1
        if e == s[i]:
            answer = True
        elif e < s[i]:
            answer = False
        i += 1
    print(answer , numCompares)


# Logarithmic algorithm with order of growth O(log)
def bsearch(s ,e ,first ,last):
    print(first ,last)
    if last - first < 2:
        return s[first] == e or s[last] == e
    mid = first ( first - last) // 2
    if s[mid] == e:
        return True
    if s[mid] > e:
        return bsearch(s ,e ,first ,mid -1)
    return bsearch(s ,e , mid + 1 ,last)

