# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        for i in range(-1, len(lists) - 1, -1):
            if lists[i] == None:
                lists.pop(i)

        while len(lists) > 0:
            lowest = 0
            for i in range(1, len(lists)):
                if lists[i].val < lists[lowest].val:
                    lowest = i
            curr.next = lists[lowest]
            curr = curr.next
            lists[lowest] = lists[lowest].next
            if lists[lowest] == None:
                lists.pop(lowest)
            lowest = 0


        return dummy.next