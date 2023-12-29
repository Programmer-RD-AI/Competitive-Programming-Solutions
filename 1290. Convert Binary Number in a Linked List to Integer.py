# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        value = ""
        tot = 0
        while head.next:
            value += str(head.val)
            head = head.next
        value += str(head.val)
        return int(value, 2)
