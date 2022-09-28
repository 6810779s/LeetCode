class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lol=head
        i=0
        while lol:
            lol=lol.next
            i+=1
        ni=i-n
        if ni==0:
            return head.next
        lol=head
        for i in range(ni-1):
            lol=lol.next
        lol.next=lol.next.next
        return head