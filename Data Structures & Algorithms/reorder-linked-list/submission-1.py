# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sp, fp = head,head
        while fp.next and fp.next.next:
            sp = sp.next
            fp = fp.next.next
        second = sp.next
        sp.next = None

        prev = None
        curr = second
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        
        first = head
        second = prev

        while second:
            fn = first.next
            sn = second.next

            first.next = second
            second.next = fn

            first = fn
            second = sn



        return