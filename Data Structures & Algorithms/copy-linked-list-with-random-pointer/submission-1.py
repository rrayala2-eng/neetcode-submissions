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
        oldTo = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldTo[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldTo[curr]
            copy.next = oldTo[curr.next]
            copy.random = oldTo[curr.random]
            curr = curr.next

        return oldTo[head]