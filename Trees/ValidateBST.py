from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def validateBST(self, root, limL, limR) -> bool:
        if not root:
            return True

        if root.val > limR or root.val < limL:
            return False

        return self.validateBST(root.left, limL, root.val) and self.validateBST(root.right, root.val, limR)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateBST(root, float("-inf"), float("inf"))



bst = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
sln = Solution()
res = sln.isValidBST(bst)
print(res)

