# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        s1 = 0
        s2 = 0
        c = 0
        res = ListNode(0)
        while l1 or l2:
            if l1:
                s1 += l1.val * 10 ** c
                l1 = l1.next
            if l2:
                s2 += l2.val * 10 ** c
                l2 = l2.next
            c += 1
        s = s1 + s2
        curr = res
        if s == 0:
            res.next = ListNode(0)
        while s > 0:
            curr.next = ListNode(s % 10)
            curr = curr.next
            s = s // 10
            print(s)
        return res.next