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

# simpler solution
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)