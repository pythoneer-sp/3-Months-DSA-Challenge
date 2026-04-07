from typing import Optional, ListNode

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(node):
            prev=None
            curr=node
            while curr:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        second_half=slow.next
        slow.next=None
        newhead=reverse(second_half)
        while head and newhead:
            f1=head.next
            f2=newhead.next
            head.next=newhead
            newhead.next=f1
            head=f1
            newhead=f2