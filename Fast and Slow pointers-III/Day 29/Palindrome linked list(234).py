from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        def reverse(node):
            prev=None
            curr=node
            while curr:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev

        while fast.next != None and fast.next.next != None:
            slow=slow.next
            fast=fast.next.next
        new_head=reverse(slow.next)
        first=head
        second=new_head
        while second!=None:
            if first.val != second.val:
                reverse(new_head)
                return False
            first=first.next
            second=second.next
        reverse(new_head)
        return True      