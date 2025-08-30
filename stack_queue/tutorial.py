from typing import Iterable

class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def find_node(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert_node(self, index, value):
        if index < 0 or index > self.size:
            return -1
            
        new_node = ListNode(value)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.find_node(index - 1)
            new_node.next = prev.next
            prev.next = new_node
            
        self.size += 1
        return 0

    def remove_node(self, index):
        if index < 0 or index >= self.size:
            return -1
            
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            prev = self.find_node(index - 1)
            prev.next = prev.next.next
            if index == self.size - 1:
                self.tail = prev
                
        self.size -= 1
        return 0

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        self.ll.insert_node(0, item)

    def pop(self):
        if self.is_empty():
            return None
        item = self.ll.head.item
        self.ll.remove_node(0)
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.ll.head.item

    def is_empty(self):
        return self.ll.size == 0
    
    @classmethod
    def factory(cls, vals: Iterable[int]) -> "Stack":
        stack = cls()
        for v in vals:
            stack.push(v)
        return stack
    
    def print_all(self) -> None:
        while not self.is_empty():
            print(self.pop(), end=" ")
        print()

class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self, item):
        self.ll.insert_node(self.ll.size, item)

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.ll.head.item
        self.ll.remove_node(0)
        return item

    def is_empty(self):
        return self.ll.size == 0
    
    @classmethod
    def factory(cls, vals: Iterable[int]) -> "Queue":
        queue = cls()
        for v in vals:
            queue.enqueue(v)
        return queue
    
    def print_all(self) -> None:
        while not self.is_empty():
            print(self.dequeue(), end=" ")
        print()


def reverse_stack(stack: Stack) -> Stack:
    queue = Queue()
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    while not queue.is_empty():
        stack.push(queue.dequeue())
    return stack

def reverse_first_k_items(queue: Queue, k: int) -> Queue:
    stack = Stack()
    for _ in range(k):
        stack.push(queue.dequeue())
    for _ in range(k):
        queue.enqueue(stack.pop())
    for _ in range(queue.ll.size - k):
        queue.enqueue(queue.dequeue())
    return queue

def sort_stack(stack: Stack) -> Stack:
    temp = Stack()
    while not stack.is_empty():
        item = stack.pop()
        count = 0
        while not temp.is_empty() and item > temp.peek():
            stack.push(temp.pop())
            count += 1
        temp.push(item)
        for _ in range(count):
            temp.push(stack.pop())
    return temp


def eval(l1: Iterable, l2: Iterable) -> bool:
    return all(a == b for a, b in zip(l1, l2))

if __name__ == "__main__":
    test1 = (5, 4, 3, 2, 1)
    stack = Stack.factory(test1)
    rev = reverse_stack(Stack.factory(test1))
    print("Original:")
    stack.print_all()
    print("Reversed:")
    rev.print_all()

    
    test2 = (1, 2, 3, 4, 5, 6)
    queue = Queue.factory(test2)
    rev = reverse_first_k_items(Queue.factory(test2), k=3)
    print("Original:")
    queue.print_all()
    print("Reversed:")
    rev.print_all()
    

    test3 = (1, 2, 3, 4, 5, 6)
    stack = Stack.factory(test3)
    sorted_ = sort_stack(Stack.factory(test3))
    print("Original:")
    stack.print_all()
    print("Sorted:")
    sorted_.print_all()


"""
Q4a: x = a + b * c % d >> e -> = x >> + a % * b c d e
b: = y && << a b >> c + d e -> y = a << b && c >> d + e
c: x a b c * d % + e >> = -> = >> e + % d * c b a x
"""