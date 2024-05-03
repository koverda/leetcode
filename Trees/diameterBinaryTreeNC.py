from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 0

    def longestPath(self, root: Optional[TreeNode]):
        if not root:
            return 0

        left = self.longestPath(root.left)
        right = self.longestPath(root.right)

        self.ans = max(self.ans, left + right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longestPath(root)
        return self.ans


sln = Solution()
bt = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
res = sln.diameterOfBinaryTree(bt)
print(res)
