"""
Berilgan linked list sonlarini ekranga chiqaring.
Misol: 1->2->3
Kutilgan natija:
1
2
3
"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def print_elements(head: Node) -> None:
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


# Create a sample linked list
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next = node2
node2.next = node3
node3.next = node4

# Print the elements of the linked list
print_elements(head)
