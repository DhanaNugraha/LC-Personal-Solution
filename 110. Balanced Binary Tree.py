# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        self.output = True

        def dfs(current):
            if not current:
                return 0
            
            left = dfs(current.left)
            right = dfs(current.right)
            difference = abs(left - right)

            if difference > 1:
                self.output = False


            return 1 + max(left, right)
        
        dfs(root)

        return self.output