from dataclasses import dataclass
from typing import Callable, Iterable, Iterator

@dataclass
class Node[DType]:
    data: DType
    prev: "Node | None" = None
    next: "Node | None" = None

    def __iter__(self) -> Iterator[DType]:
        cur = self
        while cur:
            yield cur.data
            cur = cur.next 

@dataclass
class LinkedList[DType]:
    head: Node[DType] | None = None
    _size: int = 0

    @property
    def size(self) -> int:
        return self._size
    
    def __iter__(self) -> Iterator[DType]:
        if self.head:
            yield from self.head
    
    def get_node(self, index: int) -> Node[DType]:
        if index >= self.size:
            raise Exception("Index out of range!")
        cur = self.head
        for _ in range(index):
            assert cur
            cur = cur.next
        assert cur
        return cur
    
    def insert(self, index: int, data: DType) -> None:
        if not self.head or index == 0:
            new_node = Node(data=data, next=self.head)
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        elif index == self.size:
            tail = self.get_node(index-1)
            new_node = Node(data=data, prev=tail)
            tail.next = new_node
        else:
            cur = self.get_node(index)
            new_node = Node(data=data, prev=cur.prev, next=cur)
            assert cur.prev
            cur.prev.next = new_node
            cur.prev = new_node
        self._size += 1
    
    def del_node(self, node: Node[DType]) -> DType:
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        self._size -= 1
        return node.data

    def delete(self, index: int) -> DType:
        cur = self.get_node(index)
        return self.del_node(cur)
    
    def __str__(self) -> str:
        return str(tuple(self))
    
    
def ll_factory[Dtype](items: Iterable[Dtype]) -> LinkedList[Dtype]:
    ll = LinkedList()
    for item in items:
        ll.insert(ll.size, item)
    return ll

def move_even_items_to_back(ll: LinkedList) -> LinkedList:
    cur = ll.head
    index = 0
    while cur and index < ll.size:
        nxt = cur.next
        if cur.data % 2 == 0 :
            item = ll.del_node(cur)
            ll.insert(ll.size, item)
        cur = nxt
        index += 1
    return ll

def move_max_to_front(ll: LinkedList) -> LinkedList:
    assert (max_node := ll.head)
    cur = max_node.next
    while cur:
        if cur.data >= max_node.data:
            max_node = cur
        cur = cur.next
    item = ll.del_node(max_node)
    ll.insert(0, item)
    return ll

def remove_duplicates_sorted_ll(ll: LinkedList) -> LinkedList:
    prev = None
    cur = ll.head
    while cur:
        nxt = cur.next
        if cur.data == prev:
            ll.del_node(cur)
        else:
            prev = cur.data
        cur = nxt
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
A->...->B->...
        ↑  ↓
         <- 
T2Q1 (Bptr, Aptr)
B->...->A->...
        ↑  ↓
         <- 
"""