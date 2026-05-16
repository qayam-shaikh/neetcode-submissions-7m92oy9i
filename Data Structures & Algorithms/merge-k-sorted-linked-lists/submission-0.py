# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for ll in lists:
            cur = ll
            while cur:
                arr.append(cur.val)
                cur = cur.next
        arr.sort()
        dummy = head = ListNode(0)

        for a in arr:
            head.next = ListNode(a)
            head = head.next
        
        return dummy.next