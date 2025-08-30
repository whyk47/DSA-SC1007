class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item  # Store the item (integer)
        self.left = left  # Reference to the left child node
        self.right = right  # Reference to the right child node

def insertBSTNode(root, value):
    """ Recursive approach to insert a node into a BST. """
    if root is None:
        return BTNode(value)
    
    if value < root.item:
        root.left = insertBSTNode(root.left, value)
    elif value > root.item:
        root.right = insertBSTNode(root.right, value)
    return root  # Ensure the modified node is returned

def findMin(node):
    """ Find the node with the smallest value in a subtree. """
    while node.left is not None:
        node = node.left
    return node

def rf_node(node: BTNode | None, value: int) -> BTNode | None:
    temp = BTNode(float("inf"), node)
    prev, cur = temp, node
    while True:
        if not cur:
            return temp.left
        if cur.item == value:
            break
        prev = cur
        if value < cur.item:
            cur = cur.left
        else:
            cur = cur.right
    if cur.left and cur.right:
        child = findMin(cur.right)
        cur.item = child.item
        cur.right = rf_node(cur.right, child.item)
        return temp.left
    child = cur.left or cur.right
    if not child:
        if prev.left is cur:
            prev.left = None
        else:
            prev.right = None
    else:
        cur.item = child.item
        cur.left = child.left
        cur.right = child.right
    return temp.left

def find(node: BTNode | None, value: int) -> bool:
    if not node:
        return False
    if value < node.item:
        return find(node.left, value)
    elif value > node.item:
        return find(node.right, value)
    return True
    

def removeBSTNode(node: BTNode | None, value: int) -> int:
    # Write your code here #
    if not find(node, value):
        return -1
    rf_node(node, value)
    return 0
    

def printBSTInOrder(node):
    """ Print BST items in sorted order using in-order traversal. """
    if node:
        printBSTInOrder(node.left)
        print(node.item, end=" ")
        printBSTInOrder(node.right)

def printTree(node, level=0, prefix="Root: "):
    """ Pretty prints the tree structure for better visualization """
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

if __name__ == "__main__":
    root = None
    print("Binary Search Tree Node Removal Program")
    print("=====================================")
    
    print("\nFirst, let's build the BST:")
    while True:
        try:
            value = input("\nEnter a value to insert (-1 to quit): ")
            if not value:
                continue  # Ignore empty inputs
                
            i = int(value)
            if i == -1:
                break
                
            root = insertBSTNode(root, i)
            print("\nCurrent BST structure:")
            printTree(root)
            print("\nIn-order traversal: ", end="")
            printBSTInOrder(root)
            print()
            
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print("\nNow let's remove nodes:")
    while True:
        try:
            value = input("\nEnter a value to remove (-1 to quit): ")
            if not value:
                continue  # Ignore empty inputs
                
            i = int(value)
            if i == -1:
                break
                
            result = removeBSTNode(root, i)
            if result == 0:
                print("\nBST structure after removal:")
                printTree(root)
                print("\nIn-order traversal: ", end="")
                printBSTInOrder(root)
                print()
            else:  # result == -1
                print("Value not found in the tree!")
            
        except ValueError:
            print("Invalid input! Please enter an integer.")