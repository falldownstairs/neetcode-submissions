# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        curr = head
        last = None
        l = 0
        while True:
            c = k
            begin = curr
            while curr and c > 0:
                curr = curr.next
                c -= 1
            if c != 0:
                break
            else:
                prev = curr
                curr = begin
                for _ in range(k):
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                if l == 0:
                    res.next = prev
                if last:
                    last.next = prev
                last = begin
            l += 1

        return res.next
            
        