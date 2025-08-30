"""
Q1: 
Preorder (val, left, right): A{B[C][D(E)]}{FG}
Inorder (left, val, right): {[C]B[(E)D]}A{FG}

   A
  / \
  B  F
 / \  \
C   D  G
   /
  E
"""
from typing import Iterable


class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

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
    
def levelOrderIterative(root: BTNode) -> None:
    queue = Queue()
    queue.enqueue(root)
    while not queue.is_empty():
        node = queue.dequeue()
        print(node.item)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    print()
    

def preOrderIterative(root: BTNode) -> None:
    stack = Stack()
    stack.push(root)
    while not stack.is_empty():
        node = stack.pop()
        print(node.item)
        if node.right:
            stack.push(node.right)
        if node.left:
            stack.push(node.left)
    print()
    

def maxDepth(node: BTNode | None) -> int:
    if not node:
        return -1
    return 1 + max(maxDepth(node.left), maxDepth(node.right))

if __name__ == "__main__":
    root = BTNode(
        20, 
        BTNode(15, BTNode(10), BTNode(18)), 
        BTNode(50, BTNode(25), BTNode(80)),
    )
    levelOrderIterative(root)  # 20 15 50 10 18 25 80
    preOrderIterative(root)  # 20 15 10 18 50 25 80

    node = BTNode(
        50,
        BTNode(20, BTNode(10), BTNode(30, BTNode(55))),
        BTNode(60, None, BTNode(80)),
    )
    assert maxDepth(node) == 3
    print(f"Max Depth: {maxDepth(node)}")