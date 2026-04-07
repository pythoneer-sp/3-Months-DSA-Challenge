from typing import Optional, ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(-1,head)
        slow=dummy
        fast=dummy
        for _ in range(n):
            fast=fast.next
        while fast.next != None:
            slow = slow.next
            fast= fast.next
        slow.next=slow.next.next
        return dummy.next