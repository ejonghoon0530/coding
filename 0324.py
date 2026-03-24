class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.next = next
        self.prev = prev
    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:
                node.next.prev = node
            self.next = node
    def popNext(self):
        node = self.next
        if node is not None:
            self.next  = node.next
            if self.next is not None:
                self.next.prev = self
        return node
class dbLinkedList:
    def __init__(self):
        self.head = None
    def display(self, msg = 'dbLinkedList: '):
        print(msg, end ='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end = '<=>')
            ptr = ptr.next
        print('None')
    def isEmpty(self):
        return self.head == None
    def isFull(self):
        return False
    def getNode(self, pos):
        if pos < 0 : return None
        ptr = self.head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.next
        return ptr
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.next
            count += 1
        return count
    def insert(self, pos, e):
        node = DNode(e)
        before = self.getNode(pos - 1)
        if before is None:
            node.next = self.head
            if node.next is not None:
                node.next.prev = node
            self.head = node
        else: before.append(node)
    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before is None:
            if self.head is not None:
                self.head = self.head.next
                self.head.prev = None
            return before
        else :before.popNext()
    
i = []
print("파이썬 list(초기): ", i)
i.insert(0, 10)
i.insert(0, 20)
i.insert(1, 30)
i.insert(len(i), 40)
i.insert(2, 50)
print("파이썬 list(삽입x5): ", i)
i[2] = 90
print('파이썬 list(교체)', i)
i.pop(2)
i.pop(3)
i.pop(0)
print('파이썬list(삭제x3): ', i)

