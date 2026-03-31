# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy head for the result list (ease of implementation)
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Traverse while any list has nodes OR there is a carry
        while l1 is not None or l2 is not None or carry:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Append the computed digit as a new node
            current.next = ListNode(digit)
            current = current.next

            # Move pointers ahead if possible
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # Return result list skipping dummy head
        return dummy.next
