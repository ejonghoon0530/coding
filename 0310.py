capacity = 10
array = [None] * capacity
top = -1


class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1
        
    def isEmpty(self):
        if self.top == -1: return True
        else: return False
    def isFull(self):
        return self.top == self.capacity - 1
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            print("stack overflow")
            exit()
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else:
            print("stack underflow")
            exit()
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass
    def size(self):
        return self.top + 1
        
def checkBrackets(statement):
    stack = ArrayStack(capacity)
    for c in statement:
        if c in "([{":
            stack.push(c)
        elif c in ")]}":
            if stack.isEmpty():
                return False
            top = stack.peek()
            if (c == ")" and top == "(") or (c == "]" and top == "[") or (c == "}" and top == "{"):
                stack.pop()
            else:
                return False
    return stack.isEmpty()

#statement = input("")
#print("---->", checkBrackets(statement))

# #클래스를 리스트로 구현하기
# s = list()
# msg = input("문자열 입력: ")
# for c in msg:
#     s.append(c)
# print("문자열 출력: ", end = '')
# while len(s) > 0:
#     print(s.pop(), end = '')
# print()

