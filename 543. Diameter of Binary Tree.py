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
        self.output = 0

        
        def dfs(current):
            if not current:
                return 0
            
            left = dfs(current.left)
            right = dfs(current.right)

            # longest chain = longest left + longest right of a node
            self.output = max(self.output, left + right)

            # returns height to the left= and right=
            return 1 + max(left, right)

        dfs(root)
        return self.output

