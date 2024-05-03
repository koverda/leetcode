class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseKGroup:
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        res = ListNode(0, head)
        pre = res
        ptr = head
        firstSet = False

        while True:
            start = ptr

            for i in range(k - 1):
                if not ptr: return res.next
                ptr = ptr.next

            if not ptr: return res.next
            kth = ptr.next

            if not firstSet:
                pre.next = ptr
                firstSet = True

            pre.next = ptr
            ptr.next = None

            pre.next = self.reverse(start)
            start.next = kth
            pre = start
            ptr = kth

def printNodes(l: ListNode):
    while l:
        print(l.val, end = " -> ")
        l = l.next
    print("")





rol = ReverseKGroup()
ll = ListNode(1, ListNode(2, ListNode(3)))
res = rol.reverseKGroup(ll, 2)