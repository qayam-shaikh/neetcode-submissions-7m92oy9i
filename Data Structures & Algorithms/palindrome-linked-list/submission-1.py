# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=f=head
        while f and f.next:
            s= s.next
            f=f.next.next
        
        prev=None
        while s:
            tmp=s.next
            s.next=prev
            prev=s
            s=tmp
        
        l, r= head, prev
        while r:
            if l.val!=r.val:
                return False
            l=l.next
            r=r.next
        return True
