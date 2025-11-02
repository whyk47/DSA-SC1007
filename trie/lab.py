class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.first_child = None
        self.next_sibling = None
        self.is_end_of_word = False

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _find_child(self, node, char):
        current = node.first_child
        while current:
            if current.char == char:
                return current
            current = current.next_sibling
        return None

    def _add_child(self, node: TrieNode, char: str) -> TrieNode:
        #add your implementations to insert a child following the alphabetical order
        new_node = TrieNode(char)
        cur = node.first_child
        if not cur or cur.char > char:
            new_node.next_sibling = cur
            node.first_child = new_node
            return new_node
        while cur.next_sibling and cur.next_sibling.char < char:
            cur = cur.next_sibling
        new_node.next_sibling = cur.next_sibling
        cur.next_sibling = new_node
        return new_node
        

    def insert(self, word):
        node = self.root
        for char in word:
            child = self._find_child(node, char)
            if not child:
                child = self._add_child(node, char)
            node = child
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = self._find_child(node, char)
            if not node:
                return False
        return node.is_end_of_word

    def _dfs(self, node: TrieNode, prefix: str) -> None:
        if node.is_end_of_word:
            print(prefix)
        child = node.first_child
        while child:
            self._dfs(child, prefix + child.char)
            child = child.next_sibling
    
    def _rev_dfs(self, node: TrieNode, prefix: str) -> None:
        children = Stack()
        child = node.first_child
        while child:
            children.push(child)
            child = child.next_sibling
        while not children.is_empty():
            child = children.pop()
            self._rev_dfs(child, prefix + child.char)
        if node.is_end_of_word:
            print(prefix)



    def print_words_alphabetically(self):
        self._dfs(self.root, "")


    def print_words_reverse_alphabetically(self):
        self._rev_dfs(self.root, "")


# Assume Trie, TrieNode, and Queue classes have already been defined.
# Create a new Trie instance
trie = Trie()
trie.insert("car")
trie.insert("care")
trie.insert("cat")
trie.insert("camp")
trie.insert("camera")

trie.print_words_reverse_alphabetically()
print()
trie.print_words_alphabetically()
