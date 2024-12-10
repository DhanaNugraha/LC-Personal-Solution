# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        self.output = True

        def dfs(curP,curQ):
            if not curP or not curQ:
                if not curP and curQ or curP and not curQ:
                    self.output = False
                    return 
                else:
                    return 
                
            if curP.val != curQ.val:
                self.output = False
                return 
            
            dfs(curP.left, curQ.left)
            dfs(curP.right, curQ.right)
            return

        dfs(p, q)

        return self.output