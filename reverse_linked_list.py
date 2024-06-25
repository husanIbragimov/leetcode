class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def reverse(head: Node) -> Node:
    prev = None
    curr = head

    while curr is not None:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_

    return prev


# Create a sample linked list
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next = node2
node2.next = node3
node3.next = node4

# Reverse the linked list
reversed_head = reverse(head)

# Print the reversed linked list
curr = reversed_head
while curr is not None:
    print(curr.val)
    curr = curr.next

