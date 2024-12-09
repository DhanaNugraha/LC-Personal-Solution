# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # if empty return empty
        if not root:
            return None
        

        # Use DFS algorithm
        # when given value, swap right with left
        temporary = root.left
        root.left = root.right
        root.right = temporary

        # finish swapping the left side from main head
        self.invertTree(root.left)

        # swap right side
        self.invertTree(root.right)
        
        return root