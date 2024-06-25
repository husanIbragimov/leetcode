class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def print_middle(head: Node) -> None:
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    print(slow.val)


# Create a sample linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)

# Print the value of the middle node
print_middle(head)
