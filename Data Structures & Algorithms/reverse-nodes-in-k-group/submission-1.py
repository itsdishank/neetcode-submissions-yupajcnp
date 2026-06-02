# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        dummy = ListNode()
        dummy.next = head
        prevNode = dummy
        cur = head
        while True:
            kth = cur
            ct = 0
            while kth and ct < k:
                ct +=1
                kth = kth.next
            if ct != k:
                break
            prev = None
            tail = cur
            # print(dummy)
            for _ in range(k):
                temp = tail.next
                tail.next = prev
                prev = tail
                tail = temp
            
            # print(prev)
            nxtNode = temp

            prevNode.next = prev
            cur.next = nxtNode

            prevNode = cur
            cur = cur.next
            # print(dummy)
            # print()
        
        return dummy.next

            
            

        

        

