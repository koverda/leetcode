# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headRef = head
        while head and head.next:
            toCheck = head.next
            while toCheck and toCheck.val == head.val:
                toCheck = toCheck.next
            head.next = toCheck
            head = head.next

        return headRef


sl = Solution()

res = sl.deleteDuplicates(ListNode(1,ListNode(1, ListNode(1))))
print(res)

