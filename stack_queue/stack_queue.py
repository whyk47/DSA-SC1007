from dataclasses import dataclass, field
from typing import Iterable, Iterator, Sequence

@dataclass
class Stack[DType]:
    items: list[DType] = field(default_factory=list)

    def push(self, item: DType) -> None:
        self.items.append(item)

    def pop(self) -> DType:
        assert self.items
        return self.items.pop()
    
    def peek(self) -> DType:
        return self.items[-1]

    def __iter__(self) -> Iterator[DType]:
        yield from reversed(self.items)

    @classmethod
    def factory(cls, items: Sequence[DType]) -> "Stack":
        stack = cls()
        for item in reversed(items):
            stack.push(item)
        return stack

    
@dataclass
class Queue[DType]:
    items: list[DType] = field(default_factory=list)

    def enqueue(self, item: DType) -> None:
        self.items.insert(0, item)

    def dequeue(self) -> DType:
        assert self.items
        return self.items.pop()
    
    def __iter__(self) -> Iterator[DType]:
        yield from reversed(self.items)

    @classmethod
    def factory(cls, items: Iterable[DType]) -> "Queue":
        queue = cls()
        for item in items:
            queue.enqueue(item)
        return queue


def reverse_stack(stack: Stack) -> Stack:
    queue = Queue()
    while stack.items:
        queue.enqueue(stack.pop())
    while queue.items:
        stack.push(queue.dequeue())
    return stack

def reverse_first_k_items(queue: Queue, k: int) -> Queue:
    stack = Stack()
    for _ in range(k):
        stack.push(queue.dequeue())
    for _ in range(k):
        queue.enqueue(stack.pop())
    for _ in range(len(queue.items) - k):
        queue.enqueue(queue.dequeue())
    return queue

def sort_stack(stack: Stack) -> Stack:
    temp = Stack()
    while stack.items:
        item = stack.pop()
        count = 0
        while temp.items and item > temp.peek():
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
    stack = reverse_stack(Stack.factory(test1))
    print(tuple(stack))
    assert eval(stack, Stack.factory(tuple(reversed(test1))))
    
    test2 = (1, 2, 3, 4, 5, 6)
    queue = reverse_first_k_items(Queue.factory(test2), k=3)
    print(tuple(queue))
    assert eval(queue, Queue.factory((3, 2, 1, 4, 5, 6)))

    test3 = (6, 5, 4, 3, 2, 1)
    stack = sort_stack(Stack.factory(test3))
    print(tuple(stack))
    assert eval(stack, Stack.factory(sorted(test3)))

"""
Q4a: x = a + b * c % d >> e -> = x >> + a % * b c d e
b: = y && << a b >> c + d e -> y = a << b && c >> d + e
c: x a b c * d % + e >> = -> = >> e + % d * c b a x
"""