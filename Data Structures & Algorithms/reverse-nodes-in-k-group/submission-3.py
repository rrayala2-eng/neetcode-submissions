# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy # one before the group

        while True:
            kth = self.getkth(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next # one after the group

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

        

    def getkth(self,curr,k):
        while k > 0 and curr:
            curr = curr.next
            k -= 1
        return curr