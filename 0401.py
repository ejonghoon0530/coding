import time

def find_max(a, b, c): # 최대값을 구하는 함수
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max
def findMax(A):
    n = len(A)
    max = A[0]
    for i in range(n):
        if A[i] > max:
            max = A[i]
    return max
def find_key(A, Key):
    n = len(A)
    for i in range(n):
        if A[i] == Key:
            return i
    return -1

A = [0] * 1000000
B = []

for i in range(1000000):
    A[i] = i

for i in range(1000000):
    B.append(i)
start = time.time()

#findMax(A)
#findMax(B)
find_key(A, 1000000)

end = time.time()
print('실행 시간: %0.3f' %(end - start))

