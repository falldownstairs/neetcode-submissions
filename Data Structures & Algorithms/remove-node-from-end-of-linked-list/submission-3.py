# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        curr = head
        start = ListNode(0,head)
        while curr:
            c += 1
            curr = curr.next
        prev = start
        for _ in range(c-n):
            prev = prev.next
        prev.next = prev.next.next
        return start.next