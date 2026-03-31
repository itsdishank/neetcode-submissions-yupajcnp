# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode()
        # print(dummy)
        # if not lists:
        #     print("hi")
        while lists:

            minv = mini = float("inf")
            for i, v in enumerate(lists):
                # print(mini,minv)
                if v and v.val<minv:
                    minv = v.val
                    mini = i
                # if not v:
            # print()
            if mini != float("inf"):
                # print(lists[mini])
                head.next = lists[mini]
                head = head.next
                lists[mini] = lists[mini].next
            lists = list(filter(lambda x: x is not None, lists))

            # print(lists)
        # print(lists[mini])

        # print(dummy)

        # for i in lists:
        #     print(i)
        # print(mini,minv)

        return dummy.next
                
