from dataclasses import dataclass
from typing import Callable, Iterable, Iterator


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __iter__(self) -> Iterator[int]:
        cur = self
        while cur:
            yield cur.data
            cur = cur.next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0  
        
    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
        if self.head is None:
            raise ValueError("List is empty")
            
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")
            
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
        
        prev_node = self.findNode(index - 1)
        if prev_node is not None:
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1
            return True
        return False

    def removeNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        if self.head is None:
            return False
            
        if index == 0:
            cur = self.head
            self.head = cur.next
            self.size -= 1
            return True
            
        pre = self.findNode(index - 1)
        if pre is not None and pre.next is not None:
            cur = pre.next
            pre.next = cur.next
            self.size -= 1
            return True
        return False

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")
    
    def __iter__(self) -> Iterator[int]:
        if self.head:
            yield from self.head

def num_even_nodes(ll: LinkedList) -> int:
    n = 0
    cur = ll.head
    while cur:
        if not cur.data % 2:
            n += 1
        cur = cur.next
    return n

def move_even_items_to_back(ll: LinkedList) -> LinkedList:
    i, n = 0, num_even_nodes(ll)
    while i < ll.size and n > 0:
        node = ll.findNode(i)
        if not node.data % 2:
            ll.removeNode(i)
            ll.insertNode(node.data, ll.size)
            n -= 1
        else:
            i += 1
    return ll

def move_max_to_front(ll: LinkedList) -> LinkedList:
    pre_max, max_node, cur = None, ll.head, ll.head
    while cur.next:
        if cur.next.data > max_node.data:
            pre_max, max_node = cur, cur.next
        cur = cur.next
    if pre_max:
        pre_max.next = max_node.next
        max_node.next = ll.head
        ll.head = max_node
    return ll
    

def remove_duplicates_sorted_ll(ll: LinkedList) -> LinkedList:
    prev = None
    cur = ll.head
    i = 0
    while cur:
        nxt = cur.next
        if cur.data == prev:
            ll.removeNode(i)
        else:
            prev = cur.data
            i += 1
        cur = nxt
    return ll

def ll_factory(items: Iterable[int]) -> LinkedList:
    ll = LinkedList()
    for item in items:
        ll.insertNode(item, ll.size)
    return ll

@dataclass
class Test:
    test: tuple[int, ...]
    ans: tuple[int, ...]

    def check(self, func: Callable) -> bool:
        ll = ll_factory(self.test)
        output = func(ll)
        if (passed := tuple(output) == self.ans):
            print("Passed!")
        else:
            print(f"In: {self.test}, Out: {tuple(output)}, Expected: {self.ans}") 
        return passed
    

if __name__ == "__main__":
    test_1 = (
        ((2, 3, 4, 7, 15, 18), (3, 7, 15, 2, 4, 18)),
        ((2, 7, 18, 3, 4, 15), (7, 3, 15, 2, 18, 4)),
        ((1, 3, 5), (1, 3, 5)),
        ((2, 4, 6), (2, 4, 6))
    )
    test_2 = (
        ((30, 20, 40, 70, 50), (70, 30, 20,40, 50)),
    )
    test_3 = (
        ((1, 2, 2, 4, 4, 5, 5 ), (1, 2, 4, 5)),
        ((1, 2, 3, 4, 5), (1, 2, 3, 4, 5))
    )
    tests = (test_1, test_2, test_3)
    funcs = (move_even_items_to_back, move_max_to_front, remove_duplicates_sorted_ll)
    for test_suite, func in zip(tests, funcs):
        for test in test_suite: 
            Test(*test).check(func)

"""
Q4: The result will be a singly linked list from q to the node preceding s,
and a circular linked list from s onwards.

q->...->r->s->...
           ↑    ↓
           u <- t

T2Q1 (Aptr, Bptr)
B->...->A->...
        ↑  ↓
         <- 
T2Q1 (Bptr, Aptr)
A->...->B->...
        ↑  ↓
         <- 
"""