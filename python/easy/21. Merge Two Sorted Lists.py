from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        l1 = []
        tmp = list1
        while tmp:
            l1.append(tmp.val)
            tmp = tmp.next

        tmp = list2
        l2 = []
        while tmp:
            l2.append(tmp.val)
            tmp = tmp.next
        l = sorted(l1 + l2)
        l1.sort()
        head = ListNode(l[0])
        tmp = head
        for i in range(1, len(l)):
            n = ListNode(l[i])
            tmp.next = n
            tmp = n
        return head
