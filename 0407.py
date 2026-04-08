from collections import deque
import random
import math
BUCKETS = 10
DIGITS = 4


def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        least = i;
        for j in range(i + 1, n):
            if(A[j] < A[least]):
                least = j;
        A[i], A[least] = A[least], A[i];
        print("Step %2d = " %(i + 1), A);

def insertion_sort(A):
    n = len(A);
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
            A[j + 1] = key
        print("Step %2d = " %i, A);

def quick_sort(A, left, right):
    if left < right:
        q = partition(A, left, right)
        quick_sort(A, left, q - 1)
        quick_sort(A, q + 1, right)

def partition(A, left, right):
    pivot = A[left]
    low = left + 1
    high = right
    
    while( low < high):
        while low <= right and A[low] <= pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1
        if low < high:
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]
    return high

def radix_sort(A):
    queues = []
    for i in range(BUCKETS):
        queues.append(deque())
    n = len(A)
    factor = 1
    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i] // factor) % BUCKETS].append(A[i])
        i = 0
        for b in range(BUCKETS):
            while queues[b]:
                A[i] = queues[b].popleft()
                i += 1
        factor *= BUCKETS
        print("step", d + 1, A)
def keyfunc(p):
    return p[0]
#data = [random.randint(1, 9999) for _ in range(10)]

#radix_sort(data)    
#data.sort(reverse=True)  
#sorted(data, reverse=True)

data = [(62, 88, 81),
        (50, 3, 31),
        (86, 53, 42),
        (73, 47, 4),
        (89, 9, 8),
        (47, 88, 55),
        (19, 18, 20),
        (15, 1, 88),
        (90, 6, 60),
        (41, 92, 19)]

print("Before: ", data)

#print("Radix: ", sorted(data, key=keyfunc))
#print("x_inc:", sorted(data, key = lambda p:p[0]))
#print("x_inc:", sorted(data, key = lambda p:p[1], reverse=True))
print("x_inc:", sorted(data, key = lambda p: math.sqrt(p[0]*p[0] + p[1] * p[1] + p[2] * p[2])))

