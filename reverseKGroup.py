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

        printNodes(res)
        while True:

            start = ptr

            # get kth
            for i in range(k - 1):
                if not ptr: return res.next
                ptr = ptr.next

            if not ptr:
                return res.next
            kth = ptr.next

            # print("after getting kth ", end=""), printNodes(res)
            # print(f'ptr {ptr.val}, kth {kth.val}, start {start.val}, pre {pre.val}')

            if not firstSet:
                pre.next = ptr
                firstSet = True

            pre.next = ptr
            ptr.next = None

            # reverse
            pre.next = self.reverse(start)
            # reconnect
            start.next = kth
            pre = start

            print("end of cycle ", end=""), printNodes(res)
            # continue
            # print(f'ptr {ptr.val}, kth {kth.val}, start {start.val}, pre {pre.val}')
            ptr = kth
            print("")


        return res.next

def printNodes(l: ListNode):
    while l:
        print(l.val, end = " -> ")
        l = l.next
    print("")





rol = ReverseKGroup()
ll = ListNode(1, ListNode(2, ListNode(3)))
res = rol.reverseKGroup(ll, 2)