from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if not root:
            return depth
        depth += 1
        return max(depth, self.maxDepth(root.left, depth), self.maxDepth(root.right, depth))

    def diameterOfBinaryTree(self, root: Optional[TreeNode], maxDiameter=0) -> int:
        if not root:
            return maxDiameter

        diameter = self.maxDepth(root.left) + self.maxDepth(root.right)
        maxDiameter = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(maxDiameter, diameter)


sln = Solution()
bt = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
res = sln.diameterOfBinaryTree(bt)
print(res)
