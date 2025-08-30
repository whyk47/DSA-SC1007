class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, index):
        new_node = Node(data)
        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return True

        current = self.head
        count = 0

        while current and count < index - 1:
            current = current.next
            count += 1

        if not current:
            print("Index out of range")
            return False

        new_node.next = current.next
        current.next = new_node
        return True

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def deleteList(self):
        current = self.head
        while current:
            temp = current.next
            current.next = None
            current = temp
        self.head = None

def split(ll: LinkedList) -> tuple[LinkedList, LinkedList]:
    # Add your code here #
    even, odd = LinkedList(), LinkedList()
    even_size, odd_size = 0, 0
    cur = ll.head
    i = 0
    while cur:
        if not i % 2:
            even.insert(cur.data, even_size)
            even_size += 1
        else:
            odd.insert(cur.data, odd_size)
            odd_size += 1
        i += 1
        cur = cur.next
    return even, odd


if __name__ == "__main__":
    linked_list = LinkedList()
    index = 0

    print("Enter one number per line (press Enter after each number).")
    print("Enter any non-digit character to finish input:")
    try:
        while True:
            item = int(input())
            if linked_list.insert(item, index):
                print(f"Successfully inserted {item} at index {index}")
                index += 1
            else:
                print(f"Failed to insert {item}")
    except ValueError:
        pass

    print("\nBefore split() is called:")
    print("Current list:", end=" ")
    linked_list.printList()

    even_list, odd_list = split(linked_list)

    print("\nAfter split() was called:")
    print("Current list:", end=" ")
    linked_list.printList()

    print("Even list:", end=" ")
    even_list.printList()

    print("Odd list:", end=" ")
    odd_list.printList()

    linked_list.deleteList()
    even_list.deleteList()
    odd_list.deleteList()