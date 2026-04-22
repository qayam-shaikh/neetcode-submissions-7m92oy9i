# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = []
        cur = head
        while cur:
            st.append(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.val != st.pop():
                return False
            cur = cur.next
        return True