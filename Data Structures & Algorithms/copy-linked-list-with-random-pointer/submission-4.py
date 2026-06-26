"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        ostart = Node(0,head,None)
        cstart = Node(0,None,None)
        curr = cstart

        while head:
            curr.next = Node(head.val,None,None)
            hashmap[head] = curr.next
            head = head.next
            curr = curr.next

        curr = cstart.next
        head = ostart.next
        while curr and head:
            if head.random:
                curr.random = hashmap[head.random]
            else:
                curr.random = None
            curr = curr.next
            head = head.next
        
        return cstart.next
        