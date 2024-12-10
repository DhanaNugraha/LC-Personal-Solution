# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive DFS solution
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if not root:
            return 0
        
        leftRoot = root.left
        rightRoot = root.right

        def maxLeft(leftSide):
            if not leftSide:
                return 0
            return 1 + max(maxLeft(leftSide.left), maxLeft(leftSide.right))
        
        def maxRight(rightSide):
            if not rightSide:
                return 0
            return 1 + max(maxLeft(rightSide.left), maxLeft(rightSide.right))

        return maxLeft(leftRoot) + maxRight(rightRoot)

