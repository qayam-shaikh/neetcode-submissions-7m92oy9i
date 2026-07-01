# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def kth_node(prevGroup,k):
            cur=prevGroup
            while cur and k>0:
                k-=1
                cur=cur.next
            return cur
        
        dummy=ListNode(0)
        dummy.next=head
        prevGroup=dummy
        while True:
            kth=kth_node(prevGroup,k)
            if not kth: break
            nextGroup=kth.next
            prev=nextGroup
            cur=prevGroup.next
            while cur!=nextGroup:
                nxt=cur.next
                cur.next=prev
                prev=cur
                cur=nxt
            temp=prevGroup.next
            prevGroup.next=kth
            prevGroup=temp
        return dummy.next