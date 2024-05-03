from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        toCheck = [root]
        nextCheck = []
        thisLevel = []

        while toCheck:
            for i in range(len(toCheck)):
                thisLevel.append(toCheck[i].val)
                if toCheck[i].left: nextCheck.append(toCheck[i].left)
                if toCheck[i].right: nextCheck.append(toCheck[i].right)
                res.append(thisLevel)
                thisLevel = []
                toCheck = nextCheck
                nextCheck = []

        return res
