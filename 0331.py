import queue

class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else: pass
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else: pass
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else: pass
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    def display(self, msg):
        print(msg, end='= [ ')
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i % self.capacity], end=' ')
        print("]")
    
    

class BTNode:
    def __init__(self, elem, left = None, right = None):
        self.data = elem
        self.left = left
        self.right = right
    def isLeaf(self):
        return self.left is None and self.right is None
def preorder(n):
    if n is not None:
        print(n.data, end = ' ')
        preorder(n.left)
        preorder(n.right)
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end = ' ')
        inorder(n.right)
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end = ' ')
def levelorder(n):
    queue = ArrayQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end = ' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
def count_node(n):
    if n is None:
        return 0
    else:
        return count_node(n.left) + count_node(n.right) + 1
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if(hLeft > hRight):
        return hLeft + 1
    else: return hRight + 1
def evaluate(node):
    if node is None:
        return 0
    elif node.isLeaf():
        return node.data
    else:
        op1 = evaluate(node.left)
        op2 = evaluate(node.right)
        if node.data == '+': return op1 + op2
        elif node.data == '-': return op1 - op2
        elif node.data == '*': return op1 * op2
        elif node.data == '/': return op1 / op2
def buildTree(expr):
    if len(expr) == 0:
        return None
    token = expr.pop()
    if token in '+-*/':
        node = BTNode(token)
        node.right = buildTree(expr)
        node.left = buildTree(expr)
        return node
    else:
        return BTNode(float(token))

    
            
# d = BTNode('D', None, None)
# e = BTNode('E', None, None)
# b = BTNode('B', d, e)
# f = BTNode('F', None, None)
# c = BTNode('C', f, None)
# root = BTNode('A', b, c)

# print('\n In-Order: ', end = ' ')
# inorder(root)
# print('\n Pre-order: ' , end = ' ')
# preorder(root)
# print('\n Post-order: ' , end = ' ')
# postorder(root)
# print('\n Level-order: ' , end = ' ')
# levelorder(root)
# print()

# print("노드의 개수 = %d개" % count_node(root))
# print("트리의 높이 = %d" % calc_height(root))


table = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), 
         ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'), 
         ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), 
         ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), 
         ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), 
         ('Y', '-.--'), ('Z', '--..')]
def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]

def make_morse_tree():
    root = BTNode(None, None, None)
    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if (c == '.'):
                if node.left == None:
                    node.left = BTNode(None, None, None)
                node = node.left
            elif (c == '-'):
                if node.right == None:
                    node.right = BTNode(None, None, None)
                node = node.right
        node.data = tp[0]
    return root
def decode(root, code):
    node = root
    for c in code:
        if c == '.': node = node.left
        elif c == '-': node = node.right
    return node.data

# morseCodeTree = make_morse_tree()
# str = input("입력 문장: ")
# mlist = []
# for ch in str:
#     code = encode(ch)
#     mlist.append(code)
# print("Morse Code: ", mlist)
# print("Decoding: ", end = ' ')
# for code in mlist:
#     ch = decode(morseCodeTree, code)
#     print(ch, end = ' ')
# print()


str = input("입력(후위표기): ")
expr = str.split()
root = buildTree(expr)
print('\n전위순회: ', end = ' ')
preorder(root)
print('\n중위순회: ', end = ' ')
inorder(root)
print('\n후위순회: ', end = ' ')
postorder(root)
print('\n계산결과: ', evaluate(root))