class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hashmap ={None: None}
        cur=head
        while cur:
            newnode=Node(cur.val)
            hashmap[cur]=newnode
            cur=cur.next
        cur=head
        while cur:
            newnode=hashmap[cur]
            newnode.random=hashmap[cur.random]
            newnode.next=hashmap[cur.next]
            cur=cur.next
        return hashmap[head]