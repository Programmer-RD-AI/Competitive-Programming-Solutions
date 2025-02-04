from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        all_elements = []
        while head:
            all_elements.append(head)
            head = head.next
        length = (len(all_elements) - 1) / 2
        mid = int(length)
        if length - mid != 0:
            mid = int(length + 0.5)
        print(all_elements, mid)
        return all_elements[mid]
