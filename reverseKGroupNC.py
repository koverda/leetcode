class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseKGroup:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

def printNodes(l: ListNode):
    while l:
        print(l.val, end = " -> ")
        l = l.next
    print("")





rol = ReverseKGroup()
ll = ListNode(1, ListNode(2, ListNode(3)))
res = rol.reverseKGroup(ll, 2)