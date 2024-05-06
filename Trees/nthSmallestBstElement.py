from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.left

    nRecur = 0
    resRecur = None
    def kthSmallestRecur(self, root: Optional[TreeNode], k: int) -> int:
        if root:
            if self.resRecur:
                return self.resRecur

            self.kthSmallestRecur(root.left, k)

            self.nRecur += 1

            if self.nRecur == k:
                self.resRecur = root.val

            self.kthSmallestRecur(root.right, k)

            return self.resRecur


sln = Solution()
bst = TreeNode(5, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(8)))
print(sln.kthSmallestRecur(bst, 1))