# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        diff = 0
        prev = None
        target = curr= head
        while curr:
            if diff == n:
                prev = target
                target = target.next
            else:
                diff+=1
            curr = curr.next
        if not prev:
            head = head.next
        else:
            prev.next = target.next
        
        return head


        