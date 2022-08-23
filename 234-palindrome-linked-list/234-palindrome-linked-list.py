# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        length = len(arr)
        rev=arr[length//2:]
        rev.reverse()
        if length%2==0:
            return arr[:length//2]==rev
        else:
            return arr[:(len(arr)//2)+1]==rev
            