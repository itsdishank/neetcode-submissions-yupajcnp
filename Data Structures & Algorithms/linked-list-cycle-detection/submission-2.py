# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        tortoise = hare = head

        while tortoise.next and hare.next and hare.next.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                return True
        return False
        