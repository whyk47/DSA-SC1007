class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
        
def print_tree_in_order(node):
    if node is None:
        return
    print_tree_in_order(node.left)
    print(node.item, end=", ")
    print_tree_in_order(node.right)

def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

def smallest_value(node):
    # Write your code here #
    if not node:
        return float("inf")
    return min(node.item, smallest_value(node.left), smallest_value(node.right))

if __name__ == "__main__":
    root = BTNode(4)
    root.left = BTNode(5)
    root.right = BTNode(2)
    root.left.left = None
    root.left.right = BTNode(6)
    root.right.left = BTNode(3)
    root.right.right = BTNode(1)

    print("Tree Structure:")
    printTree(root)
    
    print("\nTree (In-Order):")
    print_tree_in_order(root)
    print()
    
    print("\nThe smallest value in the tree is:", smallest_value(root))