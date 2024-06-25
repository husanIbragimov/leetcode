from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    curr1, curr2 = l1, l2
    num1, num2 = 0, 0
    head = ListNode()

    while curr1 or curr2:
        if curr1:
            num1 = num1 * 10 + curr1.val
            curr1 = curr1.next

        if curr2:
            num2 = num2 * 10 + curr2.val
            curr2 = curr2.next

        head.val = num2 + num1
        head = head.next
        print(head.val)

    return head


def reverse(num):
    reversed_num = 0

    while num:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return reversed_num


l1 = [2, 4, 3]
l2 = [5, 6, 4]

head1 = ListNode(2)
node11 = ListNode(4)
node12 = ListNode(3)
node13 = ListNode(6)

head2 = ListNode(5)
node21 = ListNode(6)
node22 = ListNode(4)

head1.next = node11
node11.next = node12

head2.next = node21
node21.next = node22

print(addTwoNumbers(head1, head2))
