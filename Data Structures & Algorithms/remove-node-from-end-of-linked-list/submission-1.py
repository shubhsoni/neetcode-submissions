# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        #use 2 pointers - at n dist apart
        prev = tail = head
        counter = 0

        while counter < n and tail:
            tail = tail.next
            counter += 1
        #  1
        # p,t
        # c = 0
        if not tail:
            return head.next

        while tail and tail.next:
            prev = prev.next
            tail = tail.next

        # 1, 2, 3, 4
        #    p,    t
        # c = 2
        
        prev.next = prev.next.next

        # 1, 2 -> 4
        return head
