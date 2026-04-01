# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        else:
            prev_node = None
            curr_node = head
            while curr_node:
                upcoming = curr_node.next
                curr_node.next = prev_node
                #update
                prev_node = curr_node
                curr_node = upcoming
            return prev_node
