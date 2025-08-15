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

from dataclasses import dataclass, field

@dataclass
class TreeNode[DType]:
    value: DType
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None

@dataclass
class Queue[DType]:
    items: list[DType] = field(default_factory=list)

    def enqueue(self, item: DType) -> None:
        self.items.insert(0, item)

    def dequeue(self) -> DType:
        return self.items.pop()
    
@dataclass
class Stack[DType]:
    items: list[DType] = field(default_factory=list)

    def push(self, item: DType) -> None:
        self.items.append(item)

    def pop(self) -> DType:
        return self.items.pop()
    
def levelOrderIterative(root: TreeNode) -> None:
    queue = Queue([root])
    while queue.items:
        node = queue.dequeue()
        print(node.value)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    print()
    

def preOrderIterative(root: TreeNode) -> None:
    stack = Stack([root])
    while stack.items:
        node = stack.pop()
        print(node.value)
        if node.right:
            stack.push(node.right)
        if node.left:
            stack.push(node.left)
    print()
    

def maxDepth(node: TreeNode | None) -> int:
    if not node:
        return -1
    return 1 + max(maxDepth(node.left), maxDepth(node.right))

if __name__ == "__main__":
    root = TreeNode(
        20, 
        TreeNode(15, TreeNode(10), TreeNode(18)), 
        TreeNode(50, TreeNode(25), TreeNode(80)),
    )
    levelOrderIterative(root)  # 20 15 50 10 18 25 80
    preOrderIterative(root)  # 20 15 10 18 50 25 80

    node = TreeNode(
        50,
        TreeNode(20, TreeNode(10), TreeNode(30, TreeNode(55))),
        TreeNode(60, None, TreeNode(80)),
    )
    assert maxDepth(node) == 3
    print(f"Max Depth: {maxDepth(node)}")