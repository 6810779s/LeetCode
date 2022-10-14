# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_copy = head
        length=0
        
        while head_copy!=None:
            head_copy=head_copy.next
            length+=1
        
        
        cnt=1
        head_copy=head
        if length//2==0:
            return None
        while length//2!=cnt:
            head_copy=head_copy.next
            cnt+=1
        
        if head_copy.next.next== None:
            head_copy.next=None
        else:
            head_copy.next = head_copy.next.next
        return head  
    
        
        