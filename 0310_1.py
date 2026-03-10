# import queue

# s = queue.LifoQueue(maxsize=20) #last in first out 큐를 최대 20개 생성

# msg = input("문자열 입력: ")
# for c in msg:
#     s.put(c)
# print("문자열 출력: ", end = '')
# while not s.empty():
#     print(s.get(), end = '')
# print()

# #반복구조의 팩토리얼 함수
# def factorial_iter(n):
#     result = 1
#     for k in range(2, n + 1):
#         result = result * k
#     return result

# #재귀구조의 팩토리얼 함수
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)  


# #하노이 타워
# def hanoi(n, fr, tmp, to):
#     if n == 1: #원판이 한개면 바로 이동
#         print("원판 1 : %s --> %s" %(fr, to))
#     else: #원판이 두개 이상이면
#         hanoi(n - 1, fr, to, tmp) #n-1개의 원판을 보조기둥으로 옮김
#         print("원판 %d : %s --> %s" %(n, fr, to))
#         hanoi(n - 1, tmp, fr, to)
# hanoi(3, '첫번째', '두번째', '세번째')
