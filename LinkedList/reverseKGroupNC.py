class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseKGroup:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                ptr = curr.next     # get next
                curr.next = prev    # point back
                prev = curr         # set next prev
                curr = ptr          # iterate

            tmp = groupPrev.next # save dummy.next ptr (#1)
            groupPrev.next = kth # set dummy.next to kth (#2, etc)
            groupPrev = tmp # set grpprev to next group prv, no longer messing with dummy's ptr in future iterations!
        return dummy.next



    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


def printNodes(l: ListNode):
    while l:
        print(l.val, end = " -> ")
        l = l.next
    print("")


rol = ReverseKGroup()
ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
printNodes(ll)
res = rol.reverseKGroup(ll, 2)
printNodes(res)